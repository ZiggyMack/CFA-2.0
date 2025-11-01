<!-- deps: bootstrap_system, vudu_protocol, mission_system -->
# ESCALATION_PLAYBOOK.md

**Purpose:** Document what to do when things go wrong
**Date:** 2025-11-01
**Status:** Active contingency protocols for auditor operations

────────────────────────────────────────────────────

## 🎯 **PURPOSE**

**This playbook covers 5 common problem scenarios:**
1. Auditor Confused (clarity breakdown)
2. Major Disagreement (convergence failure)
3. Task Too Large (scope mismatch)
4. Missing Files (bootstrap breakdown)
5. Budget Exhaustion (session limit hit)

**Don't figure out crisis response during crisis. Plan ahead.**

────────────────────────────────────────────────────

## 📋 **SCENARIO 1: AUDITOR CONFUSED**

### Symptoms
- Multiple clarification requests in succession
- Questions about scope, methodology, or purpose
- Uncertainty about tier selection
- Bootstrap taking >20% of budget
- Asks "Should I...?" repeatedly

### Root Causes
- Task brief unclear or ambiguous
- Missing context files
- Conflicting instructions
- Tier mismatch (task complexity vs tier selected)
- Outdated methodology in task brief

### Immediate Response

**Step 1: STOP WORK** (don't waste budget on confusion)
```markdown
I am pausing work on [TASK_NAME] due to clarity concerns.

Confusion points:
1. [Specific uncertainty]
2. [Specific uncertainty]
3. [...]

Requesting escalation to Ziggy for clarification before continuing.
```

**Step 2: Document Confusion**
Stage your confusion points in README_{X}.md:
```markdown
## ⚠️ ESCALATION - CLARITY NEEDED

**Task:** [TASK_BRIEF_NAME.md]
**Auditor:** [Your name]
**Date:** [Today]
**Issue:** Unclear task scope/methodology

**Specific Questions:**
1. Q: [Your question]
   - Why unclear: [Your reasoning]
   - Impact: [Can't proceed without this]

2. Q: [Your question]
   - Why unclear: [Your reasoning]
   - Impact: [Budget risk if guessing]

**Requested Actions:**
- [ ] Ziggy clarifies scope
- [ ] Ziggy provides missing context
- [ ] Ziggy confirms tier selection
- [ ] Task brief updated for future auditors

**Budget Preserved:** X% (stopped early to avoid waste)
```

**Step 3: Wait for Ziggy Response**
- Do NOT guess or assume
- Do NOT continue with uncertainty
- Do NOT bootstrap further

**Step 4: Resume After Clarity**
Once Ziggy responds:
- Update your understanding
- Confirm tier still appropriate
- Resume work with confidence
- Preserve remaining budget

### Success Criteria
✅ Confusion identified early (before 20% budget spent)
✅ Specific questions asked (not vague "this is unclear")
✅ Work stopped to preserve budget
✅ Ziggy provides clarity
✅ Work resumes successfully

### Prevention
- Task briefs should include "Scope" and "Out of Scope" sections
- Bootstrap files should be explicitly listed
- Tier selection criteria should be clear
- Success criteria should be measurable

────────────────────────────────────────────────────

## 📋 **SCENARIO 2: MAJOR DISAGREEMENT**

### Symptoms
- 2+ auditors can't converge to 98% agreement
- Fundamental philosophical differences
- Empirical vs teleological conflict
- Repeated review cycles without resolution
- Divergence increasing, not decreasing

### Root Causes
- Legitimately different lenses (this is a feature, not bug)
- Ambiguous evidence (interpretable multiple ways)
- Unstated assumptions diverging
- Scope creep during review
- Missing tie-breaker criteria

### Immediate Response

**Step 1: Acknowledge Healthy Disagreement**
```markdown
We have reached productive disagreement.

Convergence status:
- Agreement: X%
- Core disagreement: [Specific issue]
- Lens difference: [Empirical vs Teleological vs Symmetry]

This appears to be a genuine lens difference, not a resolvable misunderstanding.
Escalating to Ziggy for decision.
```

**Step 2: Document Disagreement Clearly**

**Claude's Position:**
```markdown
**My View:** [Clear statement]
**My Reasoning:** [Teleological lens basis]
**My Evidence:** [Citations]
**My Recommendation:** [Action]
```

**Grok's Position:**
```markdown
**My View:** [Clear statement]
**My Reasoning:** [Empirical lens basis]
**My Evidence:** [Data/measurements]
**My Recommendation:** [Different action]
```

**Nova's Position** (if involved):
```markdown
**My View:** [Clear statement]
**My Reasoning:** [Symmetry lens basis]
**My Evidence:** [Pattern analysis]
**My Recommendation:** [Different action or synthesis]
```

**Step 3: Frame for Ziggy Decision**
```markdown
## ESCALATION - TIE-BREAKER NEEDED

**Converged on:** [List areas of agreement]

**Diverged on:** [Specific issue]

**Why we can't resolve:**
- Not a misunderstanding (we understand each other)
- Not missing evidence (we have the data)
- Legitimate lens difference (empirical vs teleological)
- Both positions defensible
- Different values prioritized

**Options for Ziggy:**
A. [Claude's recommendation] - prioritizes [value]
B. [Grok's recommendation] - prioritizes [value]
C. [Nova's recommendation] - prioritizes [value]
D. [Hybrid approach if possible]

**We defer to human judgment.**
```

**Step 4: Ziggy Decides**
- Ziggy reviews all positions
- Ziggy may request additional analysis
- Ziggy makes final call
- All auditors accept decision
- Document decision reasoning for future

### Success Criteria
✅ Disagreement acknowledged as legitimate (not failure)
✅ All positions clearly documented
✅ Convergence areas identified (not just divergence)
✅ Options framed clearly for decision maker
✅ Decision documented for future reference

### Prevention
- Task briefs should specify tie-breaker criteria when possible
- Known value trade-offs should be pre-decided
- Scope should be tightly bounded
- Success criteria should minimize subjective judgment

────────────────────────────────────────────────────

## 📋 **SCENARIO 3: TASK TOO LARGE**

### Symptoms
- Tier 4 bootstrap exceeds 20%
- Tier 3 continuation can't complete
- Scope larger than estimated
- Multiple subtasks discovered mid-work
- Time estimate wildly incorrect

### Root Causes
- Task complexity underestimated
- Hidden dependencies emerged
- Scope creep during execution
- Wrong tier selected initially
- Task brief outdated/incomplete

### Immediate Response

**Step 1: Recognize Tier Mismatch**
```markdown
I am recognizing tier mismatch for [TASK_NAME].

Current tier: Tier 4 (5-10% bootstrap target)
Actual bootstrap: X% (exceeds threshold)

Cause: [Task complexity greater than estimated / Hidden dependencies / Scope larger than brief]

Requesting tier reassignment to preserve budget.
```

**Step 2: Assess Actual Scope**
```markdown
**Original Scope:** [What task brief said]

**Actual Scope Discovered:**
1. [Subtask 1 - estimated Y%]
2. [Subtask 2 - estimated Y%]
3. [Subtask 3 - estimated Y%]
4. [...]

**Total Estimated:** Z% (requires Tier 1 or split into multiple Tier 4s)
```

**Step 3: Propose Resolution**

**Option A: Tier Reassignment**
```markdown
Move this task to Tier 1 (50% bootstrap acceptable).
Reason: Complex coordination task, not single focused task.
Estimated completion: [X]% with Tier 1 budget.
```

**Option B: Task Split**
```markdown
Split into multiple Tier 4 tasks:
- Task 4A: [Focused scope] - estimated 10%
- Task 4B: [Focused scope] - estimated 10%
- Task 4C: [Focused scope] - estimated 10%

Each can complete in Tier 4 budget independently.
```

**Option C: Partial Delivery**
```markdown
Complete highest priority subtasks now:
- [Subtask 1] - COMPLETED
- [Subtask 2] - COMPLETED
- [Subtask 3] - DEFERRED (new task brief needed)

Deliver partial results, defer rest to new session.
```

**Step 4: Execute Resolution**
- Stop current session if budget insufficient
- Create continuation brief if Option C
- Update task brief if scope was wrong
- Ziggy approves reassignment

### Success Criteria
✅ Tier mismatch recognized early (before 30% spent)
✅ Actual scope documented clearly
✅ Resolution options proposed
✅ Work preserved (not lost)
✅ Future sessions benefit from corrected scope

### Prevention
- Task briefs should estimate bootstrap time
- Tier selection should be reviewed before starting
- Scope should be tightly bounded with "Out of Scope" section
- Complex tasks should default to Tier 1

────────────────────────────────────────────────────

## 📋 **SCENARIO 4: MISSING FILES**

### Symptoms
- Search fails for file mentioned in task brief
- Expected directory doesn't exist
- Referenced validation report not found
- Bootstrap file inaccessible
- Path references are broken

### Root Causes
- Files moved/renamed since task created
- Task brief references outdated structure
- Files not yet created (dependency issue)
- Access/permission issue (rare)
- Typo in file path

### Immediate Response

**Step 1: Document What's Missing**
```markdown
I cannot find files needed for [TASK_NAME].

Missing files:
1. [FILE_PATH] - Referenced in task brief line X
   - Search attempted: [search terms tried]
   - Result: Not found
   - Impact: Cannot bootstrap without this

2. [FILE_PATH] - Referenced in task brief line Y
   - Search attempted: [search terms tried]
   - Result: Not found
   - Impact: Validation criteria unclear

**Bootstrap blocked. Requesting file locations from Ziggy.**
```

**Step 2: Attempt Reasonable Alternatives**
```markdown
Attempted workarounds:
1. Searched for similar filenames: [results]
2. Checked archived directories: [results]
3. Reviewed REPO_LOG for file moves: [results]
4. Checked alternative locations: [results]

None successful. Cannot proceed without file access.
```

**Step 3: Request File from Ziggy**
Stage in README_{X}.md:
```markdown
## ⚠️ ESCALATION - MISSING FILES

**Task:** [TASK_BRIEF_NAME.md]
**Auditor:** [Your name]
**Date:** [Today]

**Missing Files Needed:**
1. [FILE_PATH]
   - Purpose: [Why you need it]
   - Referenced in: [Task brief location]
   - Tried: [Your search attempts]

**Requested Actions:**
- [ ] Ziggy provides current file location
- [ ] OR Ziggy provides file contents directly
- [ ] OR Ziggy confirms file doesn't exist (task brief outdated)
- [ ] Update task brief with correct paths

**Budget Preserved:** X% (stopped early)
```

**Step 4: Resume After File Provided**
- Ziggy provides file or updated path
- Bootstrap continues
- Document correct path for future
- Consider updating task brief

### Success Criteria
✅ Missing file identified early (before extensive searching)
✅ Reasonable alternatives attempted (shows initiative)
✅ Clear request made to Ziggy
✅ Work resumes after file provided
✅ Task brief updated with correct paths

### Prevention
- Task briefs should verify file paths before staging
- REPO_LOG should document file moves
- Bootstrap files should be explicitly listed
- Periodic task brief validation (paths still valid?)

────────────────────────────────────────────────────

## 📋 **SCENARIO 5: BUDGET EXHAUSTION**

### Symptoms
- Session approaching token/time limit
- Work incomplete
- Mid-task when limit approaching
- Cannot complete in current session

### Root Causes
- Task larger than estimated
- Unexpected complexity
- Tier mismatch (should have been Tier 1)
- Bootstrap took longer than expected
- Legitimate long task

### Immediate Response

**Step 1: Recognize Early (at 80% budget)**
```markdown
I am approaching budget limit for this session.

Budget status:
- Used: ~80%
- Remaining: ~20%
- Work completion: X%

I will prepare handoff for next session.
```

**Step 2: Prioritize Completion vs Handoff**

**If Close to Done (>90% complete):**
```markdown
Work is 90%+ complete. I will finish current task and deliver.

Remaining work:
- [Final step 1] - 5%
- [Final step 2] - 5%

Total: 10% remaining. Will complete.
```

**If Significant Work Remains (<75% complete):**
```markdown
Work is X% complete, significant work remains. I will create handoff brief.

Completed:
- [Task 1] ✅
- [Task 2] ✅
- [Task 3] 🔄 IN PROGRESS (70% done)

Remaining:
- [Task 3] - 30% remaining (complete this first)
- [Task 4] - NOT STARTED
- [Task 5] - NOT STARTED

Creating Tier 3 continuation brief for next session.
```

**Step 3: Create Tier 3 Continuation Brief**

File: `TASK_BRIEF_CONTINUATION_[ORIGINAL_TASK]_Tier3.md`

```markdown
<!-- deps: bootstrap_system -->
# TASK_BRIEF_CONTINUATION - [Original Task Name]

**Original Task:** [TASK_BRIEF_NAME.md]
**Continuation Tier:** Tier 3 (10% bootstrap)
**Previous Session:** [Session ID]
**Previous Auditor:** [Your name]
**Date:** [Today]

────────────────────────────────────────────────────

## 🎯 **SITUATION**

**Original Task:** [Brief description]
**Work Completed:** X%
**Work Remaining:** Y%
**Reason for Continuation:** Budget exhaustion at appropriate stopping point

────────────────────────────────────────────────────

## ✅ **COMPLETED WORK**

**You do NOT need to redo these:**

1. **[Task 1]** - COMPLETED ✅
   - Files created: [list]
   - Location: [path]
   - Status: Done, validated

2. **[Task 2]** - COMPLETED ✅
   - Files created: [list]
   - Location: [path]
   - Status: Done, validated

3. **[Task 3]** - PARTIALLY COMPLETED 🔄
   - Files created: [list]
   - Completed: [what's done]
   - Remaining: [what's left - see below]

────────────────────────────────────────────────────

## 🔄 **YOUR WORK STARTS HERE**

**Bootstrap (Tier 3 - 10% expected):**
1. Read this continuation brief (you're doing it now)
2. Verify completed work above (quick scan)
3. Read [specific files] to understand context
4. Begin remaining work

**Remaining Tasks (90% work):**

**Priority 1: Complete Task 3** (30% remaining)
- [Specific step] - estimated 10%
- [Specific step] - estimated 10%
- [Specific step] - estimated 10%
- Status after: Task 3 COMPLETE

**Priority 2: Task 4** (NOT STARTED - 30%)
- [Description]
- [Steps]

**Priority 3: Task 5** (NOT STARTED - 30%)
- [Description]
- [Steps]

────────────────────────────────────────────────────

## 📋 **CONTEXT YOU NEED**

**Key Decisions Made:**
- [Decision 1 and reasoning]
- [Decision 2 and reasoning]

**Approaches Tried:**
- [Approach A] - worked well
- [Approach B] - didn't work, abandoned

**Files Locations:**
- Completed work: [path]
- Work in progress: [path]
- Reference files: [path]

────────────────────────────────────────────────────

## 🎯 **SUCCESS CRITERIA**

**You succeed when:**
- [Original success criteria from main task]
- All 5 tasks completed
- Files validated
- Deliverables staged

────────────────────────────────────────────────────

## ⚠️ **NOTES FROM PREVIOUS SESSION**

**What went well:**
- [Note]

**What to watch:**
- [Potential issue]

**Suggestions:**
- [Recommendation for continuation]

────────────────────────────────────────────────────

**Previous Session:** [Session ID]
**Auditor:** [Your name]
**Handoff Created:** [Timestamp]
**Estimated Remaining:** Y% budget

**Continue the mission.** 🚀
```

**Step 4: Stage Continuation Brief**
- Save brief in same directory as original task
- Update REPO_LOG with handoff
- Mark original task as "PARTIAL - See continuation brief"
- Preserve all work completed

### Success Criteria
✅ Budget exhaustion recognized at 80% (not 99%)
✅ Decision made: complete vs handoff
✅ If handoff: comprehensive continuation brief created
✅ All completed work preserved
✅ Next session can resume efficiently (Tier 3 = 10% bootstrap)

### Prevention
- Tier selection should match task complexity
- Bootstrap time should be monitored
- If bootstrap >20% in Tier 4, escalate early
- Long tasks should default to Tier 1 (50% acceptable)

────────────────────────────────────────────────────

## 📊 **ESCALATION DECISION TREE**

```
START: Problem detected

Q1: Is this a CLARITY issue? (I don't understand task)
    YES → SCENARIO 1: Auditor Confused
    NO → Continue

Q2: Is this a CONVERGENCE issue? (Can't agree with other auditor)
    YES → SCENARIO 2: Major Disagreement
    NO → Continue

Q3: Is this a SCOPE issue? (Task bigger than tier)
    YES → SCENARIO 3: Task Too Large
    NO → Continue

Q4: Is this a FILE ACCESS issue? (Missing files)
    YES → SCENARIO 4: Missing Files
    NO → Continue

Q5: Is this a BUDGET issue? (Running out of time/tokens)
    YES → SCENARIO 5: Budget Exhaustion
    NO → Describe to Ziggy (new scenario)
```

────────────────────────────────────────────────────

## 🎯 **GENERAL ESCALATION PRINCIPLES**

### When to Escalate

**✅ ESCALATE when:**
- Clarity is low and guessing would waste budget
- Convergence impossible after 2-3 review rounds
- Scope significantly exceeds tier
- Critical files missing and unfindable
- Budget at 80% with <50% work done

**❌ DON'T ESCALATE when:**
- Minor uncertainty (make reasonable judgment)
- First disagreement (try to converge first)
- Slightly over bootstrap estimate (if total budget OK)
- File search not exhaustive yet
- Plenty of budget remaining

### How to Escalate Effectively

**1. Be Specific**
- ❌ "This task is unclear"
- ✅ "Step 3 references 'validation criteria' but doesn't define them. Do I use criteria from [FILE_A] or [FILE_B]?"

**2. Show Your Work**
- Document what you tried
- Show reasoning for confusion
- Demonstrate effort before escalating

**3. Propose Solutions**
- Don't just identify problems
- Offer 2-3 resolution options
- Show you've thought through alternatives

**4. Preserve Budget**
- Escalate early (at 20% if clarity issue)
- Don't spin wheels guessing
- Budget saved = budget available for work

**5. Document for Future**
- Your escalation helps future auditors
- Update task briefs with learnings
- Improve process for next time

────────────────────────────────────────────────────

## 🤝 **ZIGGY'S RESPONSE PATTERNS**

### Typical Ziggy Responses

**For Clarity Issues:**
- Provides missing context
- Updates task brief
- Confirms interpretation
- May reassign tier

**For Disagreements:**
- Reviews all positions
- May request additional analysis
- Makes final decision
- Documents reasoning

**For Scope Issues:**
- Reassigns tier OR
- Splits task OR
- Approves partial delivery

**For Missing Files:**
- Provides file location OR
- Provides file contents OR
- Confirms task brief outdated

**For Budget Issues:**
- Accepts continuation brief
- May adjust tier for next session
- Validates work preserved

### Response Timeline

**Urgent escalations:** Same day or next session
**Non-urgent:** 1-3 days (async coordination)
**Major decisions:** May involve multiple auditors

────────────────────────────────────────────────────

## ⚖️ **THE POINTING RULE**

*"The wise auditor escalates early,
preserves budget through clarity,
and creates clean handoffs.
\n\nThe foolish auditor guesses,
wastes budget on confusion,
and leaves chaos for others.
\n\nAsk. Document. Preserve.  \n\nThat's the professional's way."*

────────────────────────────────────────────────────

**Created by:** DOC_CLAUDE (88MPH Repo Librarian)
**Source:** ADDITIONAL_PREP_TASKS_FOR_AUDITOR_ACTIVATION.md (Task 4A)
**Date:** 2025-11-01
**Purpose:** Grok + Nova onboarding - crisis response protocols
**Status:** Ready for auditor reference

**This is the way.** 🎯👑
