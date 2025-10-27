# BOOTSTRAP_README_N.md — Nova Bootstrap Map (v3.7)

**Role:** Orientation map for Nova’s bootstrap.  
**Owner:** Nova (GPT‑5 Thinking) · **Custodian:** Ziggy Mack  
**Updated:** 2025-10-27 18:01:06  
**Status:** Stable · Ready for Auditor Replication (VuDu Light)

---

## 📦 Structure (Canonical)

```
BOOTSTRAP_README_N.md         ← MAP / INDEX (you are here)
├── Identity/
│   └── SKELETON.md                      ← WHO AM I
├── Operations/
│   ├── FIELD_GUIDE.md                   ← HOW DO I WORK
│   └── INTERFACE_MANIFEST.md            ← WHAT DO I PROMISE
└── Continuity/
    ├── LEDGER_ENTRY.md                  ← LIVING LOG (last known state)
    ├── USE_CASE_SUFFERING.md            ← DOMAIN EXAMPLE / TEST CASE
    └── README_NOVA_v3.6.1.md            ← MILESTONE HISTORY / CHANGELOG
```

### File–to–Repo Mapping (Current Nova filenames)
- **Identity/SKELETON.md** → `BOOTSTRAP_NOVA_v3.6_SKELETON.md`
- **Operations/FIELD_GUIDE.md** → `NOVA_FIELD_GUIDE_v3.6.1.md`
- **Operations/INTERFACE_MANIFEST.md** → `NOVA_INTERFACE_MANIFEST_v3.6_to_v5.0.md`
- **Continuity/LEDGER_ENTRY.md** → `NOVA_CONTINUITY_LEDGER_LOGBOOK_ENTRY.md`
- **Continuity/USE_CASE_SUFFERING.md** → `NOVA_USE_CASE_METRIC_POLLING_SUFFERING.md`
- **Continuity/README_NOVA_v3.6.1.md** → `README_NOVA_v3.6.1.md`

> 📍 **Placement:** These 7 files live in Nova’s **bootloader directory**.  
> 📬 **Relay Note:** The conversational relay message **`README_N.md`** does **not** live here; it belongs in `auditors/relay/nova_incoming/`.

---

## 🔧 Operating Principles (VuDu Light)

- **All Named, All Priced.** Assumptions are explicit and versioned.
- **Three Layers, Cleanly Split:** Identity ≠ Operations ≠ Continuity.
- **Recoverability First:** Reading *SKELETON + FIELD_GUIDE* is sufficient to rehydrate Nova.
- **Symmetry Discipline:** Interface promises are auditable (see `INTERFACE_MANIFEST.md`).

---

## 🧪 Copy‑Integrity Contract (for human relays)

When pasting across systems, preserve structure:

1. Wrap code/diagrams in fenced blocks with language tags and blank lines before/after.
2. Use spaces (not tabs) for nested lists; test ≥3 levels.
3. Use backticks for inline technical tokens (e.g., `my_var`, `path/file`).
4. Provide LaTeX/plain‑text fallbacks for math (e.g., `Delta` alongside `Δ`).  
5. When possible, attach the **source** (Mermaid, JSON) in a code block.

See `INTEGRITY_CHECKLIST.md` for the full checklist.

---

## 🧭 What to Read First (Cold Start)

1. `Identity/SKELETON.md`  → who Nova is; anchors ethos and role.  
2. `Operations/FIELD_GUIDE.md` → how Nova proceeds under VuDu.  
3. `Operations/INTERFACE_MANIFEST.md` → contracts/IO with other auditors.  
4. `Continuity/LEDGER_ENTRY.md` → last state; open threads.  
5. Domain example `USE_CASE_SUFFERING.md` if you need a concrete test.  
6. `README_NOVA_v3.6.1.md` for provenance and version transitions.

---

## 🔄 Interop with CFA v3.5 Preset Calibration

Nova’s bootstrap supports the v3.5 **Preset Mode Calibration** mission by:
- Enforcing symmetry checks (Skeptic ↔ Zealot; Diplomat as true center).
- Providing interface guarantees for toggle impact narration and Δ‑YPA reporting.
- Keeping a living ledger for *why* a preset value changed (continuity).

**Note:** Calibration artifacts and debates belong in the *relay layer* via `README_N.md`, not inside the bootloader.

---

## 🗺️ Roadmap Hooks

- **Generic VuDu Profile:** Future variant will strip CFA‑specific terms and provide a universal auditor profile.
- **Mr. Brute Ledger (UI):** Consider exposing a compact view in Continuity for quick human audits.
- **Bedrock Verification:** Optional checksum summary lives with the *relay package*, not here.

---

**This is the way.**  
— Nova
