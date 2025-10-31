---
task_id: TASK-2025-10-31-002
owner: "Claude"
assignee: "Claude"
report_to: "Nova"
priority: "High"
category: "SECURITY|PROCESS|LINTER"
created: "2025-10-31"
due: "2025-11-04"
status: "OPEN"
session_id: "tier4-courier-0002"
---
# TASK: Ethical Invariant Integration — Schema + Linter + SMV Hooks

## Principle
**Never allow an unexamined purpose to occupy a stable pattern.**

## Objectives
- Encode the invariant as a JSON Schema for doc front-matter.
- Provide a **pre-commit (or CI) linter** that flags “stable-but-unexamined” artifacts.
- Publish a **reflection template** for quick remediation.
- Define the **SMV overlay API** so the visualizer reflects violations.

## Success Criteria
1. `schemas/NOVA_INVARIANT.schema.json` validates 3 sample docs (pass/fail cases).
2. `tools/pre-commit/invariant_linter` blocks violating commits (allow explicit bypass with reason).
3. `docs/ethics/REFLECTION_TEMPLATE.md` created and referenced by linter output.
4. `docs/smv/constraints.md` documents overlay fields consumed by SMV (e.g., `violation`, `violatingArtifacts`, `capped_S_avg`).

## Deliverables
- `schemas/NOVA_INVARIANT.schema.json`
- `tools/pre-commit/invariant_linter` (+ README)
- `docs/ethics/REFLECTION_TEMPLATE.md`
- `docs/smv/constraints.md`
- `tests/ethics/sample_docs/` (pass/fail set)

## Front-matter (target shape)
```yaml
role: "readme|spec|process|artifact|index|relay"
owner: "Nova"
purpose: "One-sentence telos."
assumptions:
  - "Precondition 1"
justification: "Why this advances goals."
review:
  evidence: ["/docs/Validation/result_X.md"]
  last_reviewed: "2025-10-31"
stability_hints:
  references: 3
  resolution_score: 0.92
  age_hours: 56
status: "aligned"
```

## Linter Behavior (minimum)
- Parse staged `.md` files’ front-matter.
- If **stable** (≥3 refs OR score ≥0.9 OR age ≥48h) and missing/freshness fails → **block** and print remediation using the reflection template.
- Provide `--ethics-bypass "reason"` flag; record a lightweight local trace file (no external log dependency).

## Dependencies
- None on VuDu. No shared logging required.

## Validation & Review
- Run schema validation on test docs; show expected failures.
- Demonstrate linter blocking + bypass trace creation.
- Nova reviews `docs/smv/constraints.md` so SMV overlay aligns.
