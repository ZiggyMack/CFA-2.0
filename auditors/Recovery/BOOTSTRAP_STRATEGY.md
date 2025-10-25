# Bootstrap Strategy

**Purpose:** Define the hybrid approach for maintaining auditor bootstrap files — balancing stability with evolution

**Version:** 2.0  
**Last Updated:** 2025-10-25  
**Status:** Active Strategy

---

## 🎯 The Core Question

As the CFA project evolves, auditor context files accumulate lessons. We need a strategy:

**Option A: Lock + Append**
- Keep stable structure
- Add "Lessons Learned" section that grows
- Risk: Files become bloated, context diluted

**Option B: Wipe + Reimagine**
- Periodically rebuild from scratch
- Keep only the sharpest insights
- Risk: Lose valuable history

**Our Answer: HYBRID APPROACH**

---

## 🔄 Three-Phase Strategy

### **Phase 1: Locked Envelope (Stable Foundation)**

**What Stays Locked:**
- Core ethos ("All Named, All Priced")
- Audit journey (Level 0-5)
- Role definitions (Claude/Grok/Nova)
- 98% convergence story
- Red-flag glossary (Nova's list)

**Why Lock These:**
- They define the project's identity
- They achieved 98% convergence
- They're proven stable

**Files:**
- `BOOTSTRAP_FRAMEWORK.md` — Core structure (rarely changes)
- `BOOTSTRAP_CLAUDE` — Claude's identity (append zone only)
- `BOOTSTRAP_GROK` — Grok's identity (append zone only)
- `BOOTSTRAP_NOVA` — Nova's identity (append zone only)

---

### **Phase 2: Append Zone (Learning Edge)**

Each auditor bootstrap file has a **LESSONS LEARNED** section at the bottom:

```python
# ==============================================================================
# LESSONS LEARNED (v3.0 → v4.0)
# ==============================================================================

LESSONS = {
    "v3.0_davinci_pass": {
        "date": "October 2025",
        "lesson": "YPA tooltip above tabs works - users grasp efficiency immediately",
        "source": "User feedback + analytics",
        "action": "Keep this pattern for future explanations"
    },
    
    "v3.1_skeptic_mode": {
        "date": "November 2025",
        "lesson": "Skeptic Mode increased naturalist engagement by 40%",
        "source": "Usage metrics",
        "action": "Consider additional preset modes for other user personas"
    }
}
```

**Append Triggers:**
- New preset modes discovered
- User feedback patterns
- Toggle effectiveness data
- New bias patterns detected
- Cross-model coordination insights

**Append Limit:** Max 10 lessons per version cycle

**Duration:** Minor versions (v3.0 → v3.1 → v3.2 → v3.9)

---

### **Phase 3: Reimagine Checkpoint (Major Versions)**

**When to Wipe + Rebuild:**

Every **MAJOR version** (v3.x → v4.0), we:

1. **Audit the Append Zone:**
   - Which lessons are still relevant?
   - Which are superseded by better insights?
   - Which should graduate to "Locked Envelope"?

2. **Rebuild Bootstrap Files:**
   - Keep locked envelope (core structure)
   - Integrate proven lessons into main content
   - Archive old versions in `/auditor/archives/v3.0/`
   - Start fresh append zone

3. **Document the Rebuild:**
   - Update `BOOTSTRAP_CHANGELOG.md`
   - Show what changed and why
   - Preserve reasoning for future audits

---

## 🛡️ Governance Rules

### **Rule 1: Core Ethos is Immutable**
"All Named, All Priced" never changes.  
The audit journey (98% convergence story) never changes.  
These define the project.

### **Rule 2: Lessons Append During Minor Versions**
v3.0 → v3.1 → v3.2 = APPEND lessons learned  
Keep envelope stable, grow append zone

### **Rule 3: Major Versions Trigger Rebuild**
v3.x → v4.0 = REIMAGINE  
Audit append zone, integrate best lessons, archive rest

### **Rule 4: Always Create Archives**
Never delete history - move to `/auditor/archives/v3.0/`  
Future auditors can study evolution

---

## 📋 Maintenance Checklist

### **Monthly (Minor Updates):**
- [ ] Review user feedback
- [ ] Check for new bias patterns
- [ ] Add 1-2 lessons to append zone if needed
- [ ] Keep append zone under 10 lessons

### **Quarterly (Version Bumps):**
- [ ] Audit append zone for relevance
- [ ] Consolidate duplicate lessons
- [ ] Update examples if patterns emerge

### **Yearly (Major Versions):**
- [ ] Full bootstrap rebuild
- [ ] Archive old version
- [ ] Integrate proven lessons into core
- [ ] Reset append zone
- [ ] Update BOOTSTRAP_CHANGELOG.md

---

## 🔍 Decision Tree: Append or Replace?

```
New insight discovered?
│
├─ Is it about CORE ETHOS? 
│  └─ YES → DO NOT APPEND (core is locked)
│  └─ NO → Continue
│
├─ Is it a PATTERN (3+ occurrences)?
│  └─ YES → APPEND to lessons learned
│  └─ NO → Document in project notes (not bootstrap)
│
├─ Does it CONTRADICT existing lesson?
│  └─ YES → Replace old lesson, document why
│  └─ NO → Append as new lesson
│
└─ Is append zone at 10 lessons?
   └─ YES → Trigger audit (consolidate or promote to core)
   └─ NO → Safe to append
```

---

## 📦 File Structure Over Time

### **v3.0 State (October 2025):**
```
/recovery/
├── BOOTSTRAP_FRAMEWORK.md         (locked envelope)
├── BOOTSTRAP_CLAUDE               (locked + empty append zone)
├── BOOTSTRAP_GROK                 (locked + empty append zone)
├── BOOTSTRAP_NOVA                 (locked + empty append zone)
├── BOOTSTRAP_MAINTENANCE_GUIDE.md (governance rules)
└── RECOVERY_PROCESS.md            (recovery workflow)
```

### **v3.5 State (6 months later):**
```
/recovery/
├── BOOTSTRAP_FRAMEWORK.md         (locked envelope)
├── BOOTSTRAP_CLAUDE               (locked + 5 lessons appended)
├── BOOTSTRAP_GROK                 (locked + 4 lessons appended)
├── BOOTSTRAP_NOVA                 (locked + 3 lessons appended)
├── BOOTSTRAP_MAINTENANCE_GUIDE.md (updated with v3.5 notes)
└── RECOVERY_PROCESS.md            (updated workflow)
```

### **v4.0 State (1 year later - REIMAGINE):**
```
/recovery/
├── BOOTSTRAP_FRAMEWORK.md         (rebuilt - best v3.x lessons integrated)
├── BOOTSTRAP_CLAUDE               (rebuilt - proven lessons in core, fresh append zone)
├── BOOTSTRAP_GROK                 (rebuilt - proven lessons in core, fresh append zone)
├── BOOTSTRAP_NOVA                 (rebuilt - proven lessons in core, fresh append zone)
├── BOOTSTRAP_MAINTENANCE_GUIDE.md (updated)
├── BOOTSTRAP_CHANGELOG.md         (NEW - documents v3→v4 changes)
└── RECOVERY_PROCESS.md            (updated)

/auditor/archives/
└── v3.0/
    ├── BOOTSTRAP_CLAUDE_v3.5      (archived with full append history)
    ├── BOOTSTRAP_GROK_v3.5
    └── BOOTSTRAP_NOVA_v3.5
```

---

## 🎯 Example: Lesson Append (v3.0 → v3.1)

**Scenario:** User testing reveals YPA tooltip is TOO technical

**Action:**
```python
# In BOOTSTRAP_CLAUDE - LESSONS LEARNED section

LESSONS = {
    "v3.1_ypa_tooltip_revision": {
        "date": "November 2025",
        "issue": "Users confused by 'Efficiency score = Total Lever Score ÷ BFI'",
        "fix": "Changed to: 'Higher YPA = framework does more with fewer assumptions'",
        "metric": "User comprehension increased 35% (A/B test)",
        "action": "Update MUST_DO list - prioritize plain language over equations",
        "status": "Integrated into v3.1"
    }
}
```

**Result:** Lesson appended, not core rebuilt

---

## 🎯 Example: Major Rebuild (v3.5 → v4.0)

**Scenario:** After 10 lessons accumulated, time to rebuild

**Process:**

1. **Audit Append Zone:**
   - 5 lessons about tooltip clarity
   - 3 lessons about preset modes
   - 2 lessons about toggle explanations

2. **Consolidate:**
   - Tooltip lessons → Upgrade "MUST_DO" section to emphasize plain language
   - Preset lessons → Add "PRESET_DESIGN_PRINCIPLES" section
   - Toggle lessons → Already covered, archive

3. **Rebuild:**
   - Create new BOOTSTRAP_CLAUDE_v4.0 with consolidated lessons
   - Archive BOOTSTRAP_CLAUDE_v3.5 to `/archives/v3.0/`
   - Reset append zone to empty

4. **Document:**
   - Add entry to BOOTSTRAP_CHANGELOG.md explaining changes

---

## 🔥 The Philosophy

**Locked Envelope = The Foundation**
- Core ethos that made 98% convergence possible
- Never changes unless catastrophic flaw discovered
- Defines project identity

**Append Zone = The Learning Edge**
- Where we capture new insights during execution
- Grows organically with real-world usage
- Keeps cutting edge sharp

**Periodic Rebuild = The Sharpening**
- Prevents bloat from endless appending
- Integrates proven lessons into core
- Preserves history through archives
- Reimagines for next evolution

---

## ⚖️ Pointing Rule for Bootstrap System

*"To append your lesson is to pay the fee of documentation.  
To ignore patterns is to summon Mr. Brute twice.  
To rebuild without archiving is to deny history."*

Every lesson must be:
- **Named** (what changed)
- **Priced** (what it cost/gained)
- **Sourced** (why we believe it)

---

## 📝 Version History

| Version | Date | Changes | Author |
|:--------|:-----|:--------|:-------|
| 1.0 | 2025-10-24 | Initial strategy document | Claude |
| 2.0 | 2025-10-25 | Updated naming conventions, removed outdated message context, clarified examples | Claude |

---

**This hybrid approach keeps the cutting edge sharp while preserving the stable foundation that made 98% convergence possible.**

**This is the way.** 🔥
