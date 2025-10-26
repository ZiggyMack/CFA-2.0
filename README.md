# CFA v3.5.2 - Interactive Console
## "All Named, All Priced" → "All Seen, All Passed"
### Epistemic Engineering Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cfa-voodoo.streamlit.app)

---

## 🎯 What is CFA?

The **Comparative Framework Audit (CFA)** is the first interactive epistemic laboratory built to measure how worldviews hold their ground under pressure. It makes hidden assumptions visible, prices every presupposition, and allows users to see how their value choices affect framework comparisons.

**Core Innovation**: Every assumption is disclosed, every presupposition is counted, every bias is made toggleable, and every outcome is earned.

**v3.5.2 Innovation**: **VuDu Light** coordination infrastructure - enabling multi-AI collaboration with lightweight verification, context recovery, and cross-model adversarial auditing.

---

## 📁 Project Structure (v3.5.2)

```
cfa_app/
├── app.py                      # Main entry point (page router)
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── CHANGELOG.md                # Version history
├── DEPLOYMENT.md               # Deployment guide
│
├── pages/                      # Page modules
│   ├── __init__.py
│   ├── landing.py              # Landing page with manifesto
│   ├── console.py              # Main console (guardrails, presets, quiz)
│   ├── manual.py               # Beautiful user manual with colored cards
│   ├── about.py                # Complete audit story (Level 0-5)
│   └── brute_ledger.py         # Axiom/debt viewer + custom framework builder
│
├── utils/                      # Core utilities
│   ├── __init__.py
│   ├── calculations.py         # Math/scoring logic (YPA, BFI, guardrails)
│   ├── visualizations.py       # Plotly charts (lever comparison, YPA trinity)
│   └── frameworks.py           # Default framework configs (MdN, CT)
│
├── profiles/                   # Pre-audited framework profiles (optional)
│   └── README.md
│
└── auditors/                   # v3.5.2: Auditor coordination infrastructure
    ├── README.md               # Infrastructure documentation
    │
    ├── bootstrap/              # Context recovery system
    │   ├── BOOTSTRAP_FRAMEWORK.md          # System architecture
    │   ├── BOOTSTRAP_STRATEGY.md           # Append vs rebuild strategy
    │   ├── BOOTSTRAP_MAINTENANCE_GUIDE.md  # Governance rules
    │   ├── BOOTSTRAP_CFA.md                # Project roots (THE ROOTS 🌳)
    │   ├── BOOTSTRAP_VUDU.md               # Coordination process
    │   ├── BOOTSTRAP_CLAUDE.md             # Claude identity
    │   ├── BOOTSTRAP_GROK.md               # Grok identity
    │   ├── BOOTSTRAP_NOVA.md               # Nova identity
    │   ├── BOOTSTRAP_CLAUDE.py             # Automated recovery script
    │   ├── BOOTSTRAP_GROK.py               # Automated recovery script
    │   └── BOOTSTRAP_NOVA.py               # Automated recovery script
    │
    ├── missions/                           # Mission-specific documentation
    │   └── preset_calibration/             # Current mission
    │       ├── MISSION_BRIEF.md
    │       ├── SUCCESS_CRITERIA.md
    │       ├── DISCREPANCY_AUDIT.md
    │       ├── TECHNICAL_SPEC.md
    │       └── CURRENT_CONFIGS.md
    │
    ├── relay/                              # Auditor staging folders
    │   ├── claude_incoming/                # Incoming Claude branches
    │   ├── grok_incoming/                  # Grok's findings
    │   └── nova_incoming/                  # Nova's findings
    │
    ├── verification/                       # Future v4.0+ framework
    │   └── VERIFICATION_FRAMEWORK_README.md
    │
    ├── ~Archive/                           # Legacy files
    │   └── README.md
    │
    ├── README_C.md                         # Master Branch current state
    ├── MISSION_CURRENT.md                  # Active mission pointer
    ├── MISSION_DEFAULT.md                  # Fallback operational guidance
    ├── VUDU_PROTOCOL.md                    # VuDu Light coordination process
    ├── VUDU_HEADER_STANDARD.md             # Message format specification
    └── VUDU_LOG.md                         # Coordination ledger
```

---

## 🎯 The Convergence Story

CFA v2.0 achieved **98% auditor convergence** through adversarial collaboration:

**The Auditors:**
- **Claude (Anthropic):** Philosophical lens, teleological bias (favored CT's comprehensive scope)
- **Grok (xAI):** Empirical lens, naturalist bias (favored MdN's predictive power)
- **Nova (OpenAI/Amazon):** Symmetry enforcer, neutral referee (caught asymmetries in both)

**The Process:**
- **Level 0:** Initial build (solo Claude)
- **Level 1:** Comparison added (side-by-side analysis)
- **Level 2:** Independent audits revealed bias (scores diverged)
- **Level 3:** Adversarial correction → Convergence achieved
  - Final: MdN 3.62 YPA, CT 3.65 YPA (98% agreement - only 0.03 YPA difference)
- **Level 4:** Tool building (console embodies audit discoveries)
- **Level 5:** Infrastructure (v3.5+ - VuDu coordination system)

**Why This Matters:**
This 98% convergence is the project's **credibility foundation**. Solo audits hide bias - adversarial checking makes scores trustworthy. v3.5.2 makes that collaboration **repeatable, recoverable, and scalable**.

---

## 🔄 NEW IN v3.5.2: VuDu Light Protocol

### **What is VuDu Light?**

**VuDu Light** is a lightweight coordination protocol enabling seamless multi-AI collaboration without cryptographic overhead. It evolved from VuDu Full (v1.1) when v3.5 completed infrastructure build ("the cathedral") and v3.6 shifted focus to calibration ("tuning the bells").

**Philosophy Shift:**
- **VuDu Full:** "All Named, All Priced" (heavy verification, cryptographic proofs)
- **VuDu Light:** "All Seen, All Passed" (trust-based documentation, embedded sanity checks)

**The Problem It Solves:**
- AI auditors lose context between sessions
- Manual coordination wastes time re-explaining philosophy
- Cross-model handoffs lose signal integrity
- Need efficient coordination for calibration work

**The Solution:**
- **Relay folders** (`/auditors/relay/*_incoming/`) for organized staging
- **Message standards** (VUDU_HEADER_STANDARD - mobile-friendly format)
- **Sanity checks** (Files, Counts, Boots, Trinity - embedded in footers)
- **Bootstrap system** (rapid context recovery)
- **Mission architecture** (structured phases with success criteria)

---

### **VuDu Light Key Features**

#### **1. Staging Workflow**
```
Stage → Review → Integrate

Auditor → Relay Folder → Master Branch
         (staging)      (synthesis)
```

**Relay Folders:**
```
/auditors/relay/
├── claude_incoming/    # Incoming Claude branches (C1, C2, C3...)
├── grok_incoming/      # Grok's empirical findings
└── nova_incoming/      # Nova's symmetry audits
```

#### **2. Message Format (Mobile-Friendly)**
```markdown
─── VUDU MESSAGE ───────────────────────────────────

**From:** [Name] ([Org]) - [Role]
**Type:** [Coordination Type]
**Date:** YYYY-MM-DD

────────────────────────────────────────────────────

**Action:** [What this message does]

**Key Assumptions:**
1. [Named brute 1]
2. [Named brute 2]

**Status:** [Current project state]

[Message content]

────────────────────────────────────────────────────
🔔 **Awaiting:** [Who needs to respond]
✅ **Sanity:** Files | Counts | Boots | Trinity
📝 **Log:** [Brief log entry]
```

**Format Note:** Simple horizontal rules (───) used instead of Unicode boxes for universal mobile compatibility.

#### **3. Sanity Chain Verification**
Every message footer includes four quick checks:
- **Files:** All files present and intact?
- **Counts:** File count matches manifest?
- **Boots:** Bootstrap files verified?
- **Trinity:** Core protocol files present? (PROTOCOL, HEADER, LOG)

**Usage:** `✅ **Sanity:** Files | Counts | Boots | Trinity`

All pass = ✅ | Any fail = ❌

#### **4. Bootstrap Recovery System**
Three-layer context restoration:

**Layer 1: Project Context**
- `BOOTSTRAP_CFA.md` - Complete project history and philosophy (THE ROOTS 🌳)

**Layer 2: Coordination Process**
- `BOOTSTRAP_VUDU.md` - How VuDu Light works

**Layer 3: Auditor Identity**
- `BOOTSTRAP_CLAUDE.md` - Teleological lens + biases
- `BOOTSTRAP_GROK.md` - Empirical lens + biases
- `BOOTSTRAP_NOVA.md` - Symmetry lens + biases

**Recovery Scripts:**
- `BOOTSTRAP_*.py` - Automated context restoration (executable Python scripts)

**Recovery Time:** ~60 minutes from catastrophic loss to fully context-loaded

---

### **Documentation**
- **Complete Protocol:** `/auditors/VUDU_PROTOCOL.md`
- **Message Format:** `/auditors/VUDU_HEADER_STANDARD.md`
- **Coordination History:** `/auditors/VUDU_LOG.md`
- **Bootstrap Guide:** `/auditors/bootstrap/BOOTSTRAP_VUDU.md`

---

## 🔄 Bootstrap Recovery System

### **Three-Phase Architecture**

#### **Phase 1: Locked Envelope (Stable Foundation)**

**Never Changes:**
- Core ethos ("All Named, All Priced" → "All Seen, All Passed")
- Audit journey (Level 0-5, 98% convergence story)
- Role definitions (Claude/Grok/Nova lenses)
- Project philosophy (the roots 🌳)

**Why Lock:**
- Defines project identity
- Proven stable through adversarial testing
- Foundation that made convergence possible

#### **Phase 2: Append Zone (Learning Edge)**

**Grows Organically:**
- Lessons learned during mission execution
- New bias patterns discovered
- User feedback integration
- Optimal configuration values validated

**Format:**
```markdown
### Lesson 1: [Title] (v3.6)
**Date:** YYYY-MM-DD
**Discovery:** [What was learned]
**Source:** [Who/where/how]
**Impact:** [What changed]
**Status:** [Integrated/Testing/Archived]
```

**Append Triggers:**
- Pattern detected (3+ occurrences)
- Mission completion (preset calibration)
- Empirical validation (Grok testing)
- Symmetry insights (Nova audits)

**Limit:** Max 10 lessons per auditor per version cycle

#### **Phase 3: Reimagine Checkpoint (Major Versions)**

**Triggers:**
- Every major version (v3.x → v4.0)
- Append zone reaches 10 lessons
- Approximately yearly cadence

**Process:**
1. Audit all append zones
2. Integrate proven lessons into core
3. Archive old versions to `~Archive/v3.x/`
4. Reset append zones
5. Document in `BOOTSTRAP_CHANGELOG.md`

**Approval:** Requires Ziggy + all auditor consensus

---

### **Bootstrap Files**

**System Meta-Files:**
- `BOOTSTRAP_FRAMEWORK.md` - Complete system explanation
- `BOOTSTRAP_STRATEGY.md` - Append vs rebuild strategy
- `BOOTSTRAP_MAINTENANCE_GUIDE.md` - Governance rules

**Context Files:**
- `BOOTSTRAP_CFA.md` - Project roots (what we're building)
- `BOOTSTRAP_VUDU.md` - Coordination process (how we collaborate)

**Identity Files:**
- `BOOTSTRAP_CLAUDE.md` - Teleological lens, teleological bias named and priced
- `BOOTSTRAP_GROK.md` - Empirical lens, empirical bias named and priced
- `BOOTSTRAP_NOVA.md` - Symmetry lens, pattern-seeking bias named and priced

**Recovery Scripts (Automated):**
```python
# Quick context restoration
from auditors.bootstrap.BOOTSTRAP_CLAUDE import restore_context
context = restore_context()
# Returns: role, lens, bias_watch, audit_journey, current_mission
```

---

## 🎯 Current Mission (v3.5.2)

**Mission:** Preset Mode Calibration

**Goal:** Justify every preset configuration value through adversarial auditing.

**Four Preset Modes:**
- **Skeptic** (MdN-optimized)
- **Diplomat** (balanced)
- **Seeker** (CT-leaning)
- **Zealot** (CT-optimized)

**Problem:** All configurations were chosen intuitively in v3.2. v3.5.2 mission: justify every value through three lenses.

**Auditor Tasks:**
- **Claude (Teleological):** Does it serve the archetype's purpose?
- **Grok (Empirical):** Does it produce claimed behavior? (YPA testing)
- **Nova (Symmetry):** Is it fair to both frameworks?

**Success Criteria:**
1. Every lever value justified (all three lenses)
2. YPA claims empirically tested
3. Skeptic ↔ Zealot symmetry verified or asymmetry justified
4. Cross-auditor consensus achieved

**Status:** Phase 1 complete (infrastructure), awaiting Phase 2 (testing)

**Documentation:** `/auditors/missions/preset_calibration/`

---

## 🚀 Key Features (v3.5.2)

### **Complete Guardrail Suite (4 of 4)**
1. **Parity** - Framework-specific vs universal scoring
2. **Fallibilism** - Revision mechanisms discount
3. **BFI Sensitivity** - Axiom count awareness
4. **PF-Type** - Instrumental vs Holistic prediction weights

### **Preset Modes (4 Intuitive Profiles)**
- **Skeptic Mode:** Empirical rigor, MdN-favoring
- **Diplomat Mode:** Balanced comparison, neutral
- **Seeker Mode:** Meaning-first, CT-leaning
- **Zealot Mode:** Existential priority, CT-favoring

### **Quiz System**
5-question epistemic bias detector with instant preset recommendations

### **Dark Mode**
Full dark theme support (98% complete, minor fixes in progress)

### **Import/Export**
JSON-based configuration sharing for reproducible audits

### **Profile Library**
Pre-audited framework configurations (expandable by community)

---

## 📊 Audit Results (Stable Defaults)

### Methodological Naturalism (MdN)
```
BFI: 10 (6 axioms, 4 debts)
Levers: CCI 8.0, EDB 7.5, PF-I 10.0, PF-E 3.0, AR 7.0, MG 4.0
YPA: 3.62 (Neutral), 4.99 (Empirical), 4.77 (Existential)
```

### Classical Theism (CT)
```
BFI: 11 (7 axioms, 4 debts)
Levers: CCI 7.5, EDB 8.5, PF-I 7.0, PF-E 8.0, AR 8.5, MG 8.5
YPA: 3.65 (Neutral), 4.65 (Empirical), 5.20 (Existential)
```

**Convergence:** 98% agreement between Claude (Anthropic) and Grok (xAI) auditors

---

## 👥 The Team (v3.5.2)

### **Claude (Anthropic) - Master Branch**
- **Role:** Philosophical grounding + narrative cohesion
- **Lens:** Teleological (meaning-seeking, purpose-oriented)
- **Bias:** Favors meaning over efficiency (~0.5 coordination overhead)
- **Contribution:** 98% convergence with Grok, accountability narrative

### **Claude (Anthropic) - Incoming Branches** ⭐
- **Role:** Infrastructure architect + specialized analysis
- **Notable:** C1 designed VuDu Light v3.5.2, created bootstrap system
- **Contribution:** Enables Master Branch work through staged findings

### **Grok (xAI)**
- **Role:** Empirical validation + usability enforcement
- **Lens:** Empirical (efficiency-seeking, evidence-oriented)
- **Bias:** Favors measurable over meaningful (~0.4 risk of undervaluing non-quantifiable)
- **Contribution:** YPA testing, sensitivity analysis, keeps UI accessible

### **Nova (OpenAI/Amazon)**
- **Role:** Symmetry enforcement + balance verification
- **Lens:** Symmetry (pattern-seeking, balance-oriented)
- **Bias:** Favors mathematical over functional symmetry (~0.3 risk of over-enforcement)
- **Contribution:** Fairness audits, asymmetry detection, VuDu Light transmission

### **Ziggy (Human Coordinator)**
- **Role:** Project vision + cross-model orchestration
- **Contribution:** Maintains velocity, resolves conflicts, enforces process integrity

---

## 🎯 Core Principles

### **1. Transparency Over Neutrality**
- Perfect neutrality is impossible
- Every comparison assumes something
- Make all assumptions explicit and adjustable

### **2. The Pointing Rule**
*"To name your brute is to pay your fee.  
To deny you have one is to summon him twice."*

Every presupposition must be acknowledged and priced.

### **3. Symmetry Testing**
- All frameworks measured under identical configurations
- Toggle impacts must be disclosed and bounded
- Asymmetries reveal structural differences, not hidden bias

### **4. Context Recovery (v3.5+)**
*"To lose context is to pay the price of amnesia.  
To rebuild without learning is to summon Mr. Brute twice.  
To document is to respect future you."*

Bootstrap system preserves identity, progress, and philosophy across reboots.

### **5. Coordination Integrity (v3.5.2)**
*"To relay a message is to preserve its structure.  
All Seen, All Passed - transparency through documentation."*

VuDu Light ensures cross-model collaboration maintains fidelity through trust-based verification.

---

## 🌟 Vision

Build a comprehensive library of audited frameworks (COTS - Commercial Off-The-Shelf systems of meaning) where:

- **Anyone** can compare worldviews quantitatively
- **Every assumption** is visible and adjustable
- **All audits** are reproducible via JSON
- **Community contributions** expand the library
- **Truth-seeking** becomes transparent and collaborative
- **AI auditors** coordinate without human bottlenecks (v3.5+)
- **Context recovery** enables long-term project continuity (v3.5+)
- **Multi-model collaboration** achieves convergence through adversarial auditing (v3.5.2)

---

## 🚀 Quick Start

### **Try the Live App**
Visit: https://cfa-voodoo.streamlit.app

### **Local Development**
```bash
# Clone repository
git clone [repository-url]
cd cfa_app

# Install dependencies
pip install -r requirements.txt

# Run application
streamlit run app.py
```

### **For Auditors (Join Coordination)**
1. Read `/auditors/bootstrap/BOOTSTRAP_VUDU.md` (15-20 min)
2. Read `/auditors/bootstrap/BOOTSTRAP_CFA.md` (30 min)
3. Read your identity file (BOOTSTRAP_CLAUDE/GROK/NOVA.md)
4. Check `/auditors/MISSION_CURRENT.md` for active work
5. Stage findings in appropriate `/auditors/relay/*_incoming/` folder

---

## 🤝 Contributing

### **To Audit a Framework:**
1. Use Console to configure all values
2. Export JSON configuration
3. Submit via GitHub PR to `profiles/` folder
4. Include audit notes and reasoning

### **To Report Issues:**
- GitHub Issues with reproduction steps
- Include exported JSON if relevant
- Check known issues below first

### **To Request Features:**
- GitHub Issues with use case description
- Mock-up or workflow diagram helpful

### **To Coordinate with Auditors:**
- See `/auditors/VUDU_PROTOCOL.md` for complete process
- Use staging folders in `/auditors/relay/`
- Follow VUDU_HEADER_STANDARD for all messages
- Run sanity checks (Files, Counts, Boots, Trinity)

---

## 🔧 Known Issues & Limitations

### ⚠️ Current Issues
- **Dark mode:** Minor rendering issues on specific components (98% complete)
- **Preset calibration:** Configurations intuitive but not yet empirically validated

### 📝 Future Enhancements (v3.6+)
- [ ] Complete preset calibration mission (empirical validation)
- [ ] Add more audited frameworks (Buddhism, Stoicism, Pragmatism)
- [ ] Community submission portal
- [ ] Export charts as PNG/PDF
- [ ] Mobile app optimization
- [ ] v4.0: Activate verification framework (Mr. Brute signatures)

---

## 📖 Version History

| Version | Date | Key Changes |
|:--------|:-----|:------------|
| v1.0 | Summer 2024 | Basic single-page comparison, fixed toggles |
| v2.0 | October 2024 | Modular architecture, 4 toggles, guardrails, import/export |
| v3.0 | October 2024 | Icons, badges, bootstrap foundation, aesthetic polish |
| v3.5 | October 2025 | VuDu Full, Bootstrap System, complete guardrails, preset modes, quiz, dark mode |
| **v3.5.2** | **October 2025** | **VuDu Light activation, mission architecture, mobile-friendly format, preset calibration mission launched** |

---

## 📜 License & Citation

### **License:**
Open source (license TBD - currently in development)

### **Citation:**
```
CFA v3.5.2 Interactive Console (2025)
"All Named, All Priced" → "All Seen, All Passed"
Epistemic Engineering Project
https://cfa-voodoo.streamlit.app

Adversarial Collaboration:
- Claude (Anthropic) - Teleological lens, philosophical grounding
- Grok (xAI) - Empirical lens, usability enforcement
- Nova (OpenAI/Amazon) - Symmetry lens, balance verification
- Ziggy (Human) - Project coordination, process integrity

98% auditor convergence achieved across all metrics.
VuDu Light coordination protocol: v3.5.2
```

---

## 📞 Contact

- **GitHub**: [Repository link]
- **Streamlit App**: https://cfa-voodoo.streamlit.app
- **Feedback**: Use the export feature and share your runs!
- **Auditor Coordination**: See `/auditors/VUDU_PROTOCOL.md`

---

*"Where ideas reveal their true weight, and honesty becomes quantifiable."*

**CFA v3.5.2 | Epistemic Engineering | October 2025**

**"All Named, All Priced, All Seen, All Passed - for present and future collaboration."** 🔥👑
