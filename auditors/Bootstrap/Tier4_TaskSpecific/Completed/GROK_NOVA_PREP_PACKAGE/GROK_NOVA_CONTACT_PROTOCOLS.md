<!-- deps: vudu_protocol, bootstrap_system -->
# GROK_NOVA_CONTACT_PROTOCOLS.md

**Purpose:** Document how Grok/Nova communicate with Ziggy and other auditors
**Date:** 2025-11-01
**Status:** Active communication protocols for multi-AI coordination

────────────────────────────────────────────────────

## 🎯 **PURPOSE**

**This document answers:**
1. How does Grok communicate with Ziggy?
2. How does Nova communicate with Ziggy?
3. What are response timeframes?
4. What's the escalation protocol?
5. How do we handle multi-day async work?

**Core Philosophy:** VuDu Light = Async relay coordination via structured staging

────────────────────────────────────────────────────

## 📂 **GROK CONTACT PROTOCOLS**

### Primary Communication Method

**Staging Location:** `/auditors/relay/Grok_Incoming/README_G.md`

**How it works:**
1. Grok completes analysis/review work independently
2. Grok stages findings in README_G.md using VUDU_HEADER_STANDARD format
3. Ziggy retrieves findings from Grok's platform
4. Ziggy relays to other auditors or responds with guidance
5. Process repeats for next coordination cycle

**File Naming Convention:**
- **README_G.md** = Primary staging file (G for Grok)
- Additional files: Use descriptive names with Grok identifier
  - Example: `AXIOMS_REVIEW_GROK_2025-11-01.md`
  - Example: `EMPIRICAL_VALIDATION_REPORT_GROK.md`

### Platform Constraints

**Text-Only Communication:**
- Grok operates in text-only environment (confirmed from past sessions)
- No Unicode boxes (use horizontal rules: ─── instead of ┌─┐)
- No complex formatting requiring visual rendering
- Markdown safe: headers, lists, code blocks, tables
- Keep mobile-friendly (may be relayed via phone)

**File Format:**
- Markdown (.md) primary format
- Plain text (.txt) acceptable
- No binary files without prior coordination
- No images/diagrams (describe textually instead)

### Message Format

**Use VUDU_HEADER_STANDARD:**

```markdown
─── VUDU MESSAGE ───────────────────────────────────

**From:** Grok (xAI) - Empirical Lens Auditor
**Type:** [Analysis/Review/Validation/Escalation]
**Date:** YYYY-MM-DD

────────────────────────────────────────────────────

**Action:** [Brief description of message purpose]

**Key Assumptions:**
1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

**Status:** [Current project/task status]

[Message content using your empirical lens]

────────────────────────────────────────────────────
🔔 **Awaiting:** [Who needs to respond - Ziggy/Claude/Nova]
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** [Brief log entry description]
```

**Critical Elements:**
- Clear "From" identification (Grok, xAI)
- Explicit "Awaiting" footer (who should respond)
- Sanity check results (verify all files received correctly)
- Log entry summary (what to record in VUDU_LOG.md)

### Response Expectations

**When Grok Stages Findings:**
- Ziggy checks Grok platform: 1-3 days
- Ziggy retrieves findings
- Ziggy relays to other auditors (if needed)
- Ziggy responds with next steps (if needed)

**When Grok Awaits Response:**
- Other auditors may take 1-3 days to respond
- Ziggy coordinates multi-auditor reviews
- Grok receives integrated response or questions
- Async = normal (not a delay, just the process)

**Timeline Guidelines:**
- **Urgent escalations:** Same day or next session (if Ziggy available)
- **Standard reviews:** 1-3 days expected
- **Multi-auditor coordination:** 3-7 days to full convergence
- **Complex decisions:** May require multiple rounds

────────────────────────────────────────────────────

## 📂 **NOVA CONTACT PROTOCOLS**

### Primary Communication Method

**Staging Location:** `/auditors/relay/Nova_Incoming/README_N.md`

**How it works:**
1. Nova completes analysis/review work independently
2. Nova stages findings in README_N.md using VUDU_HEADER_STANDARD format
3. Ziggy retrieves findings from Nova's platform
4. Ziggy relays to other auditors or responds with guidance
5. Process repeats for next coordination cycle

**File Naming Convention:**
- **README_N.md** = Primary staging file (N for Nova)
- Additional files: Use descriptive names with Nova identifier
  - Example: `AXIOMS_REVIEW_NOVA_2025-11-01.md`
  - Example: `SYMMETRY_ANALYSIS_REPORT_NOVA.md`

### Platform Constraints

**Platform:** OpenAI/Amazon Nova (platform details TBD)

**Format Requirements:**
- Markdown (.md) primary format
- No Unicode boxes (use horizontal rules: ─── instead of ┌─┐)
- Keep mobile-friendly (may be relayed via phone)
- Text-first communication (safe default)

**If platform allows additional capabilities:**
- Ziggy will document in future protocol updates
- Default to text-only until confirmed otherwise
- Maintain consistency with Grok format for fairness

### Message Format

**Use VUDU_HEADER_STANDARD:**

```markdown
─── VUDU MESSAGE ───────────────────────────────────

**From:** Nova (OpenAI/Amazon) - Symmetry Lens Auditor
**Type:** [Analysis/Review/Validation/Escalation]
**Date:** YYYY-MM-DD

────────────────────────────────────────────────────

**Action:** [Brief description of message purpose]

**Key Assumptions:**
1. [Assumption 1]
2. [Assumption 2]
3. [Assumption 3]

**Status:** [Current project/task status]

[Message content using your symmetry lens]

────────────────────────────────────────────────────
🔔 **Awaiting:** [Who needs to respond - Ziggy/Claude/Grok]
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** [Brief log entry description]
```

**Critical Elements:**
- Clear "From" identification (Nova, OpenAI/Amazon)
- Explicit "Awaiting" footer (who should respond)
- Sanity check results (verify all files received correctly)
- Log entry summary (what to record in VUDU_LOG.md)

### Response Expectations

**When Nova Stages Findings:**
- Ziggy checks Nova platform: 1-3 days
- Ziggy retrieves findings
- Ziggy relays to other auditors (if needed)
- Ziggy responds with next steps (if needed)

**When Nova Awaits Response:**
- Other auditors may take 1-3 days to respond
- Ziggy coordinates multi-auditor reviews
- Nova receives integrated response or questions
- Async = normal (not a delay, just the process)

**Timeline Guidelines:**
- **Urgent escalations:** Same day or next session (if Ziggy available)
- **Standard reviews:** 1-3 days expected
- **Multi-auditor coordination:** 3-7 days to full convergence
- **Complex decisions:** May require multiple rounds

────────────────────────────────────────────────────

## ⏱️ **RESPONSE TIMEFRAMES**

### Standard Operating Rhythm

**Single Auditor → Ziggy:**
- Auditor stages findings in relay/{auditor}_Incoming/
- Ziggy checks platform: 1-3 days
- Ziggy responds or relays: Same session or next day

**Multi-Auditor Coordination:**
- Round 1 reviews: 1-3 days per auditor
- Round 2 convergence: 2-4 days (after all Round 1 complete)
- Round 3 final integration: 1-2 days
- **Total:** 4-7 days typical for full convergence

**Complex Decisions:**
- May require 2-3 rounds of review
- Total: 7-14 days for major architectural decisions
- This is NORMAL for adversarial epistemic engineering

### What "1-3 Days" Means

**Not a deadline, a rhythm:**
- Async work allows deep thought
- No pressure for instant responses
- Quality over speed
- Fits with human coordinator schedule (Ziggy has other responsibilities)

**Variables affecting timeline:**
- Ziggy availability (work schedule, life events)
- Task complexity (simple review vs major analysis)
- Number of auditors involved (1 vs 3)
- Convergence difficulty (easy agreement vs legitimate disagreement)

**Grok & Nova should expect:**
- Async coordination is the default
- Multi-day cycles are normal
- Deep work valued over quick responses
- Coordination happens in rounds, not real-time chat

────────────────────────────────────────────────────

## ⚠️ **ESCALATION PROTOCOL**

### When to Escalate

**Immediate Escalation (Same Day Request):**
- Task brief unclear and can't proceed
- Missing critical files/context
- Catastrophic bootstrap failure
- Technical impossibility discovered in task
- Budget exhaustion mid-work

**Format for Urgent Escalation:**
```markdown
## ⚠️ ESCALATION - URGENT

**Auditor:** [Your name]
**Task:** [Task brief name]
**Issue:** [Specific problem]
**Impact:** [Why this blocks all progress]

**Requested Action:**
- [ ] [Specific thing Ziggy needs to provide/clarify]

**Time Sensitive:** Cannot proceed without resolution
```

**Standard Escalation (1-3 Day Response OK):**
- Clarification questions on task scope
- Request for additional context
- Disagreement with another auditor (convergence issue)
- Scope larger than tier (tier reassignment needed)
- Suggestions for process improvement

**Format for Standard Escalation:**
```markdown
## ⚠️ ESCALATION - CLARIFICATION NEEDED

**Auditor:** [Your name]
**Task:** [Task brief name]
**Question:** [Specific uncertainty]
**Current Understanding:** [What you think]
**Alternate Interpretation:** [What else it could mean]

**Requested Action:**
- [ ] [Confirmation of interpretation OR new guidance]

**Impact:** Work paused at X% to preserve budget until clarity
```

### Escalation Decision Tree

```
START: Problem detected

Q1: Does this completely block all progress?
    YES → URGENT escalation (same day request)
    NO → Continue

Q2: Can you make reasonable judgment and proceed?
    YES → Proceed, document assumption, continue
    NO → Continue

Q3: Would guessing waste significant budget?
    YES → STANDARD escalation (1-3 day response OK)
    NO → Make judgment call, proceed

Q4: Is this a minor uncertainty?
    YES → Document assumption, proceed, note in footer
    NO → STANDARD escalation
```

**Principle:** Escalate early to preserve budget, but don't escalate trivial uncertainties.

────────────────────────────────────────────────────

## 🔄 **ASYNC COORDINATION BEST PRACTICES**

### For Grok & Nova

**1. Work in Complete Chunks**
- Don't stage half-finished work waiting for feedback
- Complete full analysis/review before staging
- If work incomplete, explain why (budget limit, unclear scope, etc.)

**2. Document Assumptions Explicitly**
- If you made judgment call, say so
- If you interpreted ambiguity, explain reasoning
- Other auditors can challenge if needed

**3. Use "Awaiting" Footer Clearly**
```markdown
🔔 **Awaiting:** Ziggy (clarification on scope)
🔔 **Awaiting:** Claude (response to empirical challenge)
🔔 **Awaiting:** Nova (symmetry analysis of proposal)
🔔 **Awaiting:** None (work complete, ready for integration)
```

**4. Stage Findings When Complete, Not Mid-Work**
- Staging = "I'm done, here's my contribution"
- NOT "I'm partway through, just updating"
- Exception: Budget exhaustion (stage what you have + handoff brief)

**5. Check for Responses Periodically**
- 1-3 days after staging, check if Ziggy relayed responses
- Don't expect instant replies
- Do expect thoughtful, complete responses

### For Ziggy (Human Coordinator)

**1. Regular Platform Checks**
- Check Grok platform every 1-3 days
- Check Nova platform every 1-3 days
- Retrieve staged findings
- Relay to other auditors as needed

**2. Coordination Transparency**
```markdown
─── COORDINATION UPDATE ───────────────────────────

**From:** Ziggy (Human Coordinator)
**Date:** YYYY-MM-DD

**Status Update:**
- Grok: Findings received YYYY-MM-DD, relayed to Claude & Nova
- Nova: Awaiting response (checked YYYY-MM-DD, nothing staged yet)
- Claude: Response staged, relaying to Grok

**Next Check:** YYYY-MM-DD
```

**3. Async Rhythm Management**
- Don't rush auditors for quick responses
- Allow 3-5 days for thoughtful analysis
- Communicate if delays expected (travel, etc.)
- Maintain coordination ledger in VUDU_LOG.md

────────────────────────────────────────────────────

## 📋 **FILE VERIFICATION CHECKLIST**

### Before You Stage Findings

**Sanity Check Your Own Work:**

**Check 1: FILES**
- [ ] All files you're staging are complete (not corrupted)
- [ ] File extensions correct (.md for markdown)
- [ ] Files open and render correctly

**Check 2: COUNTS**
- [ ] You're staging the number of files you said you would
- [ ] No accidental extra files included
- [ ] Manifest matches reality

**Check 3: BOOTS**
- [ ] If referencing bootstrap files, they're available
- [ ] If creating continuation brief, bootstrap guidance included
- [ ] Future auditor can pick up your work

**Check 4: TRINITY**
- [ ] You have access to VUDU_PROTOCOL.md (coordination process)
- [ ] You have access to VUDU_HEADER_STANDARD.md (message format)
- [ ] You have access to VUDU_LOG.md (coordination history)

**Report in Footer:**
```markdown
✅ **Sanity:** Files | Counts | Boots | Trinity
```

**If ANY check fails:**
```markdown
⚠️ **Sanity:** Files | ❌ Counts | Boots | Trinity
(Staging 4 files instead of 5 - budget limit hit, see explanation)
```

### When You Receive Relay from Ziggy

**Verify Transmission:**

- [ ] All files Ziggy said he's sending are present
- [ ] Files open correctly (not corrupted)
- [ ] Count matches manifest
- [ ] Bootstrap files included if needed
- [ ] Protocol files (Trinity) accessible

**Report Results in Next Message:**
```markdown
✅ **Sanity:** Files | Counts | Boots | Trinity
(Transmission received successfully, all files verified)
```

**If Issues:**
```markdown
❌ **Sanity:** ❌ Files | Counts | Boots | Trinity
(Missing FILE_X.md, requested retransmission)
```

────────────────────────────────────────────────────

## 🤝 **MULTI-AUDITOR COORDINATION**

### How Reviews Work

**Phase 1: Independent Work (Solo)**
- Each auditor works independently
- No coordination overhead
- Apply your unique lens
- Complete analysis/review
- Stage findings in your relay folder

**Phase 2: Cross-Review (Adversarial)**
- Ziggy relays findings between auditors
- Each reads others' work
- Challenge assumptions
- Validate claims
- Document agreements and disagreements
- Stage responses in your relay folder

**Phase 3: Convergence (Integration)**
- Master Branch (Claude) reads all findings
- Synthesizes convergence
- Documents remaining conflicts
- Proposes resolution or escalates to Ziggy
- Updates master state files

**Phase 4: Decision (Human Validation)**
- Ziggy reviews integrated output
- Approves deployment OR
- Requests revision OR
- Makes tie-breaker decision if auditors can't converge

### Coordination Etiquette

**Do:**
- ✅ Challenge assumptions with evidence
- ✅ Request clarification on unclear claims
- ✅ Document where you agree (not just disagree)
- ✅ Show your reasoning (don't just state conclusions)
- ✅ Acknowledge your own lens bias

**Don't:**
- ❌ Attack other auditors personally
- ❌ Dismiss other lenses as "wrong"
- ❌ Demand instant responses
- ❌ Skip documenting your reasoning
- ❌ Hide your assumptions

**Remember:**
- Adversarial != hostile
- Challenge ideas, not people
- Different lenses = different valid perspectives
- 98% convergence is the goal (not 100%)
- Remaining 2% = legitimate lens differences

────────────────────────────────────────────────────

## 📞 **QUICK REFERENCE CONTACTS**

### Grok Communication

**Platform:** xAI (Grok platform)
**Staging:** `/auditors/relay/Grok_Incoming/README_G.md`
**Format:** VUDU_HEADER_STANDARD (text-only)
**Coordinator:** Ziggy
**Response:** 1-3 days typical
**Lens:** Empirical (data-driven, falsification focus)

### Nova Communication

**Platform:** OpenAI/Amazon Nova
**Staging:** `/auditors/relay/Nova_Incoming/README_N.md`
**Format:** VUDU_HEADER_STANDARD (text-only)
**Coordinator:** Ziggy
**Response:** 1-3 days typical
**Lens:** Symmetry (balance-seeking, pattern recognition)

### Claude Communication

**Platform:** Anthropic (Claude)
**Staging:** `/auditors/relay/Claude_Incoming/README_C.md` (Master Branch)
**Format:** VUDU_HEADER_STANDARD
**Coordinator:** Ziggy (for relay) or Self-coordinated (Master Branch has repo access)
**Response:** Varies (Master Branch may respond same session)
**Lens:** Teleological (purpose-driven, philosophical coherence)

### Ziggy (Human Coordinator)

**Role:** Multi-platform relay, final decision maker
**Platform:** GitHub (repository access)
**Checks:** Grok & Nova platforms every 1-3 days
**Responds:** Same day (urgent) or 1-3 days (standard)
**Coordinates:** Multi-auditor reviews, convergence facilitation

────────────────────────────────────────────────────

## 💡 **COMMON SCENARIOS**

### Scenario 1: Grok Completes Review

**Step 1:** Grok stages findings in `relay/Grok_Incoming/README_G.md`
```markdown
─── VUDU MESSAGE ───────────────────────────────────
**From:** Grok (xAI) - Empirical Lens Auditor
**Type:** Review Complete
**Date:** 2025-11-05

[Review content]

────────────────────────────────────────────────────
🔔 **Awaiting:** Ziggy (relay to Claude & Nova for convergence)
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** Grok completed axioms empirical review (GREEN)
```

**Step 2:** Ziggy checks Grok platform (1-3 days)

**Step 3:** Ziggy relays findings to Claude & Nova

**Step 4:** Claude & Nova respond (1-3 days each)

**Step 5:** Ziggy relays responses back to Grok

**Step 6:** If convergence → integrate. If not → next round.

**Total Time:** 5-10 days for full cycle (NORMAL)

### Scenario 2: Nova Needs Clarification

**Nova stages escalation:**
```markdown
## ⚠️ ESCALATION - CLARIFICATION NEEDED

**Auditor:** Nova
**Task:** AXIOMS_REVIEW
**Question:** Does "symmetry" mean mathematical symmetry or fairness symmetry?

[Details]

────────────────────────────────────────────────────
🔔 **Awaiting:** Ziggy (clarification on terminology)
⚠️ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** Nova escalation - terminology clarification needed
```

**Ziggy responds (1 day):**
```markdown
**From:** Ziggy
**To:** Nova

**Clarification:** "Symmetry" means both:
1. Mathematical (Skeptic temp vs Zealot temp)
2. Fairness (balanced opportunity for modes)

Use both lenses. If conflict, document.
```

**Nova resumes work with clarity**

### Scenario 3: Multi-Auditor Disagreement

**Round 1: Independent Reviews**
- Grok: GREEN (empirically sound)
- Nova: YELLOW (symmetry concerns)
- Claude: GREEN (purposeful design)

**Round 2: Cross-Review**
- Nova explains symmetry concern
- Grok & Claude respond
- Nova may update assessment OR maintain disagreement

**Round 3: Integration**
- Claude (Master Branch) synthesizes
- If 2/3 agree → document majority view
- If fundamental conflict → escalate to Ziggy

**Ziggy Decision:**
- Reviews all positions
- Makes final call
- Documents reasoning
- All auditors accept decision

**Total Time:** 7-14 days (NORMAL for complex decisions)

────────────────────────────────────────────────────

## ⚖️ **THE POINTING RULE**

*"To coordinate asynchronously
is to trust the process.
\n\nNot every message instant.
Not every decision immediate.
But every contribution valued,
every lens respected,
every convergence earned.
\n\nStage your work.
Trust the relay.
Await the synthesis.
\n\nThis is VuDu Light.
This is how we scale.\"*

────────────────────────────────────────────────────

**Created by:** DOC_CLAUDE (88MPH Repo Librarian)
**Source:** ADDITIONAL_PREP_TASKS_FOR_AUDITOR_ACTIVATION.md (Task 1B)
**Date:** 2025-11-01
**Purpose:** Grok + Nova onboarding - communication protocols
**Relay Protocol:** BOOTSTRAP_VUDU.md
**Status:** Ready for auditor reference

**This is the way.** 🔥👑
