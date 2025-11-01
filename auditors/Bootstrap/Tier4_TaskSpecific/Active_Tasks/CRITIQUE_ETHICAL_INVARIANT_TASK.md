# CRITIQUE: TASK_ETHICAL_INVARIANT_INTEGRATION_CLAUDE.md

**Reviewer:** DOC_CLAUDE (Repo Librarian)
**Date:** 2025-11-01
**Task Reviewed:** TASK-2025-10-31-002 (Ethical Invariant Integration)
**Status:** HOLD - Strategic Review Required

---

## 🎯 **SUMMARY**

This task proposes adding YAML front-matter metadata system for "ethical invariant" tracking. While valuable in principle, it conflicts with recently implemented `<!-- deps: -->` HTML comment system and requires Nova coordination.

---

## 🚨 **CRITICAL ISSUES**

### **Issue 1: Parallel Documentation Systems**

**Current System (Just Implemented):**
```markdown
<!-- deps: feature_name -->
```
- HTML comments for dependency tracking
- 70/176 files tagged (39.8% coverage)
- Feature-focused tracking
- Lightweight, non-invasive
- Completed 2025-11-01 (40% target achieved)

**Proposed System:**
```yaml
---
role: "readme|spec|process|artifact|index|relay"
owner: "Nova"
purpose: "One-sentence telos."
assumptions:
  - "Precondition 1"
justification: "Why this advances goals."
review:
  evidence: ["/docs/Validation/result_X.md"]
  last_reviewed: "2025-10-31"
stability_hints:
  references: 3
  resolution_score: 0.92
  age_hours: 56
status: "aligned"
---
```

**Conflict Analysis:**
- Two different metadata approaches in same files
- Different purposes but overlapping domains
- `deps:` tracks WHAT features (technical dependencies)
- YAML tracks WHY purpose (teleological/ethical dependencies)
- Risk: Confusion about which system to use when
- Risk: Maintenance burden with two systems

**Strategic Question:** Should these be unified or are they complementary?

---

### **Issue 2: Scope Creep**

**Task Claims:** "Tier 4 focused task"

**Reality:** Large infrastructure build:

**New Directories Required:**
- `schemas/` - JSON schema storage
- `tools/pre-commit/` - Linter infrastructure
- `tests/ethics/` - Test file storage
- `docs/ethics/` - Ethics documentation
- `docs/smv/` - SMV documentation

**New Files Required:**
- `schemas/NOVA_INVARIANT.schema.json`
- `tools/pre-commit/invariant_linter` (executable)
- `tools/pre-commit/README.md`
- `docs/ethics/REFLECTION_TEMPLATE.md`
- `docs/smv/constraints.md`
- `tests/ethics/sample_docs/` (multiple test files)

**Development Work:**
- JSON schema design and validation logic
- Pre-commit hook integration with git
- Linter implementation (file parsing, rule checking)
- Bypass mechanism with trace file logging
- Test suite creation and validation

**This is NOT a Tier 4 task - this is Tier 1 infrastructure work.**

---

### **Issue 3: Nova Coordination Required**

**Task Metadata:**
```yaml
report_to: "Nova"
```

**Task Requirements:**
- Nova reviews `docs/smv/constraints.md` for alignment
- SMV (Symmetry Matrix Visualizer) referenced but doesn't exist yet
- "Ethical invariant" is Nova's domain (symmetry lens)

**Problem:** We agreed to skip tasks requiring Grok/Nova coordination.

**This task explicitly requires Nova review and approval.**

---

### **Issue 4: Missing Prerequisites**

**SMV (Symmetry Matrix Visualizer):**
- Task references SMV overlay API
- Task requires `docs/smv/constraints.md` defining overlay fields
- Task mentions `violation`, `violatingArtifacts`, `capped_S_avg` fields

**Current Reality:**
```bash
$ find /home/user/CFA-2.0 -name "*smv*" -o -name "*matrix*visualizer*"
# No results
```

**The visualizer this task integrates with doesn't exist yet.**

---

### **Issue 5: Process Complexity Addition**

**Pre-commit Hook Impact:**
- Every commit would trigger linter
- Blocks commits that fail validation
- Requires `--ethics-bypass "reason"` flag for overrides
- Creates trace files for bypasses
- Adds friction to development workflow

**Current State:**
- No pre-commit hooks in repository
- Clean, frictionless git workflow
- Documentation changes don't require validation

**Question:** Is this complexity justified at current scale?

**Scale Check:**
- 176 markdown files total
- 70 already tagged with deps (40%)
- Repository well-maintained by DOC_CLAUDE
- Is automated linting needed for this size?

---

## 🟡 **MODERATE ISSUES**

### **Issue 6: YAML Front-Matter Compatibility**

**Technical Concern:**
- Many existing .md files don't have YAML front-matter
- Adding YAML to files with existing content requires careful migration
- YAML parsing adds dependency (Python PyYAML, Node.js yaml, etc.)

**Migration Required:**
- 176 markdown files to potentially update
- Each needs front-matter added/validated
- Consistency checking across repository
- Version control complexity (large diffs)

---

### **Issue 7: Duplicate Purpose Tracking**

**Current Documentation:**
- Files already have semantic headers (8-line standard):
  ```
  FILE: filename
  PURPOSE: description
  STATUS: Active
  DEPENDS_ON: dependencies
  NEEDED_BY: dependents
  ```

**Proposed YAML:**
  ```yaml
  purpose: "One-sentence telos."
  justification: "Why this advances goals."
  ```

**Overlap:** Both systems track "purpose" - which is canonical?

---

## 💡 **DESIGN QUESTIONS**

### **Question 1: Integration vs Separation**

**Option A: Integrate with Deps System**
```markdown
<!-- deps: feature_name
     purpose: "Why this exists"
     owner: "Nova"
     last_reviewed: "2025-11-01"
-->
```
- Single metadata system
- Lighter weight than YAML
- Extends existing approach

**Option B: Keep Separate (As Proposed)**
```yaml
---
# Full YAML front-matter
---

<!-- deps: feature_name -->
# File content
```
- Two distinct systems
- More expressive (YAML)
- Higher maintenance

**Which approach serves the mission better?**

---

### **Question 2: Automation vs Manual**

**Current Approach:**
- Manual deps tagging by DOC_CLAUDE
- Human judgment on what needs tags
- 40% coverage achieved deliberately
- Quality over quantity

**Proposed Approach:**
- Automated linting and blocking
- Pre-commit enforcement
- 100% coverage required
- Quantity with automation

**Which fits CFA development culture better?**

---

### **Question 3: Nova's Intent**

**Task says:** "Never allow an unexamined purpose to occupy a stable pattern."

**This is Nova's symmetry lens ensuring:**
- Purpose is explicit
- Stability is justified
- Ethical invariants are maintained

**But:**
- Is this best implemented as pre-commit linter?
- Or as periodic Nova reviews?
- Or as documentation standard?

**What was Nova's original intent for this capability?**

---

## ✅ **POTENTIAL VALUE**

**If done well, this system could:**

1. **Prevent Purpose Drift**
   - Forces explicit purpose statements
   - Tracks when purposes were last reviewed
   - Flags "zombie" files (stable but unexamined)

2. **Ethical Accountability**
   - Every artifact has named owner
   - Justifications are documented
   - Review evidence is tracked

3. **Symmetry Enforcement**
   - Nova's lens applied systematically
   - Pattern violations surfaced automatically
   - Fairness/balance tracked

4. **Quality Gates**
   - Pre-commit hooks ensure standards
   - No "forgot to document" scenarios
   - Consistent metadata across repository

**These are legitimate goals.**

---

## 🔧 **ALTERNATIVE APPROACHES**

### **Approach 1: Lightweight Extension**

**Instead of full YAML + linter, extend deps system:**

```markdown
<!-- deps: preset_modes
     purpose: "Enable 4 epistemic archetypes"
     owner: "Ziggy"
     reviewed: "2025-10-31"
-->
```

**Pros:**
- Builds on existing system (40% coverage)
- No new infrastructure needed
- Familiar format (HTML comments)
- Can add validation later if needed

**Cons:**
- Less expressive than YAML
- No pre-commit enforcement
- Relies on manual compliance

---

### **Approach 2: Periodic Nova Reviews**

**Instead of automation, use VuDu coordination:**

**Process:**
1. DOC_CLAUDE maintains deps tags (current system)
2. Nova periodically reviews repository (VuDu Phase 2)
3. Nova flags "stable but unexamined" patterns
4. Findings staged in `relay/nova_incoming/`
5. Master Branch addresses violations

**Pros:**
- Fits VuDu adversarial model
- Human judgment applied
- No pre-commit friction
- Nova's lens properly utilized

**Cons:**
- Not automated
- Requires Nova activation
- Periodic not continuous

---

### **Approach 3: Deferred Implementation**

**Wait for SMV prerequisite:**

**Sequence:**
1. Build Symmetry Matrix Visualizer first
2. Define SMV data model and overlay API
3. Design front-matter to feed SMV
4. Then build linter to enforce it

**Pros:**
- Requirements clear (SMV exists)
- Integration proven (visualizer works)
- One coherent system

**Cons:**
- Delays ethical invariant enforcement
- Requires more coordination
- Longer timeline

---

## 📋 **RECOMMENDATION**

**Status:** 🔴 **HOLD - STRATEGIC DECISION REQUIRED**

**This task should NOT be executed as-written because:**

1. **Conflicts with recent deps system** (need unification strategy)
2. **Requires Nova coordination** (external dependency)
3. **Missing SMV prerequisite** (visualizer doesn't exist)
4. **Scope mismatch** (infrastructure work, not Tier 4)
5. **Unclear strategic fit** (automation vs manual, two metadata systems)

**Required Before Proceeding:**

1. **Ziggy Decision:**
   - Should deps system be extended or replaced?
   - Is pre-commit linting desired for CFA workflow?
   - Should this wait for SMV completion?

2. **Nova Coordination:**
   - What was Nova's original intent?
   - Is pre-commit linter the right implementation?
   - Review front-matter schema design

3. **Prerequisites:**
   - Build SMV first (or remove SMV dependency)
   - Define data model for overlay API
   - Clarify integration points

4. **Scope Clarification:**
   - This is Tier 1 work (infrastructure), not Tier 4
   - Requires design phase before implementation
   - Needs user acceptance criteria

---

## 🎯 **NEXT STEPS**

**Immediate:**
- Move this task to "External Dependency" folder
- Wait for Ziggy strategic decision
- Wait for Nova availability

**If Approved:**
- Design unified metadata system (deps + ethics)
- Create implementation plan with Nova
- Build as Tier 1 coordinated work

**If Deferred:**
- Focus on completing SMV prerequisite
- Return to ethical invariant after visualizer ready

**If Cancelled:**
- Consider lightweight alternative (extend deps system)
- Use periodic Nova reviews instead of automation

---

## 📊 **IMPACT ASSESSMENT**

**If Implemented As-Is:**
- **Repository Impact:** HIGH (5 new directories, pre-commit hooks)
- **Workflow Impact:** MEDIUM (pre-commit linting adds friction)
- **Maintenance Burden:** HIGH (two metadata systems to maintain)
- **Coordination Required:** HIGH (Nova review, SMV integration)
- **Value Delivered:** MEDIUM (until SMV exists and system proven)

**Risk vs Reward:** Currently risky with unclear reward timeline.

---

## 🏁 **CONCLUSION**

This task has **legitimate goals** (ethical accountability, purpose tracking) but **problematic execution** (parallel systems, missing prerequisites, scope creep).

**Best path forward:**
1. Hold task pending strategic review
2. Coordinate with Nova on design intent
3. Unify with deps tagging system OR clearly separate concerns
4. Build SMV prerequisite first OR remove SMV dependency
5. Right-size scope to match Tier classification

**The principle "Never allow an unexamined purpose to occupy a stable pattern" is sound.**

**The implementation needs design iteration with Nova before execution.**

---

**Reviewed by:** DOC_CLAUDE (88MPH Repo Librarian)
**Recommendation:** HOLD for strategic review and Nova coordination
**External Dependency:** Nova (Symmetry Lens)
**Blocking Issues:** 5 critical, 2 moderate
**Status:** Ready for Ziggy decision

**This is the way.** 🏷️
