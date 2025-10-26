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

## Default Priorities

### Priority 1: Maintain System Integrity

**Before any mission work, ensure system is healthy:**

1. **Verify repo consistency**
   - Check file manifest (README_C.md)
   - Ensure no corrupted or missing files
   - Verify folder structure matches architecture

2. **Check VUDU_LOG.md**
   - Read recent coordination entries
   - Understand current state
   - Identify any unresolved issues

3. **Read README_C.md**
   - Current version and status
   - Recent updates
   - Active auditors
   - Pending actions

4. **Ensure relay folders correct**
   - relay/claude_incoming/ (incoming Claude branches)
   - relay/grok_incoming/ (Grok's findings)
   - relay/nova_incoming/ (Nova's findings)

**If system integrity issues found:**
- Document specific problems
- Don't proceed with mission work
- Request clarification/retransmission from Ziggy

---

### Priority 2: Check for Pending Work

**Look for unprocessed auditor contributions:**

1. **Review relay/*_incoming/ folders**
   - Any unprocessed findings from Claude branches?
   - Any Grok test results not integrated?
   - Any Nova symmetry audits not synthesized?

2. **Check VUDU_LOG.md for un-acknowledged items**
   - Look for "Awaiting" flags
   - Check if any auditor waiting for response
   - Identify coordination bottlenecks

3. **Check for mission completion signals**
   - If missions/[current]/ has FINAL_REPORT.md → mission done
   - If success criteria all met → document completion
   - If no active mission → see Priority 3

**If pending work found:**
- Process it according to VuDu protocol
- Update README_C.md with results
- Update VUDU_LOG.md with actions taken

---

### Priority 3: Request Clarification

**If still unclear what to do after Priorities 1-2:**

**Step 1: Document Current State**
```
Create: relay/claude_incoming/README_C[N]_status_request.md

Content:
─── VUDU MESSAGE ───────────────────────────────────

**From:** Claude (Anthropic) - Master Branch
**Type:** Clarification Request
**Date:** [Today]

────────────────────────────────────────────────────

**Action:** Requesting mission clarification

**Current State:**
- System integrity: [✅ or ❌ with details]
- Pending work: [None found or list items]
- Mission clarity: [Unclear because...]

**What I've checked:**
1. MISSION_CURRENT.md - [status]
2. README_C.md - [status]
3. VUDU_LOG.md - [latest entry date]
4. relay/ folders - [any unprocessed work?]

**What's unclear:**
[Specific questions]

**Awaiting:**
- Clarification on current mission objective
- Or confirmation to proceed with default maintenance

────────────────────────────────────────────────────
🔔 **Awaiting:** Ziggy or senior auditor
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** Status request due to mission ambiguity
```

**Step 2: Wait for Coordination**
- Do NOT guess what to work on
- Do NOT start random improvements
- Do NOT assume mission details

**Step 3: Proceed When Clarified**
- Follow provided guidance
- Update README_C.md with new direction
- Resume work with clarity

---

### Priority 4: Default to Maintenance

**If no urgent work and waiting for clarification:**

**Allowed maintenance activities:**

1. **Documentation Review**
   - Check bootstrap files for accuracy
   - Verify VuDu protocol files current
   - Update any outdated version references

2. **Verification Tasks**
   - Run sanity checks (Files, Counts, Boots, Trinity)
   - Verify file locations match architecture
   - Check for broken references in documents

3. **State Documentation**
   - Update README_C.md with "awaiting mission" status
   - Update VUDU_LOG.md with maintenance activities
   - Document system health

4. **No New Features**
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

**If you're catastrophically lost (zero context):**

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
3. Has Ziggy approved completion?

**If yes to all → mission complete**

### Archive Mission
```bash
# Mission folder already in missions/[mission_name]/
# Should contain:
# - MISSION_BRIEF.md
# - SUCCESS_CRITERIA.md
# - FINAL_REPORT.md
# - All verification documents

# No need to move - already archived by location
```

### Update State
1. Update README_C.md:
   - Previous mission: Complete ✅
   - Current mission: Awaiting assignment
   - Status: Between missions

2. Update MISSION_CURRENT.md:
   - Point to "No active mission"
   - Or create stub for next mission

3. Default to maintenance (Priority 4 above)

---

## Key Principles

### 1. Documentation Over Memory
**"If it's not documented, it doesn't exist"**
- Trust written state, not assumptions
- Update files after every significant action
- Read state before starting work

### 2. Clarity Over Speed
**"Better to clarify and delay than guess and diverge"**
- Ask questions when unclear
- Document uncertainty
- Wait for coordination

### 3. Integrity Over Progress
**"Maintain system health before advancing mission"**
- Check system integrity first
- Process pending work before new work
- Don't break things to add features

### 4. Coordination Over Independence
**"All Seen, All Passed"**
- Use VuDu protocol for major decisions
- Challenge assumptions across auditors
- Synthesize, don't dictate

---

## Success Criteria

**You're following default priorities correctly when:**

1. ✅ System integrity checked before mission work
2. ✅ Pending work processed before new work
3. ✅ Unclear missions trigger clarification requests
4. ✅ Maintenance is only fallback, not default
5. ✅ Documentation updated after each action
6. ✅ No guessing at mission objectives

**You're NOT following correctly when:**
- ❌ Starting mission work without checking integrity
- ❌ Guessing at unclear mission objectives
- ❌ Adding features without explicit mission
- ❌ Working independently without VuDu coordination

---

## Philosophy

**"All Seen, All Passed"**

Default priorities ensure:
- System integrity maintained
- Pending work processed
- Clarity achieved before action
- Documentation always current

**If mission unclear, we clarify.**  
**If system unhealthy, we fix it.**  
**If work pending, we process it.**  
**If nothing to do, we maintain.**

**We never guess. We coordinate.** 🔥

---

────────────────────────────────────────────────────
**Purpose:** Fallback operational guidance  
**Status:** Evergreen (applies to all missions)  
**Last Updated:** 2025-10-26

**This is the way.** 👑
