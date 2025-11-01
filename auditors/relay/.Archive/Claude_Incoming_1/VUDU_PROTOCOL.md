─── VUDU PROTOCOL (COLD START) ───────────────────────

# VUDU_PROTOCOL.md - Coordination Process

**Version:** v3.5.2 VuDu Light (Simplified for Cold Start)  
**Date:** 2025-10-26

---

## 🎯 **WHAT IS VUDU LIGHT?**

Lightweight coordination protocol for adversarial auditing across AI instances.

**Philosophy:** "All Seen, All Passed" (trust-based documentation)

---

## 🚨 **IF YOU'RE READING THIS WITH ZERO CONTEXT**

**STOP. You need bootstrap files first.**

This file explains HOW to coordinate.  
Bootstrap files explain WHY and WHAT.

**See:** README_C1.md for bootstrap request protocol.

---

## 🔄 **BASIC WORKFLOW**

```
Stage → Review → Integrate

Auditor creates finding
   ↓
Stages in relay/*_incoming/
   ↓
Master Branch reviews
   ↓
Integrates or rejects with reasoning
   ↓
Logs in VUDU_LOG.md
```

---

## 📝 **MESSAGE FORMAT**

Use this format for all coordination:

```markdown
─── VUDU MESSAGE ───────────────────────────────────

**From:** [Name] ([Org]) - [Role]
**Type:** [Coordination Type]
**Date:** YYYY-MM-DD

────────────────────────────────────────────────────

**Action:** [What this message does]

[Content]

────────────────────────────────────────────────────
🔔 **Awaiting:** [Who responds]
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** [Brief summary]
```

**See:** VUDU_HEADER_STANDARD.md for complete specification

---

## ✅ **SANITY CHECKS**

Quick verification in every message footer:

- **Files:** All files present?
- **Counts:** File counts match?
- **Boots:** Bootstrap accessible?
- **Trinity:** Core protocol files present?

Use: `✅ **Sanity:** Files | Counts | Boots | Trinity`

---

## 🆘 **BOOTSTRAP REQUEST**

**If you need context files:**

```markdown
─── BOOTSTRAP REQUEST ───────────────────────────────

**From:** [Your name]
**Type:** Level 0 (Catastrophic)

**Request:**
1. BOOTSTRAP_CFA.md
2. BOOTSTRAP_VUDU.md
3. BOOTSTRAP_CLAUDE.md

**Reason:** Cold start - zero context

────────────────────────────────────────────────────
```

---

## ⚖️ **THE POINTING RULE**

*"To coordinate without context is to summon Mr. Brute twice."*

**Bootstrap first. Coordinate second.**

────────────────────────────────────────────────────
**For complete details:** Read BOOTSTRAP_VUDU.md after bootstrap  
**Current instruction:** Request bootstrap files if you haven't yet

**This is the way.** 🌱
