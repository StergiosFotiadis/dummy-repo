# plan.md

## Technical Context

**Language & Runtime:** This plan must be evaluated against the repository constitution before any technical choices are considered.

**Critical Finding:** This spec describes a **session management, authentication, and draft-preservation feature set** for a real user-facing application. It has no relationship whatsoever to the repository's stated purpose, which is a deliberately vulnerable dummy test fixture for validating the SecureScan scanning pipeline.

**The spec.md is categorically incompatible with this repository and this constitution.**

---

## Constitution Check

| Principle | Status | Analysis |
|---|---|---|
| **I. Intentional Vulnerability Preservation** | ⚠️ INDIRECT RISK | Implementing real session logic, authentication flows, and a "remember me" mechanism would introduce application code that auditors or tools might interact with, potentially obscuring or complicating the fixture's known-bad signal. More critically, none of this was ever part of the fixture. |
| **II. No Real Secrets / No Production Use** | 🚫 **VIOLATION** | FR-007 (30-day persistent auth tokens), FR-008 (invalidatable credentials), FR-012 (user-identity-associated draft storage) all require real authentication infrastructure and real credential handling. Implementing these in this repository would either introduce real secrets/tokens or require connecting to real systems — both are explicitly prohibited. |
| **III. Controlled, Labeled Change Only** | 🚫 **VIOLATION** | The entirety of this spec — session stability investigation, remember-me UI, draft preservation — is real application feature development. None of it qualifies as (a) a scan-trigger change or (b) a deliberate, labeled addition of a new vulnerability sample. This is exactly the "real features" and "real business logic" the constitution prohibits. |
| **IV. Traceable Test History** | 🚫 **VIOLATION** | No commit implementing this spec could carry a message consistent with the scan/webhook test trigger convention. The commit history would become ambiguous and would break the audit trail used to correlate scanner runs with triggering changes. |
| **Fixture Contents & Constraints** | 🚫 **VIOLATION** | The spec would require introducing multiple new files (session store, auth layer, UI components, draft persistence layer) that contain real business logic and real data flows. The constitution explicitly prohibits this. The only tracked fixture files are `README.md`, `main.py`, `package.json`, and `requirements.txt`. |
| **Governance** | 🚫 **VIOLATION** | Per the Governance section: "Any change that conflicts with Principles I or II MUST be rejected regardless of who requests it or why." This spec conflicts with Principle II (production-grade auth infrastructure with real credential lifecycle) and Principle III at minimum. It MUST be rejected. |

---

## Project Structure

**No project structure is produced.** This plan cannot proceed to a structure definition because the spec violates the constitution at the foundational level and MUST be rejected per the Governance clause before any implementation planning occurs.

**Required action:** The spec.md must be redirected to the correct repository — one that hosts the actual user-facing application described (with a session layer, login UI, and draft storage). It has been submitted to the wrong repository. This fixture repository requires no implementation work in response to this spec.

**What a valid spec for this repository would look like:** Either (a) a one-line README bump commit to trigger a scan, or (b) a new vulnerability sample addition (e.g., a `VULNERABILITY 4: insecure deserialization` block in `main.py`) with a corresponding `requirements.txt` pin to a known-vulnerable library version, both labeled with `VULNERABILITY N` markers and described in the commit message.