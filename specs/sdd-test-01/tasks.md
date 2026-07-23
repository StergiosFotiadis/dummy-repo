# tasks.md

## ⛔ NO TASKS GENERATED

This spec has been evaluated against the repository constitution and **rejected at the plan stage** before task generation.

---

## Rejection Summary

| Stage | Outcome |
|---|---|
| **Spec → Plan** | Plan rejected spec as constitutionally incompatible |
| **Plan → Tasks** | No tasks can be produced from a rejected plan |

---

## Mandatory Stop Conditions

The pipeline halts here because the plan explicitly and unambiguously invokes the **Governance hard-stop clause**:

> *"Any change that conflicts with Principles I or II MUST be rejected regardless of who requests it or why."*

Generating tasks — even placeholder, stub, or investigative tasks — against a rejected plan would:

1. **Circumvent the governance clause** by advancing a prohibited spec further through the pipeline under the appearance of procedural compliance.
2. **Create an ambiguous audit trail** in violation of Principle IV (Traceable Test History), as any resulting commits could not carry valid scan-trigger commit messages.
3. **Risk real credential infrastructure** entering a fixture repository, violating Principle II (No Real Secrets / No Production Use) — specifically the FR-007 persistent token, FR-008 credential invalidation, and FR-012 identity-associated draft storage requirements.
4. **Introduce real business logic files** beyond the four permitted fixture files (`README.md`, `main.py`, `package.json`, `requirements.txt`), violating the Fixture Contents constraint.

---

## Required Actions Before This Pipeline Can Proceed

**Action 1 — Redirect the spec:**
Submit `spec.md` to the repository that hosts the actual user-facing application with a session layer, login UI, and draft storage. This spec was submitted to the wrong repository.

**Action 2 — If a task for *this* repository is genuinely needed, submit a compliant spec:**

A valid spec for this repository takes one of exactly two forms:

- **Form A (Scan Trigger):** A one-line change to `README.md` with a commit message following the established scan-trigger convention.
- **Form B (New Vulnerability Sample):** An addition of a labeled `VULNERABILITY N: <type>` block to `main.py`, a corresponding pin to a known-vulnerable library in `requirements.txt`, documentation in `README.md`, and a commit message referencing the vulnerability label.

Neither form involves session management, authentication tokens, remember-me UI, or draft persistence.

---

*Tasks stage produced zero task records. Pipeline must not advance.*