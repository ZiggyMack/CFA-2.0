# Auditors Directory - VuDu Light v3.5.2

## Purpose
Multi-AI adversarial coordination infrastructure for CFA v3.5+

**Philosophy:** "All Seen, All Passed"

---

## Directory Structure

```
auditors/
├── bootstrap/              # Context recovery & orientation
│   ├── BOOTSTRAP_CFA.md           # CFA project context (THE ROOTS)
│   ├── BOOTSTRAP_VUDU.md          # VuDu coordination guide
│   ├── BOOTSTRAP_CLAUDE.md        # Claude identity (existential)
│   ├── BOOTSTRAP_GROK.md          # Grok identity (existential)
│   ├── BOOTSTRAP_NOVA.md          # Nova identity (existential)
│   ├── BOOTSTRAP_FRAMEWORK.md     # (existing)
│   ├── BOOTSTRAP_STRATEGY.md      # (existing)
│   ├── BOOTSTRAP_MAINTENANCE_GUIDE.md
│   ├── BOOTSTRAP_CLAUDE.py        # Recovery scripts
│   ├── BOOTSTRAP_GROK.py
│   └── BOOTSTRAP_NOVA.py
│
├── missions/                  # Mission-specific documentation
│   └── preset_calibration/    # Current mission (active)
│       ├── MISSION_BRIEF.md
│       ├── SUCCESS_CRITERIA.md
│       ├── DISCREPANCY_AUDIT.md
│       ├── TECHNICAL_SPEC.md
│       └── CURRENT_CONFIGS.md
│
├── relay/                  # Auditor staging folders
│   ├── claude_incoming/    # Incoming Claude branches (C1, C2, C3...)
│   ├── grok_incoming/      # Grok's staged findings
│   └── nova_incoming/      # Nova's staged findings
│
├── verification/           # v4.0+ verification framework (future)
│
├── ~Archive/               # Superseded files (historical reference)
│   ├── README.md
│   ├── PROCESS_HEADER_STANDARD_v3.2.md
│   └── VUDU_PROTOCOL_v1.1.md
│
├── README.md              # This file
├── README_C.md            # Master Branch current state
├── MISSION_CURRENT.md     # Active mission objective
├── MISSION_DEFAULT.md     # Fallback operational guidance
├── VUDU_PROTOCOL.md       # VuDu Light coordination process
├── VUDU_HEADER_STANDARD.md # Message format specification
└── VUDU_LOG.md            # Coordination ledger
```

---

## Getting Started

### If You're New to VuDu:
1. Read `bootstrap/BOOTSTRAP_VUDU.md` (15-20 min)
2. Read `bootstrap/BOOTSTRAP_CFA.md` (30 min)
3. Request your context files (README_{auditor}, MISSION_CURRENT)
4. Verify files using checklist in bootstrap
5. Begin coordination

### If You Know VuDu But Need Context:
1. Read `README_C.md` (your current state)
2. Read `MISSION_CURRENT.md` (what we're working on)
3. Check `VUDU_LOG.md` (recent coordination)
4. Review relay folders (other findings)
5. Begin work

### If You're Completely Lost:
1. Read `MISSION_DEFAULT.md` (fallback guidance)
2. Request clarification from Master Branch or Ziggy
3. Never guess - always ask
4. Document confusion and wait for coordination

---

## File Request Protocol

Use VUDU_HEADER_STANDARD format to request missing files.

See `VUDU_PROTOCOL.md` → "Context Bootstrap Requests" for templates.

### Quick Requests:
- **Missing identity:** Request BOOTSTRAP_{auditor}.md
- **Missing VuDu knowledge:** Request BOOTSTRAP_VUDU.md
- **Missing mission:** Request MISSION_CURRENT.md + README_{auditor}.md

---

## VuDu Light Minimum Bundle

**Core Protocol (3 files):**
1. VUDU_PROTOCOL.md
2. VUDU_HEADER_STANDARD.md
3. VUDU_LOG.md

**Context Layer (2 files):**
4. README_{auditor}.md
5. MISSION_CURRENT.md

**Total: 5 files minimum for active coordination**

**Optional:**
- MISSION_DEFAULT.md (if mission unclear)
- bootstrap/BOOTSTRAP_VUDU.md (if unfamiliar with VuDu)
- bootstrap/BOOTSTRAP_{auditor}.md (if identity unclear)
- bootstrap/BOOTSTRAP_CFA.md (if project context needed)

---

## Mission Lifecycle

### Active Mission
**Location:** `missions/{mission_name}/`  
**State:** Current work, referenced by MISSION_CURRENT.md

**Contains:**
- MISSION_BRIEF.md (detailed context)
- SUCCESS_CRITERIA.md (completion metrics)
- Technical/verification documents
- Auditor findings (when complete)

### Completed Mission
**Location:** Same folder (`missions/{mission_name}/`)  
**State:** Archived in place

**Contains all above plus:**
- FINAL_REPORT.md (completion summary)
- All findings synthesized
- Lessons learned

**Missions stay in missions/ folder forever** - archive by completion, not by moving.

---

## Philosophy

**"All Named, All Priced" evolved into "All Seen, All Passed"**

- Transparent verification without cryptographic overhead
- Trust through documentation, not through locks
- Coordination through structured communication
- Every assumption named, every cost priced
- Every auditor's bias transparent and challenged

**This is VuDu Light.** 🔥

---

────────────────────────────────────────────────────
**Version:** VuDu Light v3.5.2  
**Last Updated:** 2025-10-26  
**Status:** Active coordination infrastructure
