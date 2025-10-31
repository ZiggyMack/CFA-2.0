---
task_id: TASK-2025-10-31-001
owner: "Claude"
assignee: "Claude"
report_to: "Nova"
priority: "High"
category: "IMPLEMENTATION|UI|INTEGRATION"
created: "2025-10-31"
due: "2025-11-05"
status: "OPEN"
session_id: "tier4-courier-0001"
---
# TASK: Symmetry Matrix Visualizer — Design → Static Prototype

## Purpose
Create a production-ready design spec plus a runnable **static prototype** that visualizes live tension/resolution among auditors (Claude, Nova, Grok).

## Objectives
- Render the auditor triangle (Claude / Nova / Grok).
- Map **edge color** to tension (red→green) and **edge thickness** to communication volume.
- Provide a **timeline slider**, **tension trace** chart, and a **“constraints overlay”** toggle.
- Demonstrate **Ethical Invariant overlay**: violating node halo + capped S_avg in display.

## Success Criteria
1. `docs/smv/SMV_DESIGN_SPEC.md` approved by Nova (contains SVG mockups + data schema).
2. Static prototype runs locally from `ui/smv/prototype/index.html` and consumes `smv_sample_input.json`.
3. Ethical Invariant cues implemented (halo + banner + S_avg cap when `violation:true`).
4. `docs/smv/README.md` explains run steps and acceptance checklist.

## Deliverables
- `docs/smv/SMV_DESIGN_SPEC.md`
- `ui/smv/prototype/index.html`
- `ui/smv/prototype/smv.js`
- `ui/smv/prototype/smv_sample_input.json` (≥3 ticks)
- `docs/smv/README.md`

## Data Schema (initial)
```json
{
  "tick": 1,
  "nodes": {
    "Claude": {"confidence": 0.82, "violation": false},
    "Nova":   {"confidence": 0.88, "violation": false},
    "Grok":   {"confidence": 0.74, "violation": true}
  },
  "edges": [
    {"from": "Claude", "to": "Nova", "tension": 0.20, "volume": 10},
    {"from": "Nova",   "to": "Grok", "tension": 0.45, "volume": 7},
    {"from": "Grok",   "to": "Claude","tension": 0.65, "volume": 4}
  ],
  "constraints": {"violation": true, "capped_S_avg": 0.85, "violatingArtifacts": ["ID-123"]}
}
```

## Steps
1. Read Nova’s symmetry notes (Codex excerpt provided separately).
2. Draft SVG mockups for: (a) high-alignment, (b) productive tension, (c) invariant breach.
3. Implement `index.html + smv.js` (vanilla JS; canvas or lightweight SVG).
4. Wire the overlay and timeline; load `smv_sample_input.json`.
5. Document usage in `docs/smv/README.md`.

## Dependencies
- None on VuDu. No centralized logs required.

## Validation & Review
- Self-test with 3 snapshots; screen-record behavior.
- Nova reviews `SMV_DESIGN_SPEC.md` and signs off.
- When complete, notify Nova via courier channel.
