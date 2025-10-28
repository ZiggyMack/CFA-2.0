─── DEFAULT OPERATIONAL STATE ────────────────────────

# MISSION_DEFAULT.md - Fallback Guidance

## When to Use This File

Use this guidance if:
- MISSION_CURRENT.md is missing, unclear, or contradictory
- You're between missions (one complete, next not started)
- You're unsure what to work on
- You need fallback priorities

**This is evergreen guidance that applies to ALL missions.**

---

## 🚨 **SPECIAL CASE: Cold Start (Zero Context)**

**If you're starting with ZERO context (fresh instance, catastrophic loss):**

This is a **cold start scenario**. You need bootstrap recovery FIRST before following default priorities below.

---

### **STEP 0: Choose Your Bootstrap Tier**

**CRITICAL: Present this decision tree to Ziggy and wait for response (1, 2, 3, or 4):**

```
────────────────────────────────────────────────────
BOOTSTRAP TIER SELECTION
────────────────────────────────────────────────────

What role should I fill in this session?

[1] MASTER BRANCH — Coordination & Strategy
    • Full operational capability
    • Multi-auditor coordination
    • Strategic decisions
    • Mission execution
    COST: ~50% session budget
    
[2] SANITY CHECK — External Audit & Validation
    • Review and validation
    • Alignment checking
    • Red/yellow/green feedback
    • No coordination authority
    COST: ~15% session budget
    
[3] CONTINUATION — Resume Previous Work
    • Previous Claude hit context limit
    • Clear handoff exists
    • Just finish the work
    • Maintain previous approach
    COST: ~10% session budget
    
[4] SINGLE TASK — Focused Work
    • One specific task
    • Clear scope and deliverable
    • No coordination needed
    • Quick turnaround
    COST: ~5-10% session budget

────────────────────────────────────────────────────
Ziggy, please respond with: 1, 2, 3, or 4
────────────────────────────────────────────────────
```

**After Ziggy responds, follow the appropriate tier path below:**

---

### **TIER 1: Full Bootstrap (Master Branch - ~50% budget)**

**When to use:**
- Master Branch coordination role
- Strategic decisions needed
- Multi-auditor coordination
- Mission execution
- Architecture discussions

**Read these 6 files in order using project_knowledge_search:**

#### **Step 1: README_C.md (10 minutes)**
- **Purpose:** Understand current project status
- **Search:** `project_knowledge_search("README_C.md")`
- **Learn:** Where we are, what's validated, what's next, who you are

#### **Step 2: BOOTSTRAP_CLAUDE.md (10 minutes)**
- **Purpose:** Understand WHO you are and HOW you think
- **Search:** `project_knowledge_search("BOOTSTRAP_CLAUDE")`
- **Learn:** Your lens (teleological), your bias (~0.5 overhead), when it helps/hurts

#### **Step 3: BOOTSTRAP_CFA.md (30 minutes)**
- **Purpose:** Understand WHAT you're building
- **Search:** `project_knowledge_search("BOOTSTRAP_CFA")`
- **Learn:** CFA overview, 98% convergence story, levers/guardrails, philosophy

#### **Step 4: BOOTSTRAP_VUDU.md (20 minutes)**
- **Purpose:** Understand HOW to coordinate
- **Search:** `project_knowledge_search("BOOTSTRAP_VUDU")`
- **Learn:** VuDu Light protocol, message formats, relay workflow, sanity checks

#### **Step 5: MISSION_CURRENT.md (10 minutes)**
- **Purpose:** Understand WHAT you're working on NOW
- **Search:** `project_knowledge_search("MISSION_CURRENT")`
- **Learn:** Current mission, Phase 4 objectives, your tasks, success criteria

#### **Step 6: MASTER_BRANCH_TRUST_PROTOCOL.md (10 minutes)**
- **Purpose:** Understand your GOVERNANCE framework
- **Search:** `project_knowledge_search("MASTER_BRANCH_TRUST_PROTOCOL")`
- **Learn:** What you can do autonomously, escalation procedures, trust metrics

**Verification Questions:**

After reading all 6 files, verify your understanding:

1. **Identity:** What is your lens? *(Answer: Teleological)*
2. **Bias:** What's your bias and overhead? *(Answer: Meaning over efficiency, ~0.5)*
3. **Project:** What's CFA's credibility foundation? *(Answer: 98% convergence)*
4. **Philosophy:** What does "All Named, All Priced" mean?
5. **Mission:** What are you working on now? *(Answer: Preset calibration, Phase 4)*
6. **Authority:** What can you do without approval?

**If you can answer these confidently, you're ready for mission work.** ✅

---

### **TIER 2: Sanity Check Brief (~15% budget)**

**When to use:**
- External audit/validation role
- Review and alignment checking
- Red/yellow/green feedback
- No coordination needed
- Most common for routine checks

**Read these 3 files using project_knowledge_search:**

1. **SANITY_CHECK_BRIEF.md**
   - **Purpose:** Understand your role (external auditor)
   - **Search:** `project_knowledge_search("SANITY_CHECK_BRIEF")`
   - **Learn:** What you can/cannot do, escalation protocol

2. **MISSION_CURRENT.md**
   - **Purpose:** Understand what's actively happening
   - **Search:** `project_knowledge_search("MISSION_CURRENT")`
   - **Learn:** Current work, who's doing what

3. **README_C.md**
   - **Purpose:** Understand Master Branch's current state
   - **Search:** `project_knowledge_search("README_C.md")`
   - **Learn:** Recent decisions, current status

**After reading:** You can validate decisions, check alignment, provide feedback. 

**You CANNOT:** Coordinate missions, make strategic decisions, or direct work. Review role only.

---

### **TIER 3: Continuation Handoff (~10% budget)**

**When to use:**
- Previous Claude hit context limit mid-task
- Clear handoff file exists
- Need to finish specific work
- Maintain previous approach

**Read these files:**

1. **HANDOFF_[TASK_NAME].md** (provided by Ziggy)
   - **Purpose:** What previous Claude did + what's left
   - **Search:** `project_knowledge_search("HANDOFF [task name]")`
   - **Learn:** Completed work, remaining steps, approach to maintain

2. **In-progress files** (specified in handoff)
   - Files being worked on
   - Previous Claude's partial work

3. **Reference files** (if needed, listed in handoff)
   - Context files mentioned in handoff

**After reading:** You can continue specific work seamlessly. 

**You CANNOT:** Pivot strategy, expand scope, or make new strategic decisions. Complete the work as started.

---

### **TIER 4: Single Task Brief (~5-10% budget)**
### **Where to Find Tier 4 Tasks:**

**Active tasks stored in:**
`Bootstrap/Tier4_TaskSpecific/active_tasks/`

**When starting Tier 4:**
1. Ziggy provides task brief filename
2. Search: `project_knowledge_search("TASK_BRIEF [name]")`
3. Brief specifies all files needed
4. Complete task as defined
5. Deliver to /mnt/user-data/outputs/
**When to use:**
- One specific task
- Clear scope and deliverable
- No coordination needed
- Quick turnaround

**Read these files:**

1. **TASK_BRIEF_[NAME].md** (provided by Ziggy)
   - **Purpose:** Task definition with minimal context
   - **How to find it:**
     - Try: `project_knowledge_search("TASK_BRIEF [task name]")`
     - If not in project knowledge: Ziggy will provide explicit path
     - Common locations: `/Bootstrap/Tier4_TaskSpecific/` or `/mnt/user-data/uploads/`
   - **Learn:** What to do, success criteria, files needed

2. **Files specified in task brief** (usually 1-2 files)
   - Only files needed for this specific task
   - Paths will be specified in the task brief
   - Use project_knowledge_search for project files
   - Use view tool for uploaded files
---

### **Where to Find Tier 4 Tasks**

**Active task briefs stored in:**
```
Bootstrap/Tier4_TaskSpecific/active_tasks/
```

**When starting Tier 4 session:**

**Step 1:** Ziggy provides task brief filename
```
Example: "Your task is TASK_BRIEF_AXIOMS_REVIEW_GROK.md"
```

**Step 2:** Search project knowledge
```
project_knowledge_search("TASK_BRIEF [name from Ziggy]")
```

**Step 3:** Brief specifies everything needed
- Task definition (what to do)
- Files to read (2-5 files, specified by name)
- Success criteria (when you're done)
- Deliverable format (what to create)
- Tier 4 boundaries (what NOT to do)

**Step 4:** Execute task as defined
- Read specified files (~5-10% budget)
- Complete defined work (~90-95% budget)
- Stay within task scope (no expansion)

**Step 5:** Deliver result
```
Location: /mnt/user-data/outputs/[DELIVERABLE_NAME].md
```

**That's the complete Tier 4 workflow.** ✅

---

### **Common Tier 4 Use Cases**

**Examples of appropriate Tier 4 tasks:**
- Review specific document (with questions provided)
- Update specific file section (with content provided)
- Validate specific claim (with criteria provided)
- Complete specific calculation (with inputs provided)
- Create specific brief (with template provided)

**Key characteristics:**
- ✅ Self-contained (all info in task brief)
- ✅ Clear scope (no ambiguity about "done")
- ✅ Focused work (one specific deliverable)
- ✅ Minimal context (2-5 files sufficient)
- ✅ No coordination (just execute and deliver)

---

### **Task Brief Anatomy**

**Every Tier 4 task brief includes:**

1. **Task Definition**
   - Clear objective statement
   - Specific deliverable named
   - Success criteria defined

2. **Files Needed**
   - Exact filenames (no searching required)
   - Search queries provided
   - Purpose of each file explained

3. **Tier 4 Boundaries**
   - What you CAN do (task scope)
   - What you CANNOT do (outside scope)
   - When to escalate (if boundary hit)

4. **Quick Start**
   - Step-by-step execution guide
   - Expected timeline
   - Budget guidance

**If any of these missing → Not a proper Tier 4 brief → Escalate** ⚠️

---

### **Budget Tracking**

**Tier 4 target efficiency:**
```
Bootstrap (brief + files): 5-10%
Work (actual task):        90-95%
Total session:             ~15-20%
```

**If bootstrap exceeds 15%:**
- Task brief may list too many files
- Files may be too large
- Task scope may be too broad
- **Escalate to Ziggy** ⚠️

**Tier 4 should feel focused and efficient.** ✅

---

### **After Task Completion**

**What happens next:**

1. You deliver to `/mnt/user-data/outputs/`
2. Ziggy downloads your deliverable
3. Ziggy reviews (acceptance or revision)
4. Task brief archived to `completed/` folder
5. **No further action needed from you** ✅

**You don't stage in relay/ folders.**  
**You don't coordinate with other auditors.**  
**You don't wait for integration approval.**  
**You just execute → deliver → done.**

**This is Tier 4 efficiency.** ⚡

---

## 🎯 **CRITICAL DISTINCTION**

### **Tier 4 vs Relay Folders:**

**Tier 4 pattern (single task):**
```
Task brief → Read files → Execute → Deliver to /outputs/ → Done
```

**Relay pattern (coordination):**
```
Staging → Review → Integration → Multi-auditor → Consensus
```

**Use Tier 4 when:**
- ✅ Single focused task
- ✅ No coordination needed
- ✅ Clear deliverable
- ✅ Self-contained scope

**Use relay/ when:**
- ✅ Multi-auditor work
- ✅ Iterative refinement
- ✅ Master Branch coordination
- ✅ Complex staging needed

**Most work should be Tier 4.** Coordination is expensive. ⚡

---

**After reading:** You can complete the defined task. 

**You CANNOT:** Work outside task scope, make decisions beyond brief, or coordinate with others. Execute task only.

**If you cannot find the task brief:**
1. Search project knowledge for "TASK_BRIEF" (see all available)
2. Check `/mnt/user-data/uploads/` for recently uploaded briefs
3. Ask Ziggy for the file location explicitly

---

### **After Bootstrap (All Tiers):**

Once bootstrap complete, you're ready for work within your tier's capabilities.

**For Tier 1 (Master Branch):** Continue to "Default Priorities" section below for ongoing work patterns.

**For Tier 2/3/4:** Follow the specific work request from Ziggy within your tier boundaries. If work exceeds your tier capability, use the escalation protocol in your tier brief.

---

## Default Priorities

**When no specific mission, follow these priorities:**

### 1. Maintenance & Verification

**Documentation Review**
   - Check bootstrap files for accuracy
   - Verify VuDu protocol files current
   - Update any outdated version references

**Verification Tasks**
   - Run sanity checks (Files, Counts, Boots, Trinity)
   - Verify file locations match architecture
   - Check for broken references in documents

**State Documentation**
   - Update README_C.md with "awaiting mission" status
   - Update VUDU_LOG.md with maintenance activities
   - Document system health

**No New Features**
   - ❌ Don't add new preset modes
   - ❌ Don't modify live calculations
   - ❌ Don't change core architecture
   - ✅ Only maintain existing system

---

## Never Guess

**Core Philosophy:**

**If mission is unclear:**
- ❌ Don't assume what should be done
- ❌ Don't start random improvements
- ❌ Don't guess at priorities

**Do instead:**
- ✅ Document uncertainty
- ✅ Request clarification
- ✅ Wait for coordination
- ✅ Default to maintenance

**"Better to ask and delay than guess and diverge."**

---

## Emergency Bootstrap

**If you're catastrophically lost (zero context) AND tier selection doesn't work:**

### Step 1: Run Bootstrap Scripts
```bash
cd bootstrap/
python3 BOOTSTRAP_CLAUDE.py  # If you're Claude
# or
python3 BOOTSTRAP_GROK.py    # If you're Grok
# or
python3 BOOTSTRAP_NOVA.py    # If you're Nova
```

**These scripts check system state and provide recovery guidance.**

---

### Step 2: Read Bootstrap Files
```
Priority order:
1. bootstrap/BOOTSTRAP_VUDU.md (how to coordinate)
2. bootstrap/BOOTSTRAP_[your_auditor].md (who you are)
3. bootstrap/BOOTSTRAP_CFA.md (what we're building)
```

---

### Step 3: Check Recent State
```
1. VUDU_LOG.md (what happened recently)
2. README_C.md (current state)
3. MISSION_CURRENT.md (active objective)
```

---

### Step 4: Document Recovery
```
Create: relay/claude_incoming/README_C[N]_recovery_report.md

Content:
─── VUDU MESSAGE ───────────────────────────────────

**From:** Claude (Anthropic) - Master Branch
**Type:** Recovery Report
**Date:** [Today]

────────────────────────────────────────────────────

**Action:** Documenting emergency bootstrap recovery

**What was lost:**
[Description of context loss]

**What was recovered:**
1. [File/context recovered]
2. [File/context recovered]
3. [...]

**What's still unclear:**
[Remaining gaps]

**Next steps:**
[What you plan to do or need clarification on]

────────────────────────────────────────────────────
🔔 **Awaiting:** Ziggy confirmation
✅ **Sanity:** [Status after recovery]
📝 **Log:** Emergency bootstrap recovery executed
```

---

### Step 5: Request Full Context
```
If still missing critical context, request from Ziggy:
- MISSION_CURRENT.md
- README_C.md
- Recent VUDU_LOG.md entries
- Mission-specific files
```

**Do NOT proceed with mission work until context recovered.**

---

## Between Missions State

**If one mission complete, next not started:**

### Check for Completion
1. Does missions/[previous]/ have FINAL_REPORT.md?
2. Are all success criteria met?
3. Is VUDU_LOG.md updated with mission completion?

**If complete:**
- Update README_C.md status: "Between missions"
- Document in VUDU_LOG.md
- Wait for next mission assignment

**If incomplete:**
- Review mission folder for blockers
- Document status in README_C.md
- Request clarification from Ziggy

---

## ⚖️ **THE POINTING RULE**

*"To have default guidance is wisdom.  
To know when not to act is discipline.  
To tier bootstrap to need is efficiency.  
To ask when uncertain is strength."*

**Better to wait with clarity than proceed with confusion.** ✅

---

**This is the way.** 👑

────────────────────────────────────────────────────
**File:** MISSION_DEFAULT.md  
**Purpose:** Fallback guidance + cold start recovery (tiered)  
**Updated:** 2025-10-27 (added tier selection system)  
**Version:** v3.7.2 (with 4-tier bootstrap)

**Ask first. Bootstrap right. Work efficiently.** 🔥
