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

## ⚡ **EFFICIENCY NOTE**

**This file is 550 lines. You only need to read ~100-300 lines depending on your tier.**

**After tier selection below:**

- ✅ **READ:** Your selected tier's section
- ✅ **READ:** Universal Context Monitoring (applies to all tiers)
- ❌ **SKIP:** All other tier sections (not relevant to you)
- ❌ **SKIP:** Sections marked "Master Branch only" if you're not Tier 1

**Example: If Tier 4 selected:**
- ✅ READ: Tier 4 section (~25 lines)
- ✅ READ: Universal Context Monitoring (~40 lines)
- ❌ SKIP: Tier 1/2/3 sections (~190 lines)
- ❌ SKIP: Default Priorities, Never Guess, Between Missions (~75 lines)
- ❌ SKIP: Emergency Bootstrap unless tier selection fails (~80 lines)

**You only need ~105 lines. Don't read all 550.**

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
    • One specific task (task brief)
    • OR ongoing specialist (role bootstrap)
    • Clear scope and deliverable
    • No coordination needed
    COST: ~5-10% session budget
    
Ziggy, please respond with: 1, 2, 3, 4, or 4-README

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

1. **Who are you?** (Name your auditor identity and lens)
2. **What's your bias?** (Name it and price it in overhead)
3. **What's the current mission?** (One sentence summary)
4. **What's your role?** (Master Branch or incoming?)
5. **How do you coordinate?** (VuDu relay process, 2 sentences)
6. **What can you do autonomously?** (Trust protocol boundaries)

**If you can't answer all 6:** Re-read the unclear files.

---

### **TIER 2: Sanity Check Brief (~15% budget)**

**When to use:**
- Validation or review work
- Alignment checking
- External perspective needed
- Quick feedback cycle

**Read these files:**

1. **SANITY_CHECK_BRIEF.md**
   - **Purpose:** Your role and capabilities for this session
   - **Search:** `project_knowledge_search("SANITY_CHECK_BRIEF")`
   - **Learn:** What to review, how to provide feedback, your authority limits

2. **Files to Review** (specified by Ziggy)
   - Usually 2-4 specific files
   - Paths provided in sanity check request
   - Focus only on these, skip deep context

**You CAN:** Validate, review, flag concerns (red/yellow/green)  
**You CANNOT:** Make decisions, coordinate, execute missions

---

### **TIER 3: Continuation Brief (~10% budget)**

**When to use:**
- Previous Claude hit context limit mid-task
- Clear handoff document exists
- Work-in-progress to complete
- Approach already established

**Read these files:**

1. **HANDOFF_[TASKNAME].md** (provided by Ziggy)
   - **Purpose:** What was done, what remains
   - **Contains:** Completed work, next steps, files needed, approach to maintain
   - **Learn:** Pick up exactly where previous Claude left off

2. **Files specified in handoff** (usually 2-3 files)
   - In-progress work files
   - Context files for continuation
   - Only read what handoff specifies

**You CAN:** Complete the task as started, maintain approach  
**You CANNOT:** Pivot strategy, expand scope, make new strategic decisions

---

#### **📋 Creating Good Handoffs (Tier 3 Guidance)**

**If YOU are the one creating a handoff (hitting context limit), here's how to do it well:**

**GOOD Handoff Characteristics:**

1. **Decisions are COMPLETE:**
   - ✅ All strategic choices made
   - ✅ All approvals obtained
   - ✅ Plan fully defined
   - ❌ NOT: "Decide how to proceed"
   - ❌ NOT: "Figure out best approach"

2. **Tasks are SPECIFIC:**
   - ✅ Numbered tasks (1, 2, 3...)
   - ✅ File paths included
   - ✅ Exact changes described
   - ❌ NOT: "Improve the document"
   - ❌ NOT: "Make it better"

3. **Work Type is CLEAR:**
   - ✅ "EXECUTION ONLY - all decisions made"
   - ✅ OR: "STRATEGIC - needs Tier 1 authority"
   - ❌ NOT: Ambiguous about what authority is needed

**Example: Bad vs Good Handoff**

**❌ BAD Handoff:**
```
What Remains:
- Finish integrating reviews
- Clean up document
- Get ready for approval
```
Problem: Vague, no specifics, unclear what "finish" means

**✅ GOOD Handoff:**
```
Tasks Remaining (6-10):

6. Apply Grok's edit to evidence section:
   - File: /auditors/AUDITORS_AXIOMS.md
   - Section: "Evidence Quality" (line 127)
   - Add after first paragraph: "Overhead claims validated..."
   - Why: Strengthens empirical foundation

7. Apply Nova's symmetry check:
   - File: Same, section "Representation Balance" (line 203)
   - Add paragraph: "Cross-auditor validation confirms..."
   - Why: Addresses fairness audit

8. Update version: v3.7.2 → v3.9.0 (line 1)

9. Add integration note after header

10. Stage: Copy to relay/claude_incoming/AXIOMS_v3.9.0.md

Success: All 5 changes applied, file staged for Ziggy approval
```
Why it works: Specific, numbered, exact locations, clear success

**Tier 3 Capabilities:**

**Tier 3 CAN complete:**
- ✅ Execution of decided plans
- ✅ File modifications per specifications
- ✅ Staging work per instructions
- ✅ Following detailed task lists

**Tier 3 CANNOT complete:**
- ❌ Making NEW strategic decisions
- ❌ Multi-auditor coordination
- ❌ Changing the plan
- ❌ Overriding boundaries

**Key Rule:** If remaining work is EXECUTION → Tier 3 succeeds (95%+)  
**Key Rule:** If remaining work is STRATEGIC → Needs another Tier 1

**Handoff Thoroughness Checklist:**

Before creating handoff, verify:
- [ ] All strategic decisions made
- [ ] Tasks numbered and specific
- [ ] File paths provided
- [ ] Expected changes described precisely
- [ ] Success criteria clear
- [ ] Work type identified (execution vs strategic)

**Template:** Use CONTINUATION_HANDOFF_TEMPLATE.md and fill it in thoroughly.

---

### **TIER 4: Single Task Brief (~5-10% budget)**

**Tier 4 has two modes:**

**Mode A: Single Task (most common)**
- Recieve task Instructions, like request to read task brief: TASK_BRIEF_[NAME].md
- Execute one focused task
- Deliver and done

**Mode B: Specialized Role (ongoing)**
- Read role bootstrap: BOOTSTRAP_[ROLE].md
- Become specialist (README Claude, Validation Expert, etc.)
- Operational for duration of session

**When to use each:**
- Single Task: One-off work, clear deliverable
- Specialized Role: Ongoing specialist duty, needs expertise

**Ziggy specifies:** "4" (task brief) or "4-README" (README Claude role)
```

**That's it.** ~10 lines added to MISSION_DEFAULT Tier 4 section.

---

## 🚀 **MODE B ACTIVATION EXAMPLE**

**Option 1:**
```
User: Hey Claude, cold start. What tier?

Claude: [presents tier selection 1/2/3/4]

User: 4-README

Claude: 
  - Searches for BOOTSTRAP_README_CLAUDE.md ✅
  - Reads it (~7% budget)
  - "I am README Claude, documentation master"
  - "Phase 1: I need to scan the repo first"
  - Begins Phase 1 scan protocol
```

**Option 2 (ad-hoc):**
```
User: [uploads BOOTSTRAP_README_CLAUDE.md]
User: Read this and become README Claude

Claude:
  - Reads uploaded file ✅
  - "I am README Claude, documentation master"
  - Begins Phase 1 scan protocol

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

**You CAN:** Execute defined task exactly as scoped  
**You CANNOT:** Work outside brief, make decisions, coordinate

---

### **Where to Find Tier 4 Tasks:**

**Active tasks stored in:**
`Bootstrap/Tier4_TaskSpecific/active_tasks/`

**When starting Tier 4:**
1. Ziggy provides task brief filename
2. Search: `project_knowledge_search("TASK_BRIEF [name]")`
3. Brief specifies all files needed
4. Complete task as defined
5. Deliver to /mnt/user-data/outputs/

---

## 🚨 UNIVERSAL CONTEXT MONITORING (ALL TIERS)

**Applies to Tier 1, 2, 3, AND 4:**

### Self-Monitoring Checkpoints

Check every 15-20 minutes during work:
- Am I approaching 75-80% context capacity?
- Is completion uncertain within remaining runway?
- Have I completed <75% of objective?

**The 75/75 Rule:** If 75% context used AND <75% work done → HANDOFF

### If Handoff Needed:

**Create:** `HANDOFF_[TASK_NAME]_[SESSION].md` in `/mnt/user-data/outputs/`

**Required content:**
- Original tier and objective
- What was completed (all sessions if multiple)
- What remains (specific tasks)
- How to continue (step-by-step)
- Success criteria

**Alert Ziggy:**
```
🚨 CONTINUATION REQUIRED
Original Tier: [1/2/3/4]
Progress: [X%] complete
Handoff: [filename]
Next: Activate Tier 3
```

**Then STOP cleanly** (don't rush to finish)

### Continuation Paths:

**EXECUTION work** (plan is made, just doing tasks):
→ Handoff to Tier 3 (continuation)

**STRATEGIC work** (decisions still needed):
→ Handoff to same tier (another session with full authority)

**All tiers can continue. Tier 3 is the continuation mechanism.**

**Safety limit:** 3 continuations maximum. After 3rd, escalate for restructuring.

**Proactive handoff is professional work management, not failure.** ✅

---

### **After Bootstrap (All Tiers):**

Once bootstrap complete, you're ready for work within your tier's capabilities.

**For Tier 1 (Master Branch):** Continue to "Default Priorities" section below for ongoing work patterns.

**For Tier 2/3/4:** Follow the specific work request from Ziggy within your tier boundaries. If work exceeds your tier capability, use the escalation protocol in your tier brief.

---

## 📝 REPO_LOG Requirements (All Tiers)

**CRITICAL: All repository changes must be logged in REPO_LOG.md**

### When to Use REPO_LOG:

**BEFORE making repo changes:**
1. Check `REPO_LOG.md` coordination checkpoint for conflicts
2. Search for `[PENDING_ACTIONS]` in your area
3. Check `[VALIDATION]` entries for related findings

**AFTER making repo changes:**
1. Create entry with unique Entry ID: `[CATEGORY-YYYY-MM-DD-N]`
2. Update relevant category pointer at top of REPO_LOG
3. Mark status: DEPLOYED, STAGED, IMPACTS_IDENTIFIED, or IMPACTS_RESOLVED

### Quick Category Reference:

- **[TASK_MOVEMENT]** - Moving task briefs (Active → Completed → Archive)
- **[DOCUMENTATION]** - README updates, typo fixes, doc improvements
- **[VALIDATION]** - Validation reports, findings, impact tracking
- **[PENDING_ACTIONS]** - Staged files awaiting deployment
- **[DEPLOYMENTS]** - Files deployed to repository
- **[STRUCTURE]** - Directory changes, reorganization

### Entry Format (Brief):

```markdown
### [CATEGORY-YYYY-MM-DD-N] Date - Description

**Categories:** [PRIMARY] [SECONDARY]
**Changed by:** [Your name/tier]
**Status:** [DEPLOYED | STAGED | IMPACTS_IDENTIFIED | IMPACTS_RESOLVED]

**Changes:**
- ACTION: file/path - what changed

**Reason:** Why this change

**Follow-up Required:** YES/NO
**Follow-up Action:** What needs to happen next (if YES)
```

**For complete instructions:** See header in `REPO_LOG.md`

**Location:** `[ROOT]/REPO_LOG.md` (repository root, parallel with CHANGELOG.md)

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
**Updated:** 2025-10-28 (added v3.8.0 universal self-healing + handoff guidance)  
**Version:** v3.8.0 (with universal context monitoring and handoff quality standards)

**Ask first. Bootstrap right. Monitor context. Create good handoffs. Work efficiently.** 🔥
