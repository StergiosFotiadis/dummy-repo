# tasks.md

## Story 1: Add insecure deserialization code block to main.py (FR-001, FR-002, FR-003, SC-001, SC-002, SC-006)

- **T001** — Open `main.py` and append a clearly labeled comment `# VULNERABILITY 4: Insecure Deserialization` immediately before the new code block, ensuring no existing VULNERABILITY 1–3 blocks or their surrounding code are altered in any way.
- **T002** — Immediately following the T001 comment, append a self-contained Python code block that imports `pickle` from the standard library and calls `pickle.loads()` on a hardcoded, obviously fake placeholder byte string (e.g., a literal `b"..."` constant with no real payload, credentials, or live data), with no safe-load alternative, no try/except mitigation, and no Loader restriction. [P]
- **T003** — Verify that `main.py` still contains all existing VULNERABILITY 1–3 blocks verbatim and unchanged (character-level diff confirms zero modifications to pre-existing lines). [P]
- **T004** — Verify that the new block in `main.py` contains no real secrets, no production-sourced data, and no credentials (manual inspection + grep for known secret patterns). [P]

---

## Story 2: Pin CVE-documented deserialization-class library in requirements.txt (FR-004, SC-003, SC-005)

- **T005** — Open `requirements.txt` and append exactly one new line: `PyYAML==5.3.1`, leaving all existing dependency pins for VULNERABILITY 1–3 unchanged.
- **T006** — Verify that the added line `PyYAML==5.3.1` is present in `requirements.txt` and that `PyYAML==5.3.1` is a real, publicly available version on PyPI historically documented under CVE-2020-14343. [P]
- **T007** — Verify that all pre-existing dependency pin lines in `requirements.txt` are unmodified (character-level diff confirms zero changes to pre-existing lines). [P]

---

## Story 3: Add VULNERABILITY 4 inventory entry to README.md (FR-006, SC-004, SC-005)

- **T008** — Open `README.md` and append a new VULNERABILITY 4 entry to the vulnerability inventory section, including: the sequential number (4), the class label "Insecure Deserialization", a reference to the `pickle.loads()` call site in `main.py`, and a reference to the `PyYAML==5.3.1` pin and CVE-2020-14343.
- **T009** — Verify that all existing scan-trigger log entries and VULNERABILITY 1–3 inventory entries in `README.md` are present verbatim and unmodified (character-level diff confirms zero changes to pre-existing lines). [P]
- **T010** — Verify that the new README entry correctly cross-references both the `main.py` call site and the `requirements.txt` CVE pin with accurate labels and no placeholder text remaining. [P]

---

## Story 4: Validate scanner detectability and end-to-end fixture integrity (FR-001, FR-004, SC-001, SC-003)

- **T011** — Run a static analysis tool (e.g., Bandit) against `main.py` and confirm it raises at least one finding categorized under deserialization or unsafe use of `pickle` for the new VULNERABILITY 4 block, without suppressing or altering findings for VULNERABILITY 1–3. [P]
- **T012** — Run a dependency vulnerability scanner (e.g., `pip-audit` or `safety`) against `requirements.txt` and confirm it surfaces CVE-2020-14343 for the `PyYAML==5.3.1` pin, without suppressing findings for existing vulnerable pins. [P]
- **T013** — Confirm the overall fixture remains syntactically valid Python by running `python -m py_compile main.py` with a zero exit code.

---

## Story 5: Commit with traceable, correctly formed message (FR-007, SC-007)

- **T014** — Stage only the three modified files (`main.py`, `requirements.txt`, `README.md`) and confirm no other tracked files appear in the diff (e.g., `package.json`, any `.specify/` non-exempt file). [P]
- **T015** — Commit the staged changes with a message containing the substring `VULNERABILITY 4` and naming the vulnerability class, e.g.: `"Add VULNERABILITY 4: Insecure Deserialization sample"`, and verify the resulting commit log entry contains both required substrings.