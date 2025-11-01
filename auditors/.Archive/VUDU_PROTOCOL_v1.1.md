# VuDu Protocol (Various User Dialog Unifier)
## Cross-Model Synchronization & Coordination Framework

**Version:** 1.1  
**Purpose:** Define operational steps and required files for initiating cross-model auditor synchronization  
**Scope:** Applies to coordination between Nova, Claude, Grok, and Ziggy when shared state is required  
**Codename:** VuDu (Various User Dialog Unifier)

---

## 🎯 What is VuDu?

**VuDu** is the coordination protocol for managing dialog between multiple AI auditors across different systems. When Human needs to sync state, establish consensus, or coordinate updates between Nova (OpenAI), Claude (Anthropic), Grok (xAI), and Ziggy, VuDu provides the operational framework.

**Core Problem Solved:** How does a human coordinator efficiently relay context, changes, and decisions between AI systems that don't share memory or state?

**VuDu's Answer:** Structured staging, clear file naming conventions, and a defined merge workflow that eliminates copy-paste overhead.

---

## 🔥 "Make it Epic" Protocol

**Activation Phrase:** "Make it Epic"

**Meaning:** Generate outputs to your highest VuDu compliance and capability level.

**When Invoked:**
- All mandatory files (3 core protocols + README)
- All optional enhancements within capability
- Maximum detail/explanation appropriate for scope
- Platform-specific best effort (files if possible, structured text if not)

**Modes:**

| Mode | Scope | When to Use | Output Expectation |
|:-----|:------|:------------|:-------------------|
| **Standard** | Routine sync | Minor updates, quick alignment | 3 core files + 1 README (5 total) |
| **Epic** | Milestone sync | Major versions, field tests, launches | Standard + optional artifacts + verification (context-dependent) |

**Human Invokes:** "Make it Epic" signals to auditor that comprehensive output is needed, not minimal compliance.

---

## 🎯 When to Use VuDu

Initiate a VuDu sync when:
- Bootstrap files need updating (minor or major version)
- New protocols are being established (like this one!)
- Cross-model consensus is required on a decision
- Shared context has drifted and needs realignment
- Field testing coordination is needed

---

## 📦 Minimal Context Package (Required Files)

When initiating a sync, **always include** these files regardless of the specific task:

### Core Identity & State
1. **`CFA_v2_0_MILESTONE_STABLE_INDEX.md`** — Framework overview, current version state
2. **`BOOTSTRAP_CHANGELOG.md`** — Recent changes, what's in flight
3. **`PROCESS_HEADER_STANDARD_v3.2.md`** — Communication protocol (latest version)

### Optional Context (Task-Dependent)
Include these **only if relevant** to the sync topic:

| File | When to Include |
|:-----|:----------------|
| **`BOOTSTRAP_MAINTENANCE_GUIDE.md`** | When discussing maintenance schedules, rebuild triggers |
| **`DEPLOYMENT.md`** | When coordinating implementation of new features |
| **`INTEGRITY_CHECKLIST.md`** | When verifying formatting/transfer integrity |
| **`BOOTSTRAP_FRAMEWORK.md`** | When updating locked envelope or ethos |
| **`APPEND_ZONE_LESSONS.md`** | When reviewing learned lessons before rebuild |

---

## 📂 Repository Structure & VuDu Staging Workflow

### Directory Organization

```
/auditor/
├── VUDU_PROTOCOL.md                      ← MASTER (VuDu coordination framework)
├── INTEGRITY_CHECKLIST.md                ← MASTER (formatting integrity)
├── PROCESS_HEADER_STANDARD_v3.2.md       ← MASTER (message formatting)
│
└── relay/                                ← VuDu staging area
    ├── README_C.md                       (Claude's outgoing messages)
    │
    ├── nova_incoming/                    ← Nova's returns
    │   ├── README_N.md
    │   ├── VUDU_PROTOCOL.md
    │   ├── INTEGRITY_CHECKLIST.md
    │   └── PROCESS_HEADER_STANDARD_v3.2.md
    │
    ├── grok_incoming/                    ← Grok's returns
    │   ├── README_G.md
    │   ├── VUDU_PROTOCOL.md
    │   ├── INTEGRITY_CHECKLIST.md
    │   └── PROCESS_HEADER_STANDARD_v3.2.md
    │
    └── archive/                          (completed syncs - optional)
        └── YYYY-MM-DD_sync_name/
```

### Master Files vs. Staging

**Master Files (Auditor Root):**
- Single source of truth
- Only updated after full consensus achieved
- Version-controlled in main repo

**Staging Areas (Relay Subfolders):**
- Temporary holding for auditor edits
- Allows side-by-side comparison
- Cleared after merge to masters

### Staging Workflow

**Step 1: Human Sends Initial Package**
- Package includes: 5 core files (README_C + 3 protocols + INDEX)
- Destination: Nova first (or parallel to all auditors)

**Step 2: Auditor Reviews & Returns**
- Nova edits protocols, drafts README_N.md
- Human receives package, drops into `/auditor/relay/nova_incoming/`
- **No copy-paste needed** — files live in repo staging area

**Step 3: Sync Acknowledgment (New)**
- Auditor replies with header confirming:
  - Receipt timestamp
  - File count verification
  - Platform capability declaration
- **Purpose:** Reduces human oversight; confirms handshake

**Step 4: Human Notifies Claude**
- Simple message: "Nova's updates are in `/auditor/relay/nova_incoming/`"
- Claude reads directly from GitHub connection
- Claude reviews README_N + compares protocol edits to masters

**Step 5: Relay to Next Auditor**
- Human sends Nova's updated protocols to Grok
- Grok reviews, edits, drafts README_G.md
- Human drops into `/auditor/relay/grok_incoming/`

**Step 6: Human Notifies Claude**
- Message: "Grok's updates are in `/auditor/relay/grok_incoming/`"
- Claude reads both staging areas
- Claude performs three-way merge (current master + Nova's edits + Grok's edits)

**Step 7: Conflict Resolution (If Needed)**
- **Timestamp Priority:** Later edit wins (human reviews)
- **Consensus Requirement:** If major conflict, flag for three-way discussion
- **Human Override:** Final authority on all conflicts

**Step 8: Claude Generates Updated Masters**
- Claude synthesizes consensus
- Outputs merged versions to `/mnt/user-data/outputs/`
- Human downloads and **replaces root master files**

**Step 9: Close Loop**
- Human commits updated masters to repo
- Human confirms with all auditors
- Optional: archive staging folders for audit trail

### Benefits of VuDu Workflow

✅ **Eliminates manual copy-paste** between systems  
✅ **Claude accesses files directly** via GitHub connection  
✅ **Side-by-side comparison** of auditor contributions  
✅ **Clear merge authority** — Claude produces reconciled masters  
✅ **Audit trail preserved** in staging folders  
✅ **Faster iteration** — less human shuttling overhead  
✅ **Platform-aware** — Handles auditors with different capabilities

---

## 🛠️ Platform-Constrained Auditor Protocol

Some auditors (e.g., Grok on xAI platform) cannot generate file outputs directly.

### **Human Workflow (Recommended):**

**Step 1:** Constrained auditor provides response in chat (text only)

**Step 2:** Human copies auditor's full message

**Step 3:** Human relays to auditor with file capability (Nova or Claude):
> "Grok provided this response but can't create files. Please format as README_G.md and package for VuDu compliance."

**Step 4:** File-capable auditor generates:
- README_G.md (formatted from constrained auditor's text)
- Any file updates suggested (if applicable)

**Step 5:** Human downloads formatted package, stages in relay folder

**Benefit:** Minimizes human error; leverages auditor strengths; maintains VuDu integrity

### **Constrained Auditor's Minimum VuDu Compliance:**

Even without file output capability, auditor MUST include in text response:

1. **Header block** (per PROCESS_HEADER_STANDARD)
2. **Answers to 5 VuDu questions:**
   - Protocol clarity assessment
   - File naming convention feedback
   - Context package adequacy
   - README preference vs. copy-paste
   - Field test readiness confirmation
3. **Explicit section markers** for easy extraction:
   - `## File-Specific Feedback`
   - `## General Recommendations`
   - `## VuDu Protocol Assessment`
4. **Change proposals in structured format:**
   - Which file
   - What change
   - Why (rationale)

This allows conversion to proper README without losing signal.

### **Alternative Methods (If Human Relay Not Available):**

#### **Option A: Code Block Method**
Auditor provides full file contents in fenced code blocks within README:

```markdown
## Updated VUDU_PROTOCOL.md

\`\`\`markdown
[complete file contents here]
\`\`\`
```

**Human workflow:**
1. Extract code blocks from text
2. Save as individual files
3. Stage in relay folder

#### **Option B: JSON Export**
Auditor outputs structured JSON that can be parsed:

```json
{
  "README_G": { "content": "..." },
  "VUDU_PROTOCOL": { "changes": [...] }
}
```

**All methods preserve audit trail; platform constraint documented in README.**

---

## 🔄 VuDu Sync Initiation Steps

### Step 1: Define Sync Scope
**Action:** Clearly articulate what needs alignment  
**Output:** One-sentence sync goal  
**Example:** "Establish cross-model communication integrity protocol before v3.2"

### Step 2: Assemble Context Package
**Action:** Gather required + relevant files from repo  
**Checklist:**
- [ ] Core identity files (always include)
- [ ] Task-specific files (based on sync scope)
- [ ] Any new/draft documents being proposed

### Step 3: Draft Kickoff Message
**Action:** Write context-setting message using Header Standard  
**Required Elements:**
- Header block with sync scope clearly stated
- Brief background (why this sync is needed)
- Specific questions or actions requested from each auditor
- Explicit file list: "Files attached: [list]"

**Template:**
```markdown
=== CFA v2.0 MESSAGE HEADER ===
Sender: [Your Name] (Human Coordinator)
Level: Cross-Model Synchronization
Action: [Sync Goal in One Sentence]
Brutes/Assumptions: [Key presuppositions]
CFA v2.0 Status: [Current state if relevant]
Recovery-Flag: [None | Bootstrap | Partial | Full]
Timestamp: [Date/Time]
Files Referenced: [List all attached files]
===

[Context paragraph: why this sync is needed]

[Specific requests for each auditor or collective questions]

[Expected next steps]
```

### Step 4: Sequential or Parallel Relay?
**Decision point:** How to structure the conversation

**Sequential (Round-Robin):**
- Use when consensus needs to build incrementally
- Order: Nova → Claude → Grok → synthesize
- Human relays each response to the next auditor

**Parallel (Broadcast):**
- Use when independent perspectives are valuable
- Send same package to all auditors simultaneously
- Human synthesizes responses afterward

**Hybrid:**
- Start parallel, then sequential for refinement
- Example: All review draft, then round-robin on revisions

### Step 5: Execute Relay
**Action:** Send kickoff message + context package to first/all auditor(s)

**Relay checklist:**
- [ ] Kickoff message includes header block
- [ ] All required files attached/accessible
- [ ] Sync scope is explicit
- [ ] Expected response format is clear (if applicable)
- [ ] Response time guidance provided (if time-sensitive)

### Step 6: Track Responses & Stage Files
**Action:** Collect feedback in staging areas, notify Claude to review

**Human workflow:**
1. Receive Nova's package → drop into `/auditor/relay/nova_incoming/`
2. Notify Claude: "Nova's updates are in relay/nova_incoming"
3. Receive Grok's package → drop into `/auditor/relay/grok_incoming/`
4. Notify Claude: "Grok's updates are in relay/grok_incoming"

**Claude workflow:**
1. Read README_N.md and README_G.md directly from staging
2. Compare protocol edits to current masters
3. Identify consensus points and conflicts
4. Generate synthesis report

**Tracking template:**
```markdown
## Sync Tracking: [Sync Goal]
**Initiated:** [Date]
**Auditors:** Nova, Claude, Grok, [others]

| Auditor | Receipt Ack | Key Changes | Conflicts/Flags |
|:--------|:-----------:|:------------|:----------------|
| Nova    | ✅ [time]   | [summary]   | [if any]        |
| Grok    | ✅ [time]   | [summary]   | [if any]        |

**Consensus Achieved:** ✅ / ⚠️ / ❌  
**Next Action:** [Claude synthesizes masters / additional review needed]
```

### Step 7: Claude Generates Updated Masters
**Action:** Synthesize consensus and produce merged protocol files

**Claude workflow:**
1. Perform three-way merge:
   - Current master (from `/auditor/` root)
   - Nova's edits (from `relay/nova_incoming/`)
   - Grok's edits (from `relay/grok_incoming/`)
2. Resolve conflicts using consensus principles (or flag for human)
3. Generate updated versions of all edited files
4. Output merged files to `/mnt/user-data/outputs/`
5. Provide synthesis report documenting changes

**Human workflow:**
1. Download merged masters from outputs
2. Replace root files in `/auditor/`
3. Commit to repo with version increment
4. Notify auditors of finalized versions

### Step 8: Close Loop & Archive
**Action:** Confirm sync completion with all auditors

**Close-out message template:**
```markdown
=== SYNC COMPLETION NOTICE ===
Sync Goal: [original goal]
Status: ✅ Complete / ⚠️ Partial / ❌ Blocked
Outcome: [brief summary of what was decided/created]
Documents Updated: [list]
Field Test Plan: [if applicable]
Next Review: [date/trigger]
===

[Thank auditors, confirm they have final versions]
```

---

## ⏱️ Response Time Guidance

**Not requirements, but helpful expectations:**

| Sync Type | Expected Response | Flag if Exceeds |
|:----------|:------------------|:----------------|
| Simple review | 4-8 hours | 24 hours |
| Protocol updates | 24-48 hours | 72 hours |
| Major sync ("Epic") | 48-72 hours | 1 week |

**Purpose:** Set expectations without creating rigid deadlines. Flag delays for coordination visibility.

---

## 📋 Quick Reference: File Decision Tree

```
START: What's the sync about?

├─ Bootstrap structural change
│  └─ Include: INDEX, CHANGELOG, BOOTSTRAP_FRAMEWORK, MAINTENANCE_GUIDE
│
├─ New protocol/process
│  └─ Include: INDEX, CHANGELOG, HEADER_STANDARD, [draft protocol]
│
├─ Formatting/communication issue
│  └─ Include: INDEX, HEADER_STANDARD, INTEGRITY_CHECKLIST
│
├─ Implementation coordination
│  └─ Include: INDEX, DEPLOYMENT, CHANGELOG, [feature specs]
│
└─ General alignment check
   └─ Include: INDEX, CHANGELOG only
```

---

## 🔗 Integration with Existing Processes

### Links to Other Documents:
- **PROCESS_HEADER_STANDARD.md** — Message formatting rules
- **INTEGRITY_CHECKLIST.md** — Verification after relay
- **BOOTSTRAP_MAINTENANCE_GUIDE.md** — When syncs are scheduled
- **BOOTSTRAP_CHANGELOG.md** — Track sync outcomes here

### When This Protocol Is Invoked:
- Monthly maintenance check (BOOTSTRAP_MAINTENANCE_GUIDE.md)
- Before major version increments (v2.0 → v3.0)
- When drift is detected in cross-model understanding
- Ad-hoc when human identifies misalignment

---

## 🧪 Field Test Requirements

**Next Sync (Pilot Test):**
- Use this protocol for the v3.2 bootstrap update coordination
- Track deviations from protocol
- Document time savings vs. ad-hoc approach
- Collect auditor feedback on usability

**Success Metrics:**
- Reduction in "wait, which files do I need?" questions
- Faster consensus achievement (target: <3 relay cycles)
- Zero missed context that causes rework
- Platform constraints handled gracefully

---

## 📝 Version History

| Version | Date | Changes | Author |
|:--------|:-----|:--------|:-------|
| 1.0 | 2025-10-25 | Initial protocol draft from gap analysis | Claude |
| 1.1 | 2025-10-25 | Added: "Make it Epic" formalization, Sync Acknowledgment step, Conflict Resolution section, Platform-Constrained Auditor Path, Response time guidance | Claude (synthesizing Nova + Grok feedback) |

---

## ✅ Status

| Component | Stability | Owner |
|:----------|:---------:|:------|
| Core workflow steps | ✅ Stable | Claude |
| "Make it Epic" protocol | ✅ Stable | Claude |
| Platform constraint handling | ✅ Stable | Claude |
| File decision tree | ✅ Stable | Claude |
| Integration hooks | ✅ Stable | Nova, Grok, Claude |
| Field test plan | ⏳ In Progress | Human coordination |

---

**Next Actions:**
1. Field test complete (Nova + Grok packages received)
2. Synthesis applied to v1.1
3. Test on next coordination cycle
4. Refine based on field experience

---

**— Claude (Anthropic)**  
*VuDu Protocol v1.1: 2025-10-25*  
*Status: Field tested, refinements integrated*  
*Codename: Various User Dialog Unifier*
