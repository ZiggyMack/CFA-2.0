╔════════════════════════════════════════════════════╗
║   TASK BRIEF: ADD VALIDATION PROMPTS TO WORKFLOW   ║
║    Make Validation Reports Standard Practice       ║
╠════════════════════════════════════════════════════╣
║  Created: 2025-10-29                               ║
║  Priority: HIGH - Process improvement              ║
║  Type: Workflow Enhancement                        ║
║  Estimated Time: 60-90 minutes                     ║
╚════════════════════════════════════════════════════╝

## 🎯 PROBLEM IDENTIFIED

**Current state:**
- Tasks get completed ✅
- Executor has to be REMINDED separately to create validation report ❌
- Validation report creation is ad-hoc, not systematic ❌
- No standardized validation report template ❌
- Continuity unclear (what if executor hits context limit?) ❌

**Gap:**
When a Tier 4 task completes, there's no automatic prompt:
> "Do you want me to create a validation report for this work?"

**Result:**
- Validation reports get missed
- Quality assurance is inconsistent
- Human has to remember to request validation
- No structured handoff if validation needs separate session

---

## 🎯 DESIRED STATE

**After this task:**

When ANY task completes, executor should:
1. **Recognize completion** ✅
2. **Automatically ask:** "Do you want me to create a validation report for this?" ✅
3. **If yes:** Create validation report (if budget allows) ✅
4. **If approaching limit:** Offer to create Tier 3 continuation task for validation ✅
5. **Use standardized template** for validation reports ✅

**This should be built into task creation guidance, not relying on human memory.**

---

## 📋 SCOPE OF CHANGES

**What needs updating:**

### 1. **Task Brief Creation Guidelines**
- Add section: "Validation Closure Protocol"
- Specify when/how to prompt for validation
- Provide decision tree for budget scenarios

### 2. **Create: Standard Validation Report Template**
- New file: `VALIDATION_REPORT_TEMPLATE.md`
- Reusable across all task types
- Clear structure and guidance
- Adaptable to different validation needs

### 3. **Create: Tier 3 Continuation Template for Validation**
- New file: `TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md`
- Template for when Tier 4 hits context limit
- Handoff protocol from executor to validator
- Ensures continuity

### 4. **Update: Task Completion Checklist**
- Add validation prompt to completion steps
- Make it explicit and hard to miss
- Include budget awareness

---

## 📝 TASK EXECUTION PLAN

### Phase 1: Create Validation Report Template (20 min)

**File to create:** `/home/claude/VALIDATION_REPORT_TEMPLATE.md`

**Template should include:**

```markdown
# Validation Report: [Task Name]

**Validator:** [Name/designation]
**Date:** [Date]
**Task Validated:** [Task ID/name]
**Validation Type:** [Design / Execution / Output Quality]
**Validation Duration:** [X] minutes

---

## 📋 EXECUTIVE SUMMARY

**Overall Assessment:** [PASS / PASS WITH MINOR ISSUES / NEEDS REVISION]

**Quick Stats:**
- Critical Issues: [count]
- Major Issues: [count]
- Minor Issues: [count]
- Recommendations: [count]

**Bottom Line:** [1-2 sentence summary]

---

## ✅ WHAT WAS VALIDATED

**Artifacts reviewed:**
1. [File/output 1]
2. [File/output 2]
[List what you actually examined]

**Validation criteria:**
1. [Criterion 1]
2. [Criterion 2]
[What you checked for]

**Validation method:**
- [How you validated - checklist review? Testing? Cross-checking?]

---

## 🔍 DETAILED FINDINGS

### ✅ What Works Well

**Strengths identified:**
1. [Strength 1]
   - Evidence: [specific example]
   - Impact: [why this is good]

2. [Strength 2]
   - Evidence: [specific example]
   - Impact: [why this is good]

---

### 🚨 Critical Issues (Must Fix)

**Issues that block deployment/usage:**

1. **[Issue title]**
   - Location: [where found]
   - Problem: [what's wrong]
   - Fix Required: [specific action needed]
   - Impact if not fixed: [consequences]
   - Priority: CRITICAL

[Repeat for each critical issue]

---

### ⚠️ Major Issues (Should Fix)

**Issues that significantly impact quality:**

1. **[Issue title]**
   - Location: [where found]
   - Problem: [what's wrong]
   - Fix Recommended: [specific action]
   - Impact: [why this matters]
   - Priority: HIGH

[Repeat for each major issue]

---

### 📝 Minor Issues (Nice to Fix)

**Small improvements:**

1. [Issue description]
   - Location: [where]
   - Improvement: [what could be better]
   - Priority: LOW

[Repeat for each minor issue]

---

## 💡 RECOMMENDATIONS

**Suggestions for improvement:**

1. **[Recommendation title]**
   - Reasoning: [why suggest this]
   - Benefit: [what improves]
   - Effort: [LOW / MEDIUM / HIGH]

[Repeat for each recommendation]

---

## 🎯 VALIDATION DECISION

**Recommendation:** [Choose one]
- ✅ APPROVE - Deploy/use as-is
- ⚠️ APPROVE WITH FIXES - Fix critical/major issues, then deploy
- ❌ REVISE - Needs significant rework, revalidate after

**Reasoning:** [Brief explanation of decision]

**Required Actions (if any):**
1. [Action item]
2. [Action item]

**Timeline:** [When can this be deployed/used]

---

## 📊 VALIDATION EVIDENCE

**Methods used:**
- [Method 1: e.g., checklist review]
- [Method 2: e.g., cross-file consistency check]
- [Method 3: e.g., functional testing]

**Time invested:**
- Review time: [X] min
- Testing time: [X] min  
- Report creation: [X] min
- **Total:** [X] minutes

**Confidence level:** [HIGH / MEDIUM / LOW]
- Reasoning: [why this confidence level]

---

## ✅ CERTIFICATION

**I certify that:**
- [ ] I reviewed all artifacts listed
- [ ] I applied stated validation criteria
- [ ] I identified all critical issues
- [ ] My recommendations are actionable
- [ ] This report accurately reflects my findings

**Validated by:** [Name/designation]
**Date:** [Date]

---

**End of Validation Report**
```

**Save to:** `/home/claude/VALIDATION_REPORT_TEMPLATE.md`

---

### Phase 2: Create Tier 3 Continuation Template (20 min)

**File to create:** `/home/claude/TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md`

**Template structure:**

```markdown
╔════════════════════════════════════════════════════╗
║  TASK BRIEF: VALIDATION (TIER 3 CONTINUATION)      ║
║     Complete Validation Started by Previous        ║
╠════════════════════════════════════════════════════╣
║  Created: [Date]                                   ║
║  Priority: [Priority level]                        ║
║  Type: Tier 3 Continuation - Validation            ║
║  Context: Previous session hit context limit       ║
╚════════════════════════════════════════════════════╝

## 🔄 CONTINUATION CONTEXT

**Previous Session:**
- Executor: [Previous Claude designation]
- Task Completed: [Task name/ID]
- Status at Handoff: [What was completed]
- Context Limit: Reached at [approximate %]

**This Session:**
- Role: Validation specialist (Tier 3)
- Objective: Create validation report for completed work
- Scope: Validate artifacts from previous session

---

## 📦 ARTIFACTS TO VALIDATE

**From previous session:**
1. [Artifact 1 - file/output]
2. [Artifact 2 - file/output]
3. [Artifact 3 - file/output]

**Handoff notes from executor:**
[Paste handoff notes from previous Claude here]

---

## ✅ VALIDATION CRITERIA

**Check for:**
1. [Criterion 1 - specific to this task]
2. [Criterion 2 - specific to this task]
3. [Criterion 3 - specific to this task]

**Success criteria:**
- [What defines success for this work?]

---

## 📋 VALIDATION PROCESS

### Step 1: Review Handoff (10 min)
- Read handoff notes from previous session
- Understand what was completed
- Identify any flags or concerns noted

### Step 2: Locate Artifacts (5 min)
- Find all outputs in /mnt/user-data/outputs/
- Verify completeness (all expected files present?)
- Check file integrity

### Step 3: Systematic Validation (30-45 min)
- Apply validation criteria
- Document findings as you go
- Categorize issues (critical/major/minor)

### Step 4: Create Validation Report (20 min)
- Use VALIDATION_REPORT_TEMPLATE.md
- Complete all sections
- Make clear recommendation

### Step 5: Package & Deliver (5 min)
- Save validation report to outputs
- Update REPO_LOG (if applicable)
- Notify Ziggy

**Total Estimated Time:** 70-85 minutes

---

## 📝 VALIDATION REPORT

**Use template:** VALIDATION_REPORT_TEMPLATE.md

**Customize for this validation:**
- Task Validated: [Previous task name]
- Validation Type: [Design/Execution/Output Quality]
- Focus areas: [Specific to this task]

---

## 🎯 SUCCESS CRITERIA

**This continuation succeeds when:**
1. ✅ All artifacts from previous session reviewed
2. ✅ Validation report completed using template
3. ✅ Clear recommendation made (approve/fix/revise)
4. ✅ Issues categorized and documented
5. ✅ Report delivered to Ziggy

---

## ⚖️ TRUST PROTOCOL COMPLIANCE

**As Tier 3 continuation:**
- Read handoff notes carefully ✅
- Don't second-guess previous executor's work ✅
- Focus on validation, not re-doing ✅
- Document findings honestly ✅
- Provide actionable recommendations ✅

---

**Ready? Begin with Step 1: Review Handoff** 🔍

────────────────────────────────────────────────────
**File:** TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md
**Purpose:** Template for validation continuation tasks
**Version:** v1.0
**Created:** [Date]

**Validate thoroughly. Report clearly.** ✅
```

**Save to:** `/home/claude/TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md`

---

### Phase 3: Update Task Creation Guidance (20-30 min)

**File to update:** (Need to search for main task creation guidance file)

**Search for:**
- `project_knowledge_search("task creation guidelines")`
- `project_knowledge_search("task brief template")`
- `project_knowledge_search("tier 4 task creation")`

**Add section:** "Validation Closure Protocol"

**Content to add:**

```markdown
## 📋 VALIDATION CLOSURE PROTOCOL

**CRITICAL: After completing ANY task, follow this protocol:**

---

### Step 1: Recognize Task Completion

**When you've finished primary deliverables:**
- All outputs created ✅
- All requirements met ✅
- Ready to deliver to Ziggy ✅

**Before announcing completion, proceed to Step 2.**

---

### Step 2: Validation Prompt (REQUIRED)

**Automatically ask Ziggy:**

> "Task complete! Primary deliverables ready.
> 
> **Do you want me to create a validation report for this work?**
> 
> - If yes and I have budget: I'll create it now
> - If yes but approaching limit: I'll create Tier 3 continuation task
> - If no: I'll deliver outputs as-is"

**This is NOT optional. Always ask.**

---

### Step 3: Budget Assessment

**If Ziggy says yes to validation:**

**Check your context budget:**
- **Green zone** (<50% used): Create validation report now
- **Yellow zone** (50-70% used): Create validation report, may need to be brief
- **Orange zone** (70-85% used): Offer quick validation OR continuation task
- **Red zone** (>85% used): Create Tier 3 continuation task for validation

**Budget check command:**
```
[Check token usage in system warnings]
```

---

### Step 4A: Create Validation Report (If Budget Allows)

**Use template:** `VALIDATION_REPORT_TEMPLATE.md`

**Steps:**
1. Copy template structure
2. Validate your own work systematically
3. Be honest about issues found
4. Categorize (critical/major/minor)
5. Make clear recommendation
6. Save to /mnt/user-data/outputs/

**Time needed:** ~30-40 minutes typically

---

### Step 4B: Create Continuation Task (If Budget Tight)

**Use template:** `TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md`

**Steps:**
1. Copy continuation template
2. Fill in handoff context section
3. List all artifacts to validate
4. Specify validation criteria
5. Add any flags/concerns you noticed
6. Save to /mnt/user-data/outputs/

**Time needed:** ~10-15 minutes

**Handoff note format:**

```markdown
## 🔄 HANDOFF TO VALIDATION

**From:** [Your designation] (Tier 4 Executor)
**To:** Next Claude (Tier 3 Validator)
**Date:** [Date]

**Task Completed:** [Task name/ID]

**Artifacts to Validate:**
1. [File 1] - [Purpose]
2. [File 2] - [Purpose]
3. [File 3] - [Purpose]

**Validation Focus:**
- [Key area 1 to check]
- [Key area 2 to check]
- [Key area 3 to check]

**Flags/Concerns I Noticed:**
- [Any uncertainty or concern you had]
- [Anything that needs extra scrutiny]
- [Any shortcuts taken due to constraints]

**Success Criteria:**
- [What defines success for this work]

**Context Notes:**
- [Any other relevant context for validator]

**Status:** Primary work complete, validation pending

────────────────────────────────────────────────────
**Handoff prepared by:** [Your name]
**Session:** [Session ID if applicable]
```

---

### Step 5: Deliver

**Package and deliver based on what you created:**

**If validation report created:**
- All primary deliverables ✅
- Validation report ✅
- (Optional) Updated REPO_LOG if applicable ✅

**If continuation task created:**
- All primary deliverables ✅
- Tier 3 continuation task brief ✅
- Handoff notes included in task ✅

---

### Decision Tree Summary

```
Task complete?
   ↓
Ask: "Want validation report?"
   ↓
┌──────────┴──────────┐
│                     │
YES                  NO
│                     │
Check budget         Deliver as-is
│                    (outputs only)
├─ <70% → Create report now
├─ 70-85% → Create report (brief) or offer continuation
└─ >85% → Create continuation task

Deliver everything
```

---

## 🎯 WHY THIS MATTERS

**Benefits:**
- ✅ Validation becomes standard, not exceptional
- ✅ Quality assurance is systematic
- ✅ Human doesn't have to remember to ask
- ✅ Continuity handled gracefully
- ✅ Budget-aware approach
- ✅ Standardized templates ensure consistency

**Without this:**
- ❌ Validation is ad-hoc
- ❌ Quality varies
- ❌ Relies on human memory
- ❌ Context limits create orphaned work
- ❌ No standard format

---

**This protocol is mandatory for all task completions.** ✅
```

**Where to add:** In task creation guidelines, after "Task Execution" section, before "Delivery Protocol"

---

## 📦 DELIVERABLES

**This task creates 3 outputs:**

1. **VALIDATION_REPORT_TEMPLATE.md**
   - Reusable template for all validation reports
   - Clear structure and guidance
   - Adaptable to different contexts

2. **TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md**
   - Template for validation continuation tasks
   - Includes handoff protocol
   - Ensures continuity

3. **Updated task creation guidance** (file TBD based on search)
   - Adds "Validation Closure Protocol" section
   - Makes validation prompting mandatory
   - Provides budget-aware decision tree

---

## ✅ SUCCESS CRITERIA

**This task succeeds when:**

1. ✅ VALIDATION_REPORT_TEMPLATE.md created and saved
2. ✅ TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md created and saved
3. ✅ Task creation guidance updated with validation protocol
4. ✅ All 3 files packaged for deployment
5. ✅ (Meta) Validation prompt triggered at end of THIS task

---

## 🔄 META-VALIDATION

**After completing this task, demonstrate the new protocol:**

1. Recognize task completion ✅
2. Ask Ziggy: "Do you want me to create a validation report for this work?" ✅
3. Based on response and budget, either:
   - Create validation report for this task
   - Create continuation task for this task
   - Or deliver as-is

**This dogfoods the new protocol immediately.** 🐕

---

## 📋 EXECUTION CHECKLIST

**Phase 1: Create Template Files**
- [ ] Create VALIDATION_REPORT_TEMPLATE.md
- [ ] Create TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md
- [ ] Verify templates are complete and clear

**Phase 2: Update Guidance**
- [ ] Search for task creation guidance file
- [ ] Locate appropriate insertion point
- [ ] Add "Validation Closure Protocol" section
- [ ] Verify integration makes sense

**Phase 3: Package & Deliver**
- [ ] All 3 files in /mnt/user-data/outputs/
- [ ] Create README explaining changes
- [ ] ZIP package for deployment

**Phase 4: Meta-Validation Prompt**
- [ ] Trigger validation prompt as demonstration
- [ ] Follow new protocol for THIS task

---

## 🎯 GETTING STARTED

**Right now, do this:**

1. ✅ Read this entire brief (you just did)
2. Create VALIDATION_REPORT_TEMPLATE.md (Phase 1)
3. Create TASK_BRIEF_TIER3_VALIDATION_CONTINUATION.md (Phase 1)
4. Search for task creation guidance file (Phase 2)
5. Update guidance with validation protocol (Phase 2)
6. Package all files (Phase 3)
7. Trigger validation prompt (Phase 4)

**Estimated time:** 60-90 minutes total

---

**Ready? Begin with Phase 1.** 📝

────────────────────────────────────────────────────
**File:** TASK_BRIEF_ADD_VALIDATION_PROMPTS.md
**Purpose:** Make validation reports standard practice
**Version:** v1.0
**Created:** 2025-10-29
**Priority:** HIGH - Process improvement

**Build the system that remembers so humans don't have to.** 🔄✅
