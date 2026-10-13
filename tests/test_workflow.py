"""Static checks of the CI workflow (QC-WF-001 criterion 24, MIL-001 task 7)."""

import re
from collections.abc import Hashable, Iterator
from pathlib import Path
from typing import Any

import pytest
import yaml

ROOT = Path(__file__).parents[1]
WORKFLOW_PATH = ROOT / ".gitea" / "workflows" / "ci.yml"
GITHUB_WORKFLOW_PATH = ROOT / ".github" / "workflows" / "ci.yml"
MAX_RUN_LINES = 5
EXACT_TAG = re.compile(r"@v\d+\.\d+\.\d+$")
FULL_SHA = re.compile(r"@[0-9a-f]{40}$")

# Parsed YAML is untyped data, so Any is the honest type here.
Workflow = dict[Any, Any]


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe loader that rejects a mapping with a repeated key."""

    def construct_mapping(
        self, node: yaml.MappingNode, deep: bool = False
    ) -> dict[Hashable, Any]:
        """Build the mapping, raising ValueError on a duplicate key."""
        seen: set[Hashable] = set()
        for key_node, _ in node.value:
            key = self.construct_object(key_node, deep=deep)
            if key in seen:
                raise ValueError(f"duplicate key {key!r} at {key_node.start_mark}")
            seen.add(key)
        return super().construct_mapping(node, deep=deep)


def load_workflow() -> Workflow:
    """Parse the workflow with the safe loader."""
    loaded = yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))
    assert isinstance(loaded, dict)
    return loaded


def triggers(workflow: Workflow) -> Any:
    """Return the trigger section; YAML 1.1 reads the key `on` as True."""
    return workflow["on"] if "on" in workflow else workflow[True]


def trigger_names(workflow: Workflow) -> set[str]:
    """Return the names of the events that trigger the workflow."""
    section = triggers(workflow)
    if isinstance(section, str):
        return {section}
    return {str(name) for name in section}


def jobs(workflow: Workflow) -> dict[str, Workflow]:
    """Return the jobs by id."""
    found: dict[str, Workflow] = workflow["jobs"]
    return found


def steps(job: Workflow) -> list[Workflow]:
    """Return the steps of a job."""
    found: list[Workflow] = job.get("steps", [])
    return found


def all_steps(workflow: Workflow) -> Iterator[Workflow]:
    """Yield every step of every job."""
    for job in jobs(workflow).values():
        yield from steps(job)


def exceeds_line_limit(script: str, limit: int = MAX_RUN_LINES) -> bool:
    """Tell whether a script has more lines than the limit, as written.

    Blank lines and comments count.
    """
    return len(script.splitlines()) > limit


def test_workflow_parses_with_required_keys() -> None:
    """The file is valid YAML with a name, a trigger and jobs."""
    workflow = load_workflow()
    assert "name" in workflow
    assert "on" in workflow or True in workflow
    assert "jobs" in workflow


def test_workflow_has_no_duplicate_keys() -> None:
    """No mapping in the file repeats a key."""
    text = WORKFLOW_PATH.read_text(encoding="utf-8")
    assert yaml.load(text, Loader=UniqueKeyLoader) is not None


def test_duplicate_key_loader_rejects_repeated_key() -> None:
    """The duplicate-key loader bites on a repeated key."""
    with pytest.raises(ValueError, match="duplicate key"):
        yaml.load("a: 1\na: 2\n", Loader=UniqueKeyLoader)


def test_permissions_are_declared() -> None:
    """Permissions are set at workflow level or on every job."""
    workflow = load_workflow()
    if "permissions" in workflow:
        return
    assert all("permissions" in job for job in jobs(workflow).values())


def test_every_job_has_runner_and_timeout() -> None:
    """Each job names its runner and a timeout."""
    for job_id, job in jobs(load_workflow()).items():
        assert "runs-on" in job, job_id
        assert "timeout-minutes" in job, job_id


def test_every_step_has_a_name() -> None:
    """Each step carries a name."""
    for job_id, job in jobs(load_workflow()).items():
        for step in steps(job):
            assert "name" in step, f"{job_id}: {step}"


def test_step_names_are_unique_within_a_job() -> None:
    """No two steps of one job share a name."""
    for job_id, job in jobs(load_workflow()).items():
        names = [step["name"] for step in steps(job) if "name" in step]
        assert len(names) == len(set(names)), job_id


def test_uses_are_pinned_to_exact_release_or_sha() -> None:
    """Each action is pinned to an exact tag or a full commit SHA."""
    for step in all_steps(load_workflow()):
        if "uses" in step:
            ref = str(step["uses"])
            assert EXACT_TAG.search(ref) or FULL_SHA.search(ref), ref


def test_run_blocks_stay_within_line_limit() -> None:
    """No inline script is longer than the limit."""
    for step in all_steps(load_workflow()):
        if "run" in step:
            assert not exceeds_line_limit(str(step["run"])), step.get("name")


def test_line_limit_check_rejects_six_lines() -> None:
    """The line-limit helper counts lines as written, blank lines included."""
    assert exceeds_line_limit("a\nb\nc\nd\ne\nf\n")
    assert exceeds_line_limit("a\nb\nc\nd\ne\n\n")
    assert not exceeds_line_limit("a\nb\n\nc\nd\n")


def test_workflow_uses_no_secrets() -> None:
    """The file refers to no secret."""
    assert "secrets." not in WORKFLOW_PATH.read_text(encoding="utf-8")


def test_workflow_is_not_triggered_by_pull_request_target() -> None:
    """The privileged pull_request_target trigger is not used."""
    assert "pull_request_target" not in trigger_names(load_workflow())


def test_workflow_is_not_duplicated_for_github() -> None:
    """The same workflow does not also live under .github/workflows."""
    assert not GITHUB_WORKFLOW_PATH.exists()
