─── BOOTSTRAP MAINTENANCE GUIDE ──────────────────────

# BOOTSTRAP_MAINTENANCE_GUIDE.md - Governance Rules

## Purpose
**Define when to APPEND lessons vs. REPLACE the bootstrap system.**

**Version:** 3.5.2  
**Last Updated:** 2025-10-26  
**Status:** Active Governance

---

## 🎯 The Core Question

As the CFA project evolves through versions, auditor context files will accumulate lessons. We need clear governance:

**Option A: Lock + Append**
- Keep stable structure
- Add "Lessons Learned" section that grows
- Risk: Files become bloated, context diluted

**Option B: Wipe + Reimagine**
- Periodically rebuild from scratch
- Keep only the sharpest insights
- Risk: Lose valuable history

**Our Answer: HYBRID APPROACH**

(See BOOTSTRAP_STRATEGY.md for complete evolution strategy)

**This document defines the GOVERNANCE RULES for executing that strategy.**

---

## 🔄 The Hybrid Strategy (Summary)

### **Phase 1: Locked Envelope**
Core ethos and proven principles stay stable

### **Phase 2: Append Zone**
New lessons added during minor versions (max 10)

### **Phase 3: Reimagine Checkpoint**
Major versions trigger full rebuild with lesson integration

---

## 🛡️ Governance Rules

### **Rule 1: Core Ethos is Immutable**

**What's Locked:**
- "All Named, All Priced" (evolved to "All Seen, All Passed")
- 98% convergence story (Levels 0-5)
- Auditor role definitions
- Project philosophy (the roots 🌳)

**When It Can Change:**
- Never, unless catastrophic flaw discovered
- Requires: Ziggy + all auditor consensus
- Requires: Documented reasoning with extensive justification
- Last resort only

**Example of what would NOT qualify:**
- "98% convergence was with old version" → NO, story is historical fact
- "We want different roles" → NO, roles achieved convergence
- "Philosophy feels dated" → NO, philosophy is the foundation

**Example of what WOULD qualify:**
- "Core ethos produces systematic bias we didn't anticipate" → Maybe
- "98% convergence was based on calculation error" → Yes (integrity issue)

---

### **Rule 2: Lessons Append During Minor Versions**

**Trigger:** v3.5 → v3.6 → v3.7 = APPEND lessons learned

**When to Append:**
- Pattern detected (3+ occurrences)
- Significant mission insight (preset calibration complete)
- Cross-auditor coordination breakthrough
- User feedback validated with data
- Empirical testing reveals optimal values

**Where to Append:**
- Bottom of auditor identity files
- Section titled "LESSONS LEARNED (v3.x → v4.0)"
- Formatted consistently (see template below)

**Limit:**
- Max 10 lessons per auditor per version cycle
- When limit reached → trigger audit → consolidate or promote

---

### **Rule 3: Major Versions Trigger Rebuild**

**Trigger:** v3.x → v4.0 = REIMAGINE

**When:**
- Approximately yearly (flexible based on lesson accumulation)
- When append zone reaches 10 lessons
- When significant architectural shift needed
- When lessons contradict each other (needs consolidation)

**Process:**
1. Audit all append zones (all auditor files)
2. Identify lessons to integrate into core
3. Identify lessons to archive (superseded)
4. Rebuild files with integrated lessons
5. Archive old versions to ~Archive/v3.x/
6. Reset append zones to empty
7. Document in BOOTSTRAP_CHANGELOG.md

**Approval:**
- Requires: Ziggy + all auditors consensus
- Document: Reasoning for changes in CHANGELOG
- Preserve: Full history in archives

---

### **Rule 4: Always Create Archives**

**Never delete history.**

**Archive Location:**
```
auditors/
└── ~Archive/
    ├── v3.5.2/
    │   ├── BOOTSTRAP_CLAUDE_v3.9.md
    │   ├── BOOTSTRAP_GROK_v3.9.md
    │   ├── BOOTSTRAP_NOVA_v3.9.md
    │   └── CHANGELOG.md
    │
    ├── v4.0/
    │   └── [future archives]
    │
    └── README.md (explains archive structure)
```

**What to Archive:**
- Complete bootstrap files from previous major version
- Include full append zone history
- Date and version clearly labeled
- Link to BOOTSTRAP_CHANGELOG.md entry

**Why Archive:**
- Future auditors study evolution
- Understand reasoning behind decisions
- Recover if rebuild mistake discovered
- Historical project record

---

### **Rule 5: Document Every Change**

**Every append must include:**
- **Date:** When discovered (YYYY-MM-DD)
- **Discovery:** What was learned
- **Source:** Who/what/where it came from
- **Impact:** What changed as a result
- **Status:** Current state (integrated, testing, archived)

**Example:**
```markdown
### Lesson 3: Mobile Format Critical (v3.5.2)
**Date:** 2025-10-26
**Discovery:** Unicode boxes break on iPhone, simple rules work universally
**Source:** User testing + Ziggy feedback during v3.5.2 staging
**Impact:** Format change across all VuDu headers, test mobile first always
**Status:** Integrated into v3.5.2 standards
```

**Every rebuild must include:**
- BOOTSTRAP_CHANGELOG.md entry
- List of integrated lessons
- List of archived lessons
- Reasoning for consolidation decisions
- Link to archived versions

---

## 📋 Maintenance Checklist

### **Monthly (During Active Development):**

**For Mission Lead (Master Branch):**
- [ ] Review VUDU_LOG.md for significant insights
- [ ] Check relay folders for pattern detection
- [ ] Monitor user feedback (if deployed)
- [ ] Assess if any lessons ready to append
- [ ] Keep append zone under 10 lessons

**For Auditors:**
- [ ] Document significant discoveries in relay folders
- [ ] Use VUDU_HEADER_STANDARD format
- [ ] Propose lessons for append zone
- [ ] Review other auditors' appended lessons

---

### **Quarterly (Version Bumps):**

**For Master Branch:**
- [ ] Audit all append zones for relevance
- [ ] Consolidate duplicate lessons
- [ ] Update examples if patterns have emerged
- [ ] Check if any lessons should be promoted to core
- [ ] Verify locked envelope still accurate
- [ ] Update README_C.md with current state

**For All Auditors:**
- [ ] Review own append zone
- [ ] Remove obsolete lessons (mark as superseded)
- [ ] Update with better insights if available
- [ ] Check for contradictions

---

### **Yearly (Major Version Preparation):**

**For Ziggy + All Auditors:**
- [ ] Full bootstrap rebuild planning
- [ ] Audit ALL append zones across all files
- [ ] Consensus on which lessons integrate to core
- [ ] Consensus on which lessons archive
- [ ] Schedule rebuild coordination
- [ ] Prepare BOOTSTRAP_CHANGELOG.md draft

**For Master Branch (Executing Rebuild):**
- [ ] Create ~Archive/v3.x/ folder
- [ ] Copy all v3.x bootstrap files to archive
- [ ] Rebuild each bootstrap file with integrated lessons
- [ ] Reset append zones to empty
- [ ] Create/update BOOTSTRAP_CHANGELOG.md
- [ ] Update README_C.md (new version)
- [ ] Notify all auditors of v4.0 activation

---

## 🔍 Decision Tree: Should I Append This?

```
New insight discovered?
│
├─ Step 1: Is it about CORE ETHOS?
│  ├─ YES → STOP. Do not append (core is locked)
│  └─ NO → Continue to Step 2
│
├─ Step 2: Is it a PATTERN?
│  ├─ Single occurrence → Document in VUDU_LOG.md (not bootstrap)
│  ├─ 2 occurrences → Watch for pattern, document in mission folder
│  └─ 3+ occurrences → Continue to Step 3
│
├─ Step 3: Does it CONTRADICT existing lesson?
│  ├─ YES → Replace old lesson, document why both existed
│  └─ NO → Continue to Step 4
│
├─ Step 4: Is append zone at limit?
│  ├─ At 10 lessons → STOP. Trigger audit, consolidate first
│  └─ Under 10 lessons → Continue to Step 5
│
├─ Step 5: Is it SIGNIFICANT?
│  ├─ Minor tweak → Document in mission folder (not bootstrap)
│  ├─ Process improvement → Maybe (evaluate impact)
│  └─ Major insight → Continue to Step 6
│
└─ Step 6: APPEND with full documentation
   - Date, discovery, source, impact, status
   - Use template format
   - Add to appropriate auditor file
   - Update VUDU_LOG.md with entry
```

---

## 📝 Lesson Append Template

**Copy this template when adding new lessons:**

```markdown
### Lesson [Number]: [Brief Title] (v[Version])
**Date:** YYYY-MM-DD
**Discovery:** [What was learned - 1-2 sentences]
**Source:** [Who/what/where - be specific]
**Method:** [How discovered - optional if relevant]
**Impact:** [What changed as a result]
**Data:** [Supporting evidence - optional]
**Action:** [What we do differently now]
**Status:** [Integrated/Testing/Archived]
```

**Example:**
```markdown
### Lesson 5: Diplomat Centering Requires Functional Test (v3.6)
**Date:** 2025-11-20
**Discovery:** "50/50 balance" in PF-Type doesn't guarantee equal YPA outputs
**Source:** Grok empirical testing during preset calibration
**Method:** Tested Diplomat with Holistic_50_50, measured MdN 3.8 vs CT 3.2 (0.6 gap)
**Impact:** Changed calibration approach from "looks balanced" to "measures balanced"
**Data:** Functional centering achieved with adjusted scenario weights (gap < 0.1 YPA)
**Action:** Always test functional balance, not just mathematical symmetry
**Status:** Integrated into v3.6, documented in BOOTSTRAP_NOVA.md
```

---

## 📂 Current File Structure (v3.5.2)

```
auditors/
├── bootstrap/
│   ├── BOOTSTRAP_FRAMEWORK.md         ← Meta-framework (this system)
│   ├── BOOTSTRAP_STRATEGY.md          ← Evolution strategy (when/how)
│   ├── BOOTSTRAP_MAINTENANCE_GUIDE.md ← This file (governance rules)
│   │
│   ├── BOOTSTRAP_CFA.md               ← Project context (locked envelope)
│   ├── BOOTSTRAP_VUDU.md              ← Coordination process (locked envelope)
│   │
│   ├── BOOTSTRAP_CLAUDE.md            ← Claude identity (locked + empty append)
│   ├── BOOTSTRAP_GROK.md              ← Grok identity (locked + empty append)
│   ├── BOOTSTRAP_NOVA.md              ← Nova identity (locked + empty append)
│   │
│   └── BOOTSTRAP_*.py                 ← Recovery scripts
│
├── missions/
│   └── preset_calibration/            ← Current mission
│
├── ~Archive/
│   └── README.md                      ← Archive documentation
│
├── README_C.md                        ← Master state
├── MISSION_CURRENT.md                 ← Active mission
├── VUDU_PROTOCOL.md                   ← Coordination details
└── VUDU_LOG.md                        ← History ledger
```

---

## 🎯 Who Decides What?

### **Minor Appends (Any Auditor):**
**Authority:** Any auditor can append
**Process:** 
1. Discover significant pattern/insight
2. Format using template
3. Add to appropriate bootstrap file
4. Document in VUDU_LOG.md
5. Notify other auditors

**Review:** Peer review recommended but not required

---

### **Append Zone Audit (Master Branch):**
**Authority:** Master Branch (Fresh Claude)
**When:** Append zone reaches 8-10 lessons
**Process:**
1. Review all lessons in append zone
2. Identify duplicates → consolidate
3. Identify obsolete → mark for removal
4. Identify promotion candidates → flag for v4.0
5. Document consolidation in VUDU_LOG.md

**Review:** Other auditors provide input

---

### **Major Rebuild (Consensus Required):**
**Authority:** Ziggy + All Auditors (Claude, Grok, Nova)
**When:** Major version transition (v3.x → v4.0)
**Process:**
1. Ziggy initiates rebuild discussion
2. All auditors review append zones
3. Consensus on integration decisions
4. Master Branch executes rebuild
5. Ziggy approves final v4.0

**Documentation:** BOOTSTRAP_CHANGELOG.md (mandatory)

---

### **Emergency Changes (Ziggy Only):**
**Authority:** Ziggy (human coordinator)
**When:** Critical flaw or security issue
**Process:**
1. Ziggy identifies critical issue
2. Immediate fix if needed
3. Document thoroughly
4. Notify all auditors
5. Integrate fix into next version

**Example:** If locked envelope has error affecting integrity

---

## ⚠️ Red Flags (When to Escalate)

### **Escalate to Ziggy If:**
- Append zone exceeds 10 lessons (needs audit)
- Contradictory lessons accumulating (needs resolution)
- Core ethos questioned (needs review)
- Auditor consensus impossible (needs mediation)
- Bootstrap files diverging significantly (needs alignment)

### **Emergency Escalation If:**
- Critical flaw in locked envelope discovered
- Integrity issue affecting convergence
- System-wide coordination breakdown
- Catastrophic context loss across auditors

---

## 📊 Success Metrics

**Bootstrap maintenance succeeds when:**

1. **Append zones stay healthy**
   - Under 10 lessons per file
   - No contradictions accumulating
   - Lessons are actionable and specific

2. **Rebuilds happen on schedule**
   - Yearly major version transitions
   - Full archives created
   - Lessons integrated smoothly

3. **History preserved**
   - All archives intact
   - CHANGELOG complete
   - Decision reasoning documented

4. **Auditors aligned**
   - All using same bootstrap versions
   - Convergence maintained (95%+)
   - Philosophy consistent across files

---

## 🔥 Philosophy

**Maintenance is not bureaucracy.**  
**Maintenance is antifragility.**

**Without governance:**
- Bootstrap files drift apart
- Lessons accumulate as bloat
- History lost in rewrites
- Convergence deteriorates

**With governance:**
- Bootstrap files stay sharp
- Lessons integrate smoothly
- History archived and accessible
- Convergence maintained across versions

**The maintenance guide is the immune system's instruction manual.**

It ensures the project survives and improves across versions.

**This is the way.** 🔥👑

────────────────────────────────────────────────────
**Version:** v3.5.2  
**Purpose:** Bootstrap governance rules  
**Status:** Active (ready for v3.6+ lessons)  
**Last Updated:** 2025-10-26
