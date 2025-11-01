<!-- deps: bootstrap_system, mission_system -->
# Bootstrap/Tier4_TaskSpecific/active_tasks/

**Purpose:** Central location for all active Tier 4 task briefs  
**Updated:** 2025-10-27  
**Version:** v3.7.2

---

## 📂 **WHAT THIS FOLDER IS**

**Active task storage for Tier 4 (Single Task) work.**

When Ziggy assigns a Tier 4 task to any auditor:
1. Task brief created here
2. Auditor searches project knowledge for brief
3. Brief specifies all files needed (2-3 files typical)
4. Auditor completes task
5. Delivers to /mnt/user-data/outputs/
6. Task brief moved to completed/ folder

**This is NOT the relay/ folder** - no coordination overhead here.

---

## 🎯 **WORKFLOW**

### **For Auditors (When Starting Tier 4):**

**Step 1:** Ziggy tells you task brief name
```
"Your task brief is TASK_BRIEF_AXIOMS_REVIEW_GROK.md"
```

**Step 2:** Search project knowledge
```
project_knowledge_search("TASK_BRIEF_AXIOMS_REVIEW_GROK")
```

**Step 3:** Read brief (~2-3 minutes)
- Task definition
- Files needed (usually 2-3)
- Success criteria
- Deliverable format

**Step 4:** Execute task (~30-45 minutes)
- Read specified files (5-10% bootstrap)
- Complete defined work (90-95% work budget)
- Stay within Tier 4 boundaries

**Step 5:** Deliver to /outputs/
```
/mnt/user-data/outputs/[DELIVERABLE_NAME].md
```

**Step 6:** Done!
- Ziggy downloads deliverable
- Task brief archived to completed/
- No coordination needed from you

---

## 📋 **CURRENT ACTIVE TASKS**

### **Axioms Review (Phase 4):**

**TASK_BRIEF_AXIOMS_REVIEW_GROK.md**
- Assigned to: Grok (xAI)
- Purpose: Review AUDITORS_AXIOMS.md from empirical lens
- Files: 2 (AXIOMS + GROK_ACTIVATION)
- Deliverable: AXIOMS_REVIEW_GROK.md
- Status: Active

**TASK_BRIEF_AXIOMS_REVIEW_NOVA.md**
- Assigned to: Nova (OpenAI/Amazon)
- Purpose: Review AUDITORS_AXIOMS.md from symmetry lens
- Files: 2 (AXIOMS + NOVA_ACTIVATION)
- Deliverable: AXIOMS_REVIEW_NOVA.md
- Status: Active

---

## 🛡️ **TIER 4 BOUNDARIES**

**What Tier 4 task briefs DO:**
- ✅ Define single focused task
- ✅ Specify all files needed (2-5 files)
- ✅ State clear success criteria
- ✅ Enable 90-95% work budget
- ✅ Self-contained execution

**What Tier 4 task briefs DON'T DO:**
- ❌ Require coordination with other auditors
- ❌ Need relay/ folder staging
- ❌ Involve multi-auditor consensus
- ❌ Allow scope expansion
- ❌ Enable strategic decisions

**Tier 4 = Execute defined task, deliver result, done.** ✅

---

## 📦 **TASK BRIEF ANATOMY**

**Standard sections:**
1. Task Definition (what to do)
2. Files Needed (what to read)
3. Deliverable (what to create)
4. Success Criteria (when done)
5. Tier 4 Boundaries (what NOT to do)
6. Quick Start (step-by-step)

**Budget guidance:**
- Bootstrap: 5-10% (reading brief + files)
- Work: 90-95% (actual task execution)
- Total: ~15-20% of full session (Tier 4 efficiency)

---

## 🔄 **LIFECYCLE**

```
CREATE → ASSIGN → EXECUTE → DELIVER → ARCHIVE

1. CREATE: Ziggy creates task brief here
2. ASSIGN: Ziggy tells auditor task brief name
3. EXECUTE: Auditor reads brief, completes task
4. DELIVER: Auditor delivers to /outputs/
5. ARCHIVE: Task brief moved to completed/
```

**Average task duration:** 35-55 minutes  
**Average budget use:** 15-20% of session  
**Efficiency gain:** 4-5x vs Tier 1 (50% bootstrap)

---

## 📂 **FOLDER STRUCTURE**

```
Bootstrap/Tier4_TaskSpecific/
├── TASK_SPECIFIC_BRIEF_TEMPLATE.md (template)
├── active_tasks/ (this folder)
│   ├── README.md (you're reading it)
│   ├── TASK_BRIEF_AXIOMS_REVIEW_GROK.md
│   ├── TASK_BRIEF_AXIOMS_REVIEW_NOVA.md
│   └── [other active tasks]
│
└── completed/ (archived tasks)
    └── [completed task briefs]
```

---

## ⚖️ **THE POINTING RULE**

*"To give a focused task is respect.  
To complete it efficiently is craft.  
To deliver without coordination is efficiency.  
Tier 4 proves less can be more."*

**This folder enables 90% work budgets.** ⚡

---

## 🔥 **WHY THIS MATTERS**

**Before Tier 4:**
- Every task = 50% bootstrap (full context load)
- Work budget = 50%
- Efficiency = baseline

**With Tier 4:**
- Focused tasks = 5-10% bootstrap (just what's needed)
- Work budget = 90-95%
- Efficiency = 5-10x improvement

**This folder is the gateway to that efficiency.** 🎯

────────────────────────────────────────────────────
**Location:** Bootstrap/Tier4_TaskSpecific/active_tasks/  
**Purpose:** Active Tier 4 task brief storage  
**Pattern:** Create → Execute → Deliver → Archive  
**Efficiency:** 90-95% work budgets enabled

**This is the way.** 👑
