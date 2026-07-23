<!--
Sync Impact Report
==================
Version change: (template) → 1.0.0
Rationale: Initial ratification. The prior file was the unfilled constitution
template (all placeholder tokens); this is the first concrete constitution
for this repository, so MINOR/PATCH semantics don't apply — this is the
initial adoption (1.0.0).

Modified principles: n/a (first fill, no renames)

Added sections:
- Core Principles: I. Intentional Vulnerability Preservation (NON-NEGOTIABLE),
  II. No Real Secrets / No Production Use, III. Controlled, Labeled Change
  Only, IV. Traceable Test History
- Fixture Contents & Constraints
- Change Workflow
- Governance

Removed sections: none

Templates requiring updates:
- ✅ .specify/templates/plan-template.md — generic "Constitution Check" gate
  references the constitution file, no agent-specific wording to fix, no
  change needed.
- ✅ .specify/templates/spec-template.md — no constitution-coupled content
  found, no change needed.
- ✅ .specify/templates/tasks-template.md — no constitution-coupled content
  found, no change needed.
- ✅ .claude/skills/speckit-constitution — generic instructions, no
  agent-specific references to fix.

Follow-up TODOs: none. Ratification date derived from the repository's
initial commit (fe510b5, "Initial commit of vulnerable test files").
-->

# SecureScan Dummy Test Fixture Constitution

This repository is not a software product. It is a deliberately vulnerable,
disposable fixture used to trigger and validate the SecureScan scanning
pipeline (including its Discord webhook notifications). Every principle
below exists to protect that single purpose.

## Core Principles

### I. Intentional Vulnerability Preservation (NON-NEGOTIABLE)
The known, seeded vulnerabilities in this repository — including but not
limited to the hardcoded example credentials and SQL injection pattern in
`main.py`, and the outdated/vulnerable pinned dependencies in
`package.json` and `requirements.txt` — MUST remain present and MUST NOT be
"fixed," patched, remediated, or refactored away. A change that removes,
masks, or neutralizes an existing seeded vulnerability without an explicit,
documented decision to retire that test case is a constitution violation.
Rationale: the repository's entire value is being a stable, known-bad
target; silently fixing it breaks scanner test coverage and invalidates
prior scan baselines.

### II. No Real Secrets / No Production Use
All credentials, keys, and passwords committed to this repository MUST be
well-known placeholder/example values (e.g. the AWS documentation example
key pair) or otherwise obviously fake — never a real, live, or reusable
secret. This repository MUST NOT be deployed, executed against real
infrastructure, connected to production systems, or used as a dependency
by real software. Rationale: the repo is publicly/internally exercised by
a scanner and its notifications; any real secret placed here is presumed
compromised the moment it's committed.

### III. Controlled, Labeled Change Only
Changes to this repository MUST fall into one of two categories: (a) a
scan-trigger change (e.g. a README bump, a commit made solely to fire a
scan or webhook), or (b) a deliberate, clearly labeled addition of a new
vulnerability sample for expanded scanner test coverage. New vulnerability
samples MUST be commented in-code with a `VULNERABILITY N: <type>` marker,
consistent with the existing style in `main.py`. Unrelated application
logic, real features, or "cleanup" of the vulnerable code paths MUST NOT
be introduced. Rationale: keeps the fixture legible as a test asset rather
than drifting into a real, ambiguous codebase.

### IV. Traceable Test History
Every commit MUST make its purpose as a scan/webhook test trigger evident
from its commit message (following the existing "Nth test" / "trigger scan"
/ "testing X webhook" convention) or, for vulnerability-sample additions,
describe the vulnerability being added. Rationale: the commit history is
itself a test log used to correlate scanner runs and webhook deliveries
with the change that triggered them; ambiguous messages break that audit
trail.

## Fixture Contents & Constraints

The repository's tracked surface is intentionally small: `README.md`
(scan-trigger log), `main.py` (seeded vulnerability samples),
`package.json` (vulnerable npm dependency pins), and `requirements.txt`
(vulnerable pip dependency pins). Any new file added to the repository
MUST serve one of the two purposes in Principle III and MUST NOT introduce
real business logic, real data, or a real build/deploy pipeline. The
`.specify/` and `.claude/` scaffolding directories support spec-driven
workflows for maintaining this fixture and are exempt from the "no real
logic" constraint since they are tooling, not the fixture itself.

## Change Workflow

To trigger a scan: make a minimal, clearly-labeled commit (e.g. a README
line bump) and push — no review gate is required for pure trigger commits.
To add a new vulnerability sample: add the code with a `VULNERABILITY N`
comment marker, describe the vulnerability class in the commit message,
and note it in the README's scan-trigger log. To retire a vulnerability
sample: this requires an explicit decision recorded in the commit message
explaining why that test case is no longer needed (e.g. superseded by a
better sample), satisfying the exception carved out in Principle I.

## Governance

This constitution supersedes ad hoc judgment calls about what belongs in
this repository. Any change that conflicts with Principles I or II MUST be
rejected regardless of who requests it or why, since those two principles
protect the fixture's core purpose and safety. Amendments to this
constitution (adding/removing principles, changing the fixture's scope)
require the change to be made directly to this file with an updated Sync
Impact Report and version bump, following semantic versioning: MAJOR for
removing or redefining a principle, MINOR for adding a principle or
materially expanding a section, PATCH for wording/clarification only.
Compliance is self-checked at commit time against Principles I–IV above;
there is no separate CI gate for this repository.

**Version**: 1.0.0 | **Ratified**: 2026-05-19 | **Last Amended**: 2026-07-21
