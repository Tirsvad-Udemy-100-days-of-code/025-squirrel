# RC Review of ci.yml against the workflow checklist

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-010 |
| CrossReference | [WF-MIL-001], [QC-WF-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Deprecated | Jens Tirsvad Nielsen | AI as stand-in for S01 | Action items closed: criterion 22 by RC-025 (Go), criterion 24 by RC-030 (Go) | [40c3387] |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Link definitions added for the IDs cited in the text | [5b948e5] |

---

## Artifact Under Review

- Instance reviewed: [WF-MIL-001]
- Checklist used: [QC-WF-001]
- Scope: full review
- Language and domain: n/a
- Language reviewer: none (the stand-in reviewer reads English and the `it` domain)
- Mode: autonomous, not independent (reviewer: AI as stand-in for S01)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The file meets the YAML checklist ([QC-YML-001]) (Mandatory) | Pass | See RC-009: YAML checklist passes. |
| 2 | The file is in `.gitea/workflows/` or `.github/workflows/` with the extension `.yml` or `.yaml`, and the same workflow does not exist in both directories (Mandatory) | Pass | File is in `.gitea/workflows/` only; no `.github/workflows/` copy. |
| 3 | The file declares `name`, `on` and `jobs`; `on` lists explicit events and, where it matters, `branches` or `paths` (Mandatory) | Pass | `name`, `on` (push to main, pull_request) and `jobs` are declared. |
| 4 | A header comment states the purpose, the triggers, the inputs, the secrets it needs, what it changes outside the repository, and the decision or milestone it implements (Mandatory) | Pass | Header comment states purpose, triggers, secrets (none), outside effects (none) and decision. |
| 5 | Every job and step has a descriptive `name`, unique within its job (Mandatory) | Pass | Every job and step has a unique descriptive `name`. |
| 6 | The file passes `actionlint` (or the project's workflow validation test) and the tool version is stated (Mandatory) | Pass | `actionlint 1.7.12` reports no findings. |
| 7 | Every job declares `permissions` explicitly with the least access that works (`contents: read` or none by default); write access only on the job that needs it (Mandatory) | Pass | Workflow-level `permissions: contents: read`. |
| 8 | Every action used is pinned to a full commit SHA or an exact release tag, never to a branch; a moving major tag (`@v1`) is accepted only for an action published by the same organisation under a stated release policy (Mandatory) | Pass | `actions/checkout@v4.2.2` and `actions/setup-python@v5.6.0` are exact release tags. |
| 9 | No secret is written in the file; a secret is read as `secrets.NAME`, passed to a step through `env:`, never placed on a command line or echoed (Mandatory) | Pass | No secret is used. |
| 10 | Untrusted text (`inputs.*`, event fields such as a title, branch name or label, step outputs derived from them) is never interpolated into a `run:` script; it is passed through `env:` and used as a quoted variable (Mandatory) | Pass | No event field or input reaches a `run:` script; `PIP_VERSION` is a workflow `env` value used as a quoted shell variable. |
| 11 | A trigger that gives a run secrets or a write token on code from a fork or an untrusted branch (`pull_request_target`, `workflow_run`) does not check out or execute that code (Mandatory) | Pass | Trigger is `pull_request`, not `pull_request_target`. |
| 12 | A workflow that changes state outside the repository (release, tag, publish, sync, deploy) is started by hand or by a protected branch, and a manual run defaults to a dry run with an explicit input to apply (Mandatory) | Pass | The workflow changes nothing outside the repository. |
| 13 | The token the workflow uses has only the scope the job needs, and where the host's built-in token is enough it is used instead of a personal token (Optional) | Pass | No token is used. |
| 14 | Every job sets `runs-on` to an explicit label and `timeout-minutes` (Mandatory) | Pass | `runs-on: ubuntu-latest` and `timeout-minutes: 10`. |
| 15 | `concurrency` is set where two runs would conflict: a check cancels the older run (`cancel-in-progress: true`); a publishing job queues (`cancel-in-progress: false`) (Mandatory) | Pass | Concurrency group per ref with `cancel-in-progress: true`. |
| 16 | Triggers are filtered (`branches`, `paths`, `types`) so the workflow runs only for the changes it concerns (Mandatory) | Pass | Push filtered to `main`; pull requests run for all branches. |
| 17 | Tools and dependencies are installed at pinned versions; a version is a workflow input with a default or a value in one place (Mandatory) | Pass | Python version and pip version are workflow `env` values; tool versions are exact in `pyproject.toml`. |
| 18 | A dependency cache is used where the install is slow enough to matter (Optional) | N-A | Install takes seconds; a cache would add complexity without benefit. |
| 19 | A failing step names the tool, the file and the reason in its log (annotation or `::error::` line) (Optional) | Pass | pytest names the failing file, test and reason in the log and exits non-zero. |
| 20 | A `run:` block is within the limit on embedded program text of criterion 7 of [QC-YML-001]; a longer script is a file (`tools/`, or a shared repository fetched at a pinned ref) that the step calls with one command, and the workflow passes its settings through `env:` (Mandatory) | Pass | Longest `run:` block is 3 lines. |
| 21 | Logic used by more than one workflow or repository is a reusable workflow (`workflow_call`) or a composite action; each input has a `description`, a `type` and a `default` where one is sensible (Mandatory) | N-A | Single workflow; nothing is shared. |
| 22 | Every workflow feature used is verified on the instance that runs it, and the host and version are recorded; a feature the target hosts differ on is noted in the header (Mandatory) | Fail | Gitea 1.27.3 and runner labels (`ubuntu-latest`) are known, but the run of this workflow stayed `queued` for over 15 minutes on the only runner (busy), so the features are not yet verified on the instance. |
| 23 | A reusable workflow states, in its header, how a caller pins it and the script it fetches, so the workflow and its script are the same release (Optional) | N-A | Not a reusable workflow. |
| 24 | A static test of the repository's workflows exists and runs on every pull request: valid YAML, required keys, explicit permissions and runner, no inline script above the limit (Optional) | Fail | No static workflow test exists; actionlint and yamllint were run by hand. |

## Overall Verdict

Go-with-conditions — all Mandatory criteria pass except 22: the workflow has not yet run on the instance. The commands it runs were executed locally (pytest 6 passed, ruff, mypy --strict).

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| Re-check criterion 22 when run 1012 or the next run on main completes; record the result in a delta re-review | S01 | 2026-10-16 |
| Decide whether to add a static workflow test (criterion 24, optional) | S01 | 2026-10-16 |

---

[WF-MIL-001]: ../../../.gitea/workflows/ci.yml
[QC-WF-001]: ../../../framework/qc/code/qc-workflow.md
[40c3387]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/40c3387ea7a4b601e8d20a5a7b6eba20c3d5323d
[QC-YML-001]: ../../../framework/qc/code/qc-yaml.md
[5b948e5]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/025-squirrel/commit/5b948e5a66bbcea5ef062f4557f47aae113a4e07
