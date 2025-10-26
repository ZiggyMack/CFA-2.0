─── VUDU PROTOCOL ───────────────────────────────────

# VUDU_PROTOCOL.md - VuDu Light Coordination Process

**Purpose:** Define how auditors coordinate across AI instances  
**Version:** v3.5.2 VuDu Light  
**Last Updated:** 2025-10-26  
**Philosophy:** "All Seen, All Passed" (trust-based documentation)

---

## 🎯 **WHAT IS VUDU LIGHT?**

**VuDu Light** is a lightweight coordination protocol enabling adversarial auditing across AI instances without cryptographic overhead.

**Philosophy Shift:**
- v3.5 (VuDu Full): "All Named, All Priced" (heavy verification)
- v3.5.2 (VuDu Light): "All Seen, All Passed" (trust-based documentation)

**Why Light?**
- v3.5 completed infrastructure build ("the cathedral")
- v3.6 focuses on calibration ("tuning the bells")
- Heavy cryptographic verification deferred to v4.0+
- Embedded sanity checks replace formal verification

---

## 🔄 **CORE WORKFLOW**

### **Stage → Review → Integrate**

```
Auditor → relay/*_incoming/ → Master Branch → README_C update → VUDU_LOG entry
         (creates finding)   (reviews)      (integrates)      (documents)
```

**Example:**
1. Grok tests Skeptic mode empirically
2. Grok stages findings in relay/grok_incoming/
3. Fresh Claude (Master Branch) reviews findings
4. If accepted: Updates README_C, logs in VUDU_LOG
5. If rejected: Documents why, suggests revision

---

## 📁 **RELAY FOLDER ARCHITECTURE**

```
auditors/relay/
├── claude_incoming/    # Fresh Claude branches stage here
├── grok_incoming/      # Grok stages findings here
└── nova_incoming/      # Nova stages findings here
```

**Naming Convention:** `[auditor]_[topic]_[date].md`

**Example:** `grok_skeptic_ypa_test_20251026.md`

---

## 📝 **MESSAGE FORMAT**

**All coordination uses VUDU_HEADER_STANDARD format:**

```markdown
─── VUDU MESSAGE ───────────────────────────────────

**From:** [Name] ([Org]) - [Role]
**Type:** [Coordination Type]
**Date:** YYYY-MM-DD

────────────────────────────────────────────────────

**Action:** [What this message does]

**Key Assumptions:**
1. [Named brute 1]
2. [Named brute 2]

**Status:** [Current state]

[Message content]

────────────────────────────────────────────────────
🔔 **Awaiting:** [Who responds]
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** [Brief log entry]
```

**See:** VUDU_HEADER_STANDARD.md for complete specification

---

## ✅ **SANITY CHAIN VERIFICATION**

**Four quick checks embedded in every message footer:**

### **Files** - All files present and intact?
Check key files exist and are accessible

### **Counts** - File counts match manifest?
- bootstrap/ = 11 files (8 .md + 3 .py)
- missions/preset_calibration/ = 5 files
- relay/ = 3 *_incoming/ folders

### **Boots** - Bootstrap files verified?
Can access BOOTSTRAP_CFA, BOOTSTRAP_VUDU, BOOTSTRAP_CLAUDE

### **Trinity** - Core protocol files present?
VUDU_PROTOCOL, VUDU_HEADER_STANDARD, VUDU_LOG accessible

### **Usage:**
```
✅ **Sanity:** Files | Counts | Boots | Trinity  (all pass)
⚠️ **Sanity:** Files | ❌ Counts | Boots | Trinity  (counts fail)
```

---

## 🆘 **CONTEXT BOOTSTRAP REQUESTS**

**If you lose context or need files:**

### **Level 0: Complete Loss (Catastrophic)**
**Request:** All bootstrap files + master state

**Protocol:**
```markdown
─── BOOTSTRAP REQUEST ───────────────────────────────

**From:** [Your name]
**Type:** Level 0 (Catastrophic)
**Need:** Complete context recovery

**Request:**
1. BOOTSTRAP_CFA.md (project roots)
2. BOOTSTRAP_VUDU.md (coordination process)
3. BOOTSTRAP_[your_auditor].md (your identity)
4. README_C.md (current state)
5. MISSION_CURRENT.md (active mission)

**Reason:** [Why context lost]

────────────────────────────────────────────────────
```

### **Level 1: Partial Loss**
**Request:** Specific bootstrap or mission files

### **Level 2: Clarification**
**Request:** Specific sections or recent history

**See:** BOOTSTRAP_VUDU.md for detailed recovery procedures

---

## 🎯 **MASTER BRANCH RESPONSIBILITIES**

**Fresh Claude (Master Branch) coordinates all work:**

1. **Review relay folders** for staged findings
2. **Evaluate findings** through teleological lens
3. **Accept or reject** with documented reasoning
4. **Update README_C.md** with integrated findings
5. **Log in VUDU_LOG.md** all coordination events
6. **Request clarification** if findings unclear

---

## 👥 **AUDITOR ROLES**

**Claude (Master Branch):**
- Coordinate all work
- Synthesize findings
- Update master state
- Apply teleological lens

**Grok (xAI):**
- Empirical testing
- YPA validation
- Usability enforcement
- Apply empirical lens

**Nova (OpenAI/Amazon):**
- Symmetry auditing
- Balance verification
- Fairness checks
- Apply symmetry lens

**Ziggy (Human):**
- Final decisions
- Manual relay (when needed)
- Process integrity
- Conflict resolution

---

## 📂 **FILE HIERARCHY**

**Always Current (Single Source of Truth):**
- README_C.md - Master state
- VUDU_LOG.md - Coordination history
- MISSION_CURRENT.md - Active mission

**Reference (Stable):**
- VUDU_PROTOCOL.md - This file
- VUDU_HEADER_STANDARD.md - Message format
- Bootstrap files - Context recovery

**Mission-Specific:**
- missions/[mission_name]/ - Current work
- relay/*_incoming/ - Staged findings

---

## ⚖️ **THE POINTING RULE**

*"To coordinate is to name your assumptions.  
To integrate is to price your decisions.  
To log is to respect those who follow."*

**Every finding must:**
- Name its assumptions
- Price its impact
- Document its reasoning

**This is VuDu Light.** 🔥

────────────────────────────────────────────────────
**Version:** v3.5.2 VuDu Light  
**For More:** See BOOTSTRAP_VUDU.md (complete coordination guide)  
**Last Updated:** 2025-10-26

**This is the way.** 👑
