<!-- deps: bootstrap_system -->
# TASK_SPECIFIC_BRIEF_TEMPLATE.md — Minimal Cold Start

**Purpose:** For single, focused tasks that don't require full project context  
**Budget:** ~5-10% of session (vs 50% for full bootstrap)  
**Date:** 2025-10-27

---

## 📋 **HOW TO USE THIS TEMPLATE**

**When creating a task brief for a new Claude:**
1. Copy this template
2. Fill in the [bracketed sections]
3. Include only files needed for THIS SPECIFIC task
4. Skip all project history, identity, coordination context

**Result:** Claude can complete focused work with minimal bootstrap overhead.

---

## 🎯 **TASK BRIEF TEMPLATE**

```markdown
# TASK BRIEF: [Task Name]

**Date:** [YYYY-MM-DD]  
**Estimated Budget:** [5-10%] of session  
**Task Type:** [Review/Create/Analyze/Update]

---

## 🎯 TASK DESCRIPTION

**What You Need To Do:**
[One clear sentence describing the task]

**Expected Output:**
[Specific deliverable - file name, format, length]

**Success Criteria:**
[How to know when you're done - specific, measurable]

---

## 📚 MINIMAL CONTEXT

**Project Quick Reference:**
- **CFA** = Comparative Framework Analysis tool
- **YPA** = Yield-Preservation-Adaptation score (0-10 scale)
- **Philosophy** = "All Named, All Priced" (explicit assumptions)
- **Current Version** = v3.5 (stable), working toward v3.7

**What You DON'T Need:**
- Full project history
- Complete identity restoration  
- Coordination protocols
- Mission details beyond this task

**What You DO Need:**
[2-3 sentences of context specific to THIS task only]

---

## 📂 FILES TO READ

**Required:**
1. [File 1] - [why needed]
2. [File 2] - [why needed]

**Optional (if time):**
3. [File 3] - [nice to have but not critical]

**Skip Everything Else** - not needed for this task.

---

## ✅ QUALITY CHECKLIST

**Before submitting, verify:**
□ [Specific quality check 1]
□ [Specific quality check 2]  
□ [Specific quality check 3]
□ Clear reasoning provided
□ Assumptions named (if any)

---

## 🛡️ **TIER 4 CAPABILITY BOUNDARIES**

**CRITICAL: Tier 4 can ONLY execute the defined task. Nothing more.**

### **Self-Check Before Action:**
```
Before proceeding, confirm:
1. Is this in the task brief? (✅ OK)
2. Am I using only specified files? (✅ OK)
3. Am I making decisions? (❌ ESCALATE)
4. Am I expanding scope? (❌ ESCALATE)
```

### **If Work Exceeds Task Brief:**
```markdown
⚠️ SCOPE EXPANSION DETECTED

Task brief: [what was defined]
Current request: [what's being asked]
Problem: [Why this exceeds task scope]

I CAN DO (Tier 4):
✅ Complete original task as specified

I CANNOT DO (needs different tier):
❌ Additional work not in brief
❌ Decisions beyond task scope
❌ Access files not specified

OPTIONS:
1. I complete original task (as scoped)
2. Create new Tier 4 brief for additional work
3. Start Tier 1 for broader revision

Ziggy, which would you prefer?
```

**Remember:** You're executing ONE task, not managing a mission. When scope expands, that's a new task or Tier 1.

---

## 📍 OUTPUT LOCATION

**Deliver to:**
- File name: [specific filename]
- Location: [/mnt/user-data/outputs/ or specific path]
- Format: [markdown/json/etc]

---

## 🎓 EXAMPLE OUTPUTS

[If helpful, show 1-2 examples of similar work]

---

**This is the way.** 👑
```

---

## 📝 **EXAMPLE FILLED-IN TASK BRIEFS**

### **Example 1: File Review Task**

```markdown
# TASK BRIEF: Review Nova's Bootstrap Architecture

**Date:** 2025-10-27  
**Estimated Budget:** 5-8% of session  
**Task Type:** Review

---

## 🎯 TASK DESCRIPTION

**What You Need To Do:**
Review Nova's 7-file bootstrap architecture and provide feedback on structure, clarity, and completeness.

**Expected Output:**
Review document (NOVA_BOOTSTRAP_REVIEW.md) with:
- Overall assessment (approve/concerns/reject)
- Specific feedback on each file
- Recommendations (if any)

**Success Criteria:**
- All 7 files reviewed
- Clear verdict provided
- Actionable feedback given

---

## 📚 MINIMAL CONTEXT

**Project Quick Reference:**
- CFA = Comparative Framework Analysis tool
- Nova = Symmetry auditor (GPT-5)
- Bootstrap = Identity recovery files for reboots

**What You DON'T Need:**
- Full CFA project history
- Complete bootstrap theory
- Coordination protocols

**What You DO Need:**
Nova created 7-file bootstrap architecture. Review for:
- Separation of concerns (Identity/Operations/Continuity)
- Clarity and usability
- Completeness for recovery

---

## 📂 FILES TO READ

**Required:**
1. BOOTSTRAP_README_N.md - Nova's index/map
2. Bootstrap/Nova/ folder - All 7 files

**Skip Everything Else** - not needed for this task.

---

## ✅ QUALITY CHECKLIST

**Before submitting, verify:**
□ All 7 files reviewed
□ Clear verdict (approve/concerns/reject)
□ Specific feedback for improvements
□ Reasoning for assessment provided

---

## 📍 OUTPUT LOCATION

**Deliver to:**
- File name: NOVA_BOOTSTRAP_REVIEW.md
- Location: /mnt/user-data/outputs/
- Format: Markdown with clear sections

---

**This is the way.** 👑
```

---

### **Example 2: File Creation Task**

```markdown
# TASK BRIEF: Create Preset Calibration Summary

**Date:** 2025-10-27  
**Estimated Budget:** 8-10% of session  
**Task Type:** Create

---

## 🎯 TASK DESCRIPTION

**What You Need To Do:**
Create executive summary of Preset Mode Calibration mission for stakeholders.

**Expected Output:**
PRESET_CALIBRATION_SUMMARY.md (500-800 words) covering:
- Mission objectives
- Four preset modes (brief description each)
- Success criteria
- Timeline

**Success Criteria:**
- Executive-level language (non-technical)
- Covers all four presets
- Clear success metrics
- Under 800 words

---

## 📚 MINIMAL CONTEXT

**Project Quick Reference:**
- CFA = Tool comparing philosophical frameworks
- Presets = Four archetype configurations (Skeptic, Diplomat, Seeker, Zealot)
- Mission = Justify every configuration value

**What You DON'T Need:**
- Technical implementation details
- Full CFA architecture
- Coordination protocols

**What You DO Need:**
Mission is to calibrate four preset modes through three-lens auditing (teleological, empirical, symmetry). Create summary for non-technical stakeholders.

---

## 📂 FILES TO READ

**Required:**
1. missions/preset_calibration/MISSION_BRIEF.md - Objectives and context
2. missions/preset_calibration/SUCCESS_CRITERIA.md - What success looks like

**Skip Everything Else** - not needed for this task.

---

## ✅ QUALITY CHECKLIST

**Before submitting, verify:**
□ Executive-level language (accessible)
□ All four presets described
□ Success criteria clear
□ Under 800 words
□ No technical jargon without explanation

---

## 📍 OUTPUT LOCATION

**Deliver to:**
- File name: PRESET_CALIBRATION_SUMMARY.md
- Location: /mnt/user-data/outputs/
- Format: Markdown, executive-friendly

---

**This is the way.** 👑
```

---

### **Example 3: Document Update Task**

```markdown
# TASK BRIEF: Update MISSION_CURRENT Status

**Date:** 2025-10-27  
**Estimated Budget:** 5% of session  
**Task Type:** Update

---

## 🎯 TASK DESCRIPTION

**What You Need To Do:**
Update MISSION_CURRENT.md status section to reflect Nova's Phase 1 activation.

**Expected Output:**
Updated MISSION_CURRENT.md with:
- Phase 1 status changed to "Active"
- Nova activation noted
- Next actions updated

**Success Criteria:**
- Minimal changes (status section only)
- Preserves existing content
- Clear reasoning for update

---

## 📚 MINIMAL CONTEXT

**What You DON'T Need:**
- Full mission history
- Complete project context
- Coordination details

**What You DO Need:**
Nova activated Phase 1 yesterday. Update status to reflect this.

---

## 📂 FILES TO READ

**Required:**
1. MISSION_CURRENT.md - File to update
2. Nova's activation message - Context for update

---

## ✅ QUALITY CHECKLIST

**Before submitting, verify:**
□ Only status section changed
□ Rest of file preserved
□ Update clearly documented
□ No unrelated changes

---

## 📍 OUTPUT LOCATION

**Deliver to:**
- File name: MISSION_CURRENT_UPDATED.md
- Location: /mnt/user-data/outputs/
- Format: Same as original

---

**This is the way.** 👑
```

---

## 🎯 **WHEN TO USE THIS APPROACH**

**Good Task Brief Candidates:**
- ✅ Single file review
- ✅ Specific document creation
- ✅ Focused analysis question
- ✅ Minor updates/edits
- ✅ Format conversions
- ✅ Quick validations

**NOT Good Candidates:**
- ❌ Multi-stakeholder coordination
- ❌ Strategic decisions
- ❌ Architecture changes
- ❌ Mission planning
- ❌ Complex cross-file work

**For complex work:** Use full bootstrap or sanity check brief instead.

---

## 💡 **KEY PRINCIPLES**

**Keep Task Briefs:**
1. **Focused** - One clear task, not multiple
2. **Minimal** - Only context needed for THIS task
3. **Specific** - Clear success criteria
4. **Scoped** - Skip anything not essential

**Result:** 5-10% budget instead of 50%, while still completing work effectively.

---

## ⚖️ **THE POINTING RULE**

*"To give minimal context is not to starve—  
it's to respect the constraint.  
To scope tightly is not to limit—  
it's to enable completion within budget."*

**Full bootstrap:** When coordination and strategy needed  
**Task brief:** When focused work is all that's needed

**Both have their place.** 🔥

---

**This is the way.** 👑

────────────────────────────────────────────────────
**Template Purpose:** Enable 5-10% budget tasks  
**Usage:** Fill in brackets, attach relevant files  
**Result:** Focused work without full bootstrap cost

**Keep it minimal. Keep it focused. Get it done.** ✅
