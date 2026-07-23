# plan.md

## Technical Context

**Language:** Python (the fixture's primary language, per `main.py`)

**Framework:** None — this is not an application; it is a static, deliberately vulnerable code fixture evaluated by an external scanner (SecureScan).

**Storage / dependency manifests:**
- `requirements.txt` — pip pin file; the vehicle for introducing a CVE-linked deserialization-relevant package version
- `package.json` — not touched by this change (no JavaScript deserialization sample is in scope)
- `README.md` — plain Markdown; serves as the scan-trigger log and vulnerability inventory

**Deserialization mechanism choice (resolving FR-001 clarification):** Python's standard-library `pickle` module. Rationale: `pickle` is universally recognized by security scanners as an unsafe deserialization sink, has no safe-load alternative that would tempt a future maintainer to "fix" it, and does not require a third-party import — keeping the vulnerability self-contained in `main.py`. The paired `requirements.txt` entry will use a separately CVE-documented serialization-adjacent library (e.g. `PyYAML==5.3.1`, CVE-2020-14343, which is a deserialization-class vulnerability) to satisfy FR-004 independently of the `pickle` call site.

**Pinned library choice (resolving FR-004 clarification):** `PyYAML==5.3.1` — a real, historically published version, documented under CVE-2020-14343 (arbitrary code execution via `yaml.load` without a safe Loader). This version is publicly available on PyPI and has a well-documented CVE, satisfying SC-003.

---

## Constitution Check

**Principle I — Intentional Vulnerability Preservation (NON-NEGOTIABLE):**
Compliant. The plan adds VULNERABILITY 4 as a purely additive block; no existing VULNERABILITY 1–3 blocks, their pins, or their README entries are altered. SC-005 and FR-005 are structurally enforced by the additive-only nature of every file change described below.

**Principle II — No Real Secrets / No Production Use:**
Compliant. The `pickle` code block will operate on an obviously fake, hardcoded placeholder byte string (e.g. a literal example value, not sourced from any real system). No credentials, keys, or live payloads are introduced. FR-003 and SC-006 are satisfied.

**Principle III — Controlled, Labeled Change Only:**
Compliant. Every file change is in direct service of adding a new vulnerability sample. The `# VULNERABILITY 4: Insecure Deserialization` marker will appear verbatim in `main.py` immediately before the insecure block (FR-001, SC-001). No unrelated logic, cleanup, or real features are introduced (FR-008).

**Principle IV — Traceable Test History:**
Compliant. The commit message will contain the substring `VULNERABILITY 4` and name the vulnerability class (e.g. `"Add VULNERABILITY 4: Insecure Deserialization sample"`), satisfying FR-007 and SC-007 and maintaining the audit trail the constitution requires.

**Fixture Contents & Constraints:**
Compliant. Only `main.py`, `requirements.txt`, and `README.md` are modified — all three are explicitly listed as tracked fixture surface. No new files are introduced to the fixture layer. `.specify/` plan artifact is exempt per the constitution's tooling carve-out.

**Governance:**
No constitution amendment is needed or made. This change is a straightforward Principle III category-(b) addition and requires no governance action beyond a correctly formed commit message.

---

## Project Structure

```
/                                   ← repository root (fixture)
│
├── main.py                         ← MODIFIED
│   ├── [existing VULNERABILITY 1 block — unchanged]
│   ├── [existing VULNERABILITY 2 block — unchanged]
│   ├── [existing VULNERABILITY 3 block — unchanged]
│   └── # VULNERABILITY 4: Insecure Deserialization
│       └── [new pickle-based unsafe deserialization block,
│            fake/placeholder input data only, no mitigations]
│
├── requirements.txt                ← MODIFIED (additive only)
│   ├── [existing vulnerable pins for VULNERABILITY 1–3 — unchanged]
│   └── PyYAML==5.3.1              ← new pin; CVE-2020-14343; deserialization class
│
├── README.md                       ← MODIFIED (additive only)
│   ├── [existing scan-trigger log entries — unchanged]
│   ├── [existing VULNERABILITY 1–3 inventory entries — unchanged]
│   └── [new VULNERABILITY 4 entry: number, class label "Insecure Deserialization",
│         reference to pickle call site in main.py and PyYAML CVE pin]
│
├── package.json                    ← NOT TOUCHED (out of scope)
│
└── .specify/                       ← tooling scaffolding (exempt from fixture rules)
    └── specs/
        └── [this plan.md artifact]
```