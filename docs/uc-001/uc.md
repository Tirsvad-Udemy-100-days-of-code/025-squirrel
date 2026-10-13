# Use Case (Brief/Casual/Fully Dressed)

## Metadata
| Key | Value |
| --- | --- |
| ID | UC-001 |
| CrossReference | [UCD-001], [US-001], [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-10-13 | Accepted | Jens Tirsvad Nielsen | AI as stand-in for S01 | Initial version | pending |

---

**Format:** Fully Dressed

- **Scope:** Squirrel census program
- **Level:** user-goal
- **Primary Actor:** Participant (as named in [UCD-001])
- **Stakeholders and Interests:**
  - S01 — a correct summary that matches the dataset and the assignment
  - S02 — a result that is easy to reproduce from the README
  - S03 — a program with no runtime dependencies
- **Preconditions:** The participant has the census file.
- **Postconditions (success guarantee):** The summary file exists and holds the colour count of Gray, Cinnamon and Black; the participant has seen the counts.

### Main Success Scenario

1. The participant supplies the census file and the name of the summary file.
2. The system counts the squirrel sightings of each fur colour.
3. The system writes the summary to the summary file.
4. The system shows the participant the colour count of each fur colour.

### Extensions / Alternative Flows

- 1a. The census file does not exist: the system tells the participant that the file is missing and ends without writing a summary.
- 2a. A squirrel sighting has no fur colour: the system leaves it out of every colour count.

### Special Requirements / Business Rules

- Step 2: only the fur colours Gray, Cinnamon and Black are counted; a colour count is the number of sightings with that exact fur colour.
- Step 3: the summary has one row per counted fur colour, in the order Gray, Cinnamon, Black.

### Open Issues

None.

---

[UCD-001]: ../use-case-diagram.md
[US-001]: ../user-stories.md
[SA-001]: ../stakeholder-analysis.md
