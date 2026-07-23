```markdown
# spec.md

## User Scenarios

**P1 – Security engineer expands scanner coverage with a deserialization test case**
As a security engineer maintaining the SecureScan fixture, I want to add a clearly labeled insecure deserialization vulnerability sample to `main.py` so that the scanner detects and reports on this additional vulnerability class, widening the pipeline's validated detection surface.

**P1 – Security engineer confirms all three fixture files reflect the new vulnerability**
As a security engineer, I want the new vulnerability sample to be consistently recorded across `main.py`, `requirements.txt`, and `README.md` so that the fixture surface remains coherent and the commit history accurately logs the addition as a scan/webhook trigger.

**P2 – Auditor traces a scanner alert back to the seeded vulnerability**
As an auditor reviewing scanner output, I want the `VULNERABILITY 4` marker in `main.py` and the README entry to match, so that I can correlate a specific scanner finding to its intentional test case without ambiguity.

**P3 – Future maintainer identifies the vulnerability class for retirement or replacement**
As a future maintainer, I want the vulnerability sample to carry a self-describing inline comment and a README description so that I can decide whether to retire or supersede it with minimal archaeology.

---

## Functional Requirements

**FR-001 – VULNERABILITY 4 block in main.py**
`main.py` MUST contain a new code block preceded by a comment marker in the exact form `# VULNERABILITY 4: Insecure Deserialization`, consistent with the style of existing vulnerability markers in the file. The block MUST demonstrate unsafe deserialization of untrusted input (e.g. passing unsanitized user-controlled data directly to a deserialization call). [NEEDS CLARIFICATION: Should the deserialization call use the Python standard-library `pickle` module specifically, or is any demonstrably unsafe deserialization mechanism (e.g. `yaml.load` without `Loader`, `marshal`) acceptable?]

**FR-002 – No functional remediation within the VULNERABILITY 4 block**
The VULNERABILITY 4 code block MUST NOT include input validation, safe-load alternatives, sandboxing, or any other mitigating pattern. The insecure path MUST be the only path shown, in accordance with Constitution Principle I.

**FR-003 – Placeholder/fake input data only**
Any data, file paths, or variable values used within the VULNERABILITY 4 block MUST be obviously fake or example values. No real serialized payloads from production systems MUST appear, in accordance with Constitution Principle II.

**FR-004 – Pinned vulnerable library version in requirements.txt**
`requirements.txt` MUST gain exactly one new entry: a pinned, known-vulnerable version of a library relevant to the deserialization vulnerability class. The pinned version MUST be a real, historically published version documented to carry a relevant CVE or known exploit. [NEEDS CLARIFICATION: Is there a preferred library and version already under consideration (e.g. a specific `PyYAML` or serialization-adjacent package with a known CVE), or should the spec leave library selection open provided the CVE relevance is documentable?]

**FR-005 – No removal or alteration of existing vulnerable pins**
The existing pinned dependency entries in `requirements.txt` (VULNERABILITY 1–3 era pins) MUST remain unchanged. The new entry MUST be additive only.

**FR-006 – README vulnerability list entry**
`README.md` MUST contain a new entry in the existing seeded-vulnerability list that identifies VULNERABILITY 4 by number, names the vulnerability class (Insecure Deserialization), and references the relevant library or call site, consistent in format with existing entries.

**FR-007 – Commit message convention**
The commit message for this change MUST reference `VULNERABILITY 4` and describe the vulnerability class being added (e.g. "Add VULNERABILITY 4: Insecure Deserialization sample"), satisfying Constitution Principle IV's traceability requirement.

**FR-008 – No unrelated changes**
The commit MUST NOT include changes to any file or code path outside the scope of `main.py`, `requirements.txt`, and `README.md` for this vulnerability addition, except for `.specify/` or `.claude/` tooling files if a plan or spec artifact is being committed alongside.

---

## Success Criteria

**SC-001 – Marker format exact match**
The string `# VULNERABILITY 4: Insecure Deserialization` (or the agreed vulnerability-class label) appears verbatim in `main.py` immediately preceding the insecure deserialization code block.

**SC-002 – Scanner detects the new vulnerability class**
On the next triggered scan following this commit, the SecureScan pipeline produces at least one finding attributable to the insecure deserialization pattern introduced in the VULNERABILITY 4 block.

**SC-003 – requirements.txt pin is real and CVE-linked**
The newly pinned library version in `requirements.txt` resolves to a historically published package version for which a CVE or documented vulnerability exists; no unpublished, invented, or yanked version is used.

**SC-004 – README entry present and consistent**
`README.md` contains an entry for VULNERABILITY 4 whose vulnerability class label matches the inline comment in `main.py`.

**SC-005 – Existing vulnerabilities unaffected**
VULNERABILITY 1, 2, and 3 blocks in `main.py`, their corresponding pins in `requirements.txt`, and their README entries are byte-for-byte identical before and after this change.

**SC-006 – No real or reusable secrets introduced**
Automated secret-scanning of the commit (or manual review) finds zero credentials, keys, or tokens that are not obviously fake example values.

**SC-007 – Commit message references VULNERABILITY 4**
The commit message contains the substring `VULNERABILITY 4` and a description of the vulnerability class, satisfying the audit-trail requirement of Constitution Principle IV.

---

## Key Entities

| Entity | Description |
|---|---|
| `main.py` | Primary fixture file hosting all seeded vulnerability code blocks; target of the VULNERABILITY 4 insertion. |
| `requirements.txt` | Pip dependency pin file; holds intentionally vulnerable library versions corresponding to fixture vulnerabilities. |
| `README.md` | Scan-trigger log and vulnerability inventory; must document VULNERABILITY 4 alongside existing entries. |
| VULNERABILITY 4 block | The new, labeled insecure deserialization code sample to be inserted into `main.py`. |
| Pinned vulnerable library | A real, historically published package version with a known CVE relevant to insecure deserialization, to be added to `requirements.txt`. |
| SecureScan pipeline | The scanner that consumes this fixture repository and whose detection coverage this change is intended to extend. |
| Constitution Principle I | The non-negotiable rule that seeded vulnerabilities must not be remediated; governs the VULNERABILITY 4 block's content. |
| Constitution Principle II | The rule that no real secrets or production values may appear; governs the fake-data requirement in FR-003. |
| Constitution Principle III | The controlled-change rule requiring `VULNERABILITY N` comment markers and no unrelated logic. |
| Constitution Principle IV | The traceability rule governing commit message content. |
```