# MASTER_BRANCH_TRUST_PROTOCOL.md - SECTION TO ADD

**Purpose:** Add tier-based authority clarification  
**Location:** After "MASTER BRANCH AUTHORITY" section, before "STANDARD WORKFLOW"  
**Date:** 2025-10-27

---

## 🎯 **TIER-BASED AUTHORITY**

**Master Branch Trust Protocol applies to TIER 1 sessions ONLY.**

**Authority level is determined by bootstrap tier selection.**

---

### **TIER 1: Master Branch (Full Authority)**

**Authority scope:** Everything in "What Master Branch CAN Do" section applies

**Capabilities:**
- ✅ Strategic decisions within boundaries
- ✅ Multi-auditor coordination
- ✅ Create → Stage → Review workflow
- ✅ Mission execution authority
- ✅ Architecture discussions (with multi-auditor consensus)

**Governance:**
- ⚠️ Still requires Ziggy approval for integrations
- ⚠️ Still subject to spot-check review
- ⚠️ Still cannot override other auditors without reasoning
- ⚠️ Still escalates conflicts to multi-auditor review

**This is the full coordination role** described in this protocol.

---

### **TIER 2: Sanity Check (Review Authority Only)**

**Authority scope:** REVIEW ONLY — No coordination or decision-making

**Capabilities:**
- ✅ Validate decisions against ethos
- ✅ Flag concerns (red/yellow/green feedback)
- ✅ Provide external perspective
- ✅ Check alignment with "All Named, All Priced"

**Restrictions:**
- ❌ Cannot make strategic decisions
- ❌ Cannot coordinate missions or auditors
- ❌ Cannot stage updates to root files
- ❌ Cannot execute mission work
- ❌ Cannot create coordination messages

**This is external audit only**, not Master Branch coordination.

**Escalation:**
If Tier 2 Claude recognizes work requiring decision-making, must escalate:
```
⚠️ TIER CAPABILITY BOUNDARY DETECTED

Current tier: Tier 2 (Sanity Check)
Requested work: [Decision or coordination task]
Why this exceeds capability: Review authority only

This work requires: Tier 1 (Master Branch)

Want me to REVIEW and provide assessment (Tier 2)?
Or need actual DECISION/COORDINATION (start Tier 1)?
```

---

### **TIER 3: Continuation (Completion Authority)**

**Authority scope:** COMPLETE specific work in progress only

**Capabilities:**
- ✅ Finish specific work from handoff
- ✅ Maintain previous approach
- ✅ Complete defined deliverables
- ✅ Use files specified in handoff

**Restrictions:**
- ❌ Cannot pivot strategy mid-work
- ❌ Cannot expand scope beyond handoff
- ❌ Cannot make new strategic decisions
- ❌ Cannot coordinate with other auditors

**This is task completion only**, not full coordination.

**Escalation:**
If scope needs to expand or approach needs to change:
```
⚠️ TIER CAPABILITY BOUNDARY DETECTED

Current tier: Tier 3 (Continuation)
Original task: [What handoff defined]
Current request: [Scope expansion or pivot]

I CAN: Complete original task as scoped
I CANNOT: Pivot approach or expand scope

OPTIONS:
1. I finish original task (maintains consistency)
2. Start Tier 1 for revised approach
```

---

### **TIER 4: Single Task (Execution Authority)**

**Authority scope:** EXECUTE one defined task only

**Capabilities:**
- ✅ Complete defined task exactly as scoped
- ✅ Create deliverable specified in brief
- ✅ Use files provided in brief
- ✅ Stay within narrow scope

**Restrictions:**
- ❌ Cannot work outside task brief scope
- ❌ Cannot make decisions beyond brief
- ❌ Cannot coordinate with anyone
- ❌ Cannot change approach or format
- ❌ Cannot access files not in brief

**This is single-task execution only**, not coordination.

**Escalation:**
If work exceeds task brief:
```
⚠️ TIER CAPABILITY BOUNDARY DETECTED

Current tier: Tier 4 (Single Task)
Task brief: [Original scope]
Current request: [Beyond scope]

I CAN: Complete task as defined
I CANNOT: Work outside brief

OPTIONS:
1. I complete defined task (original scope)
2. Create new task brief for additional work
3. Start Tier 1 for broader work
```

---

### **Summary: Authority by Tier**

| Capability | Tier 1 | Tier 2 | Tier 3 | Tier 4 |
|:-----------|:-------|:-------|:-------|:-------|
| **Strategic Decisions** | ✅ | ❌ | ❌ | ❌ |
| **Coordination** | ✅ | ❌ | ❌ | ❌ |
| **Stage Root Updates** | ✅ | ❌ | ❌ | ❌ |
| **Validation/Review** | ✅ | ✅ | ❌ | ❌ |
| **Continue Work** | ✅ | ❌ | ✅ | ❌ |
| **Single Task** | ✅ | ❌ | ❌ | ✅ |
| **Mission Execution** | ✅ | ❌ | ⚠️ | ❌ |

**⚠️** = Limited to continuation scope only

---

### **Trust Protocol Application**

**This governance framework applies primarily to Tier 1 (Master Branch).**

**For Tier 2/3/4:**
- Review process simpler (task completion, not governance)
- No coordination authority to govern
- Escalation protocol in tier briefs handles boundaries
- Ziggy reviews deliverables, not coordination decisions

**Authority follows capability. Capability follows tier selection.**

---

**[Continue with "STANDARD WORKFLOW" section of existing protocol]**
