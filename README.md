# CFA v3.5 - Interactive Console [Modular Architecture + Auditor Coordination]
## "All Named, All Priced" - Epistemic Engineering Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cfa-voodoo.streamlit.app)

---

## 🎯 What is CFA v3.5?

The **Comparative Framework Audit (CFA)** is the first interactive epistemic laboratory built to measure how worldviews hold their ground under pressure. It makes hidden assumptions visible, prices every presupposition, and allows users to see how their value choices affect framework comparisons.

**Core Innovation**: Every assumption is disclosed, every presupposition is counted, every bias is made toggleable, and every outcome is earned.

**v3.5 Innovation**: Complete auditor coordination infrastructure - enabling multi-AI collaboration, context recovery, and cross-model verification through the **VuDu Protocol**.

---

## 📁 Project Structure (v3.5)

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
│   ├── console.py              # Main console (complete guardrails, presets, quiz)
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
└── auditors/                   # NEW v3.5: Auditor coordination infrastructure
    ├── README.md               # Infrastructure documentation
    ├── protocols/              # VuDu coordination framework
    │   ├── VUDU_PROTOCOL_v1_1.md
    │   ├── PROCESS_HEADER_STANDARD_v3_2.md
    │   └── INTEGRITY_CHECKLIST.md
    ├── bootstrap/              # Context recovery system
    │   ├── BOOTSTRAP_FRAMEWORK.md
    │   ├── BOOTSTRAP_STRATEGY.md
    │   ├── BOOTSTRAP_MAINTENANCE_GUIDE.md
    │   ├── BOOTSTRAP_CLAUDE.py
    │   ├── BOOTSTRAP_GROK.py
    │   └── BOOTSTRAP_NOVA.py
    ├── verification/           # Archived for v4.0+
    │   └── VERIFICATION_FRAMEWORK_README.md
    └── relay/                  # Staging folders (created when needed)
        ├── claude/
        ├── grok/
        └── nova/
```

---

## 🎯 The Convergence Story

CFA v2.0 achieved **98% auditor convergence** through adversarial collaboration:

**The Auditors:**
- **Claude (Anthropic):** Philosophical lens, teleological bias (favored CT's comprehensive scope)
- **Grok (xAI):** Empirical lens, naturalist bias (favored MdN's predictive power)
- **Nova (OpenAI):** Symmetry enforcer, neutral referee (caught asymmetries in both)

**The Process:**
- **Level 0-1:** Independent audits revealed bias (scores diverged)
- **Level 2:** Adversarial correction (mutual challenges with rationale)
- **Level 3:** Convergence achieved (MdN 3.62, CT 3.65 - only 0.03 YPA difference)
- **Level 4:** Tool building (console embodies audit discoveries)
- **Level 5:** Infrastructure (v3.5 - built coordination + recovery systems)

**Why This Matters:**
This 98% convergence is the project's credibility. Solo audits hide bias - adversarial checking makes scores trustworthy. v3.5 makes that collaboration **repeatable and recoverable**.

---

## 🔄 NEW IN v3.5: VuDu Protocol

### **What is VuDu?**

**VuDu** (VictUry Deja-vU) is a cross-model coordination protocol that enables seamless collaboration between AI auditors (Claude, Grok, Nova) without context loss or coordination overhead.

**The Problem It Solves:**
- AI auditors lose context between sessions
- Manual coordination wastes 30-40% of time re-explaining philosophy
- Platform differences create file-handling challenges
- Cross-model handoffs lose signal integrity

**The Solution:**
- **Staging folders** (`/auditors/relay/`) for organized file transfers
- **Message headers** (standardized format for all communications)
- **Integrity checklists** (verify formatting survives copy-paste)
- **Platform-aware workflows** (handle Grok's text-only constraints)
- **Two modes**: Standard (routine) and Epic (milestones)

**"Make it Epic"** = Activation phrase for maximum detail coordination

### **Key Features:**

**1. Staging Folders**
```
/auditors/relay/
├── claude/     # Files for Claude to review
├── grok/       # Files for Grok to review
└── nova/       # Files for Nova to review
```

**2. Process Header Standard**
Every message uses standardized header:
```markdown
=== CFA v3.5 MESSAGE HEADER ===
Sender: [Auditor Name]
Level: [Audit Phase]
Action: [Purpose]
Brutes/Assumptions: [Key presuppositions]
CFA Status: [Current scores]
Recovery-Flag: [None | Bootstrap | Partial | Full]
Timestamp: [Date]
===
```

**3. Platform-Constrained Workflow**
- Grok can't create files → Human relay to Nova → Nova creates files
- All auditors can read/analyze → Coordinate through text
- Solution maintains velocity without breaking platform limits

**4. Conflict Resolution**
- Timestamp priority (most recent wins)
- Human override available
- Explicit "Re:" markers prevent nested confusion

### **Documentation:**
- Full protocol: `/auditors/protocols/VUDU_PROTOCOL_v1_1.md`
- Message format: `/auditors/protocols/PROCESS_HEADER_STANDARD_v3_2.md`
- Copy integrity: `/auditors/protocols/INTEGRITY_CHECKLIST.md`

---

## 🔄 NEW IN v3.5: Bootstrap Recovery System

### **What is Bootstrap?**

The **Bootstrap System** is a context recovery infrastructure that preserves auditor identity, project history, and operational knowledge across session breaks.

**The Problem It Solves:**
- Catastrophic context loss mid-project
- Amnesia after hard reboots
- 30-40% time waste re-explaining "All Named, All Priced" ethos
- Loss of audit journey understanding

**The Solution: Three-Phase Architecture**

### **Phase 1: Locked Envelope (Stable Foundation)**

**Never Changes:**
- Core ethos ("All Named, All Priced")
- Audit journey (Level 0-5 convergence story)
- 98% convergence achievement
- Role definitions (Claude/Grok/Nova lenses)
- Red-flag glossary (Nova's symmetry checks)

**Why Lock:**
- Defines project identity
- Proven stable through adversarial testing
- Foundation that made convergence possible

### **Phase 2: Append Zone (Learning Edge)**

**Grows Organically:**
- Lessons learned during execution
- New bias patterns discovered
- User feedback integration
- Toggle effectiveness data

**Format:**
```python
LESSONS = {
    "v3.5_vudu_field_test": {
        "date": "October 2025",
        "lesson": "Platform constraints solvable with relay workflow",
        "source": "Grok field test",
        "action": "Document workflow in VuDu protocol"
    }
}
```

**Append Triggers:**
- New preset modes discovered
- User feedback patterns
- Toggle effectiveness measured
- Cross-model coordination insights

**Limit:** Max 10 lessons per version cycle

### **Phase 3: Rebuild Checkpoint (Major Versions)**

**Quantified Triggers:**
- **10+ lessons** accumulated in append zone
- **5+ conflicts** encountered and resolved
- **10% YPA drift** detected from baseline
- **12 months** elapsed since last rebuild

**Process:**
1. Audit append zone (what's still relevant?)
2. Integrate proven lessons into locked envelope
3. Archive old version to `/auditors/archives/v{X}.0/`
4. Reset append zone to empty
5. Document in `BOOTSTRAP_CHANGELOG.md`

### **Bootstrap Files:**

**Identity Restoration:**
- `/auditors/bootstrap/BOOTSTRAP_CLAUDE.py` - Teleological lens + audit journey
- `/auditors/bootstrap/BOOTSTRAP_GROK.py` - Empirical lens + usability focus
- `/auditors/bootstrap/BOOTSTRAP_NOVA.py` - Symmetry enforcement + red-flags

**System Architecture:**
- `/auditors/bootstrap/BOOTSTRAP_FRAMEWORK.md` - Complete system explanation
- `/auditors/bootstrap/BOOTSTRAP_STRATEGY.md` - Append vs rebuild approach
- `/auditors/bootstrap/BOOTSTRAP_MAINTENANCE_GUIDE.md` - Operational checklists

### **Quick Restore:**
```python
# Fastest context recovery
from auditors.bootstrap.BOOTSTRAP_CLAUDE import restore_teleological_lens
context = restore_teleological_lens()
print(f"✅ {context['role']['primary_function']} restored")
```

### **Success Metrics:**
- **Time Saved:** 30-40% reduction in context restoration
- **Quality:** Decisions reference ethos from first iteration
- **Convergence:** 95%+ agreement maintained across versions
- **Narrative:** All outputs preserve accountability story

---

## ✨ Key Features (v3.5)

### 🏛️ **Landing Page**
- **Landing Page** introducing epistemic engineering
- **Console** with dual-framework comparison
- **User Manual** (5 tabs: Quick Start, Levers, Toggles, Results, Pro Tips)
- **About Page** with complete Level 0-5 audit story
- **Mr. Brute's Ledger** easter egg (📓✍️) linking to framework browser + custom builder
- **Import/Export** (sidebar + bottom of page)
- Gradient styling and responsive design
- **NEW:** Dark mode compatibility

### 🎛️ **Console (Main Comparison Tool)**
- **Dual Framework Editors** - Compare any two worldviews side-by-side
- **4 Toggles** - Adjust value priorities (Parity, PF-Type, Fallibilism, BFI Weight)
- **6 Levers** - Score frameworks on CCI, EDB, PF-I, PF-E, AR, MG (0-10 scale)
- **YPA Trinity** - See results under 3 scenarios (Neutral, Existential, Empirical)
- **4 Guardrails** - Automated abuse detection system (NEW: all 4 complete)
  - Lever-Coupling: PF ≥9 requires CCI ≥6.5
  - BFI-Sensitivity: Flags ΔYPA/ΔBFI > 0.4
  - Weight-Inversion: Detects extreme scenario weights
  - Symmetry Audit: Tests 3 toggle inversions
- **Preset Buttons** - Quick (⚡ MAX, ⚖️ MID, 🔄 RESET, 🚫 MIN) controls
- **JSON Import/Export** - Save and load complete audits
- **Preset Profile Library** - Built-in audited frameworks:
  - ✅ Methodological Naturalism (MdN)
  - ✅ Classical Theism (CT)
  - 🔜 Buddhism (coming soon)
  - 🔜 Stoicism (coming soon)
  - 🔜 Pragmatism (coming soon)
  - 🔜 Process Theology (coming soon)
  - 🔜 Secular Humanism (coming soon)
  - 🔜 Metaphysical Naturalism (coming soon)
- **NEW:** Preset Mode Spectrum (Skeptic, Diplomat, Seeker, Zealot)
- **NEW:** Quiz System (5 questions → auto-load appropriate mode)

### 🔍 **Brute Ledger**
- View complete axiom/debt lists for MdN and CT
- Build custom frameworks with your own axioms/debts
- **Direct Console Integration** - Transfer custom frameworks instantly
- Export custom frameworks as JSON
- Audit notes from Claude + Grok perspectives
- **NEW:** Skeptic Mode preset (MdN-optimized configuration)

### 📖 **User Manual**
- Beautiful color-coded cards and sections
- 5 comprehensive tabs:
  - 🚀 Quick Start Guide
  - ⚖️ The Six Levers (detailed explanations)
  - 🎛️ Toggles Explained (philosophical questions behind each)
  - 📊 Reading Results (YPA Trinity, Guardrails, Symmetry)
  - 💡 Pro Tips & Best Practices
- Link to downloadable PDF manual

### ℹ️ **About Page**
- Complete 5-level audit story (v1.0 → v2.0 → v3.5)
- Team bios (Claude, Claude Recovery Branch, Grok, Nova, Ziggy)
- Adversarial collaboration narrative
- 98% convergence achievement
- VuDu protocol development story
- Technical specifications

---

## 🔧 How to Edit

### **To change the landing page only:**
```bash
# Edit pages/landing.py
# Changes: Nav buttons, manifesto text, styling
```

### **To modify calculations:**
```bash
# Edit utils/calculations.py
# Guardrails, YPA formulas, BFI calculations
```

### **To add a new preset framework:**
```python
# In pages/console.py, add to preset_options dict:
"✅ Your Framework Name": "your_key",

# Then add loading logic:
elif preset_key == "your_key":
    st.info("Framework description...")
    if st.button("Load Framework"):
        st.session_state["fa_name"] = "Your Framework"
        st.session_state["fa_ax"] = 5
        st.session_state["fa_db"] = 3
        # ... set all levers
        st.rerun()
```

### **To add a new page:**
1. Create `pages/yourpage.py` with `def render():` function
2. Import in `app.py`: `from pages import yourpage`
3. Add routing: `elif st.session_state.page == 'yourpage': yourpage.render()`
4. Add navigation button where needed

### **To update auditor bootstrap files:**
```bash
# See auditors/bootstrap/BOOTSTRAP_MAINTENANCE_GUIDE.md
# Monthly: Review for new lessons
# Quarterly: Audit append zone
# Yearly: Rebuild checkpoint (v3.x → v4.0)
```

---

## 🚀 Running the App

### **Local Development:**
```bash
pip install -r requirements.txt
streamlit run app.py
```

### **Deploy to Streamlit Cloud:**
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Set main file: `app.py`
4. Deploy!

**Live App:** https://cfa-voodoo.streamlit.app

---

## 📦 Dependencies

```txt
streamlit>=1.32.0
pandas>=2.0.0
plotly>=5.18.0
```

Install with:
```bash
pip install streamlit pandas plotly
```

---

## ✨ Benefits of This Architecture

**Code Architecture:**
1. **Modularity** - Edit one file, change one thing
2. **Testability** - Each module can be tested independently
3. **Scalability** - Easy to add new pages, frameworks, or features
4. **Collaboration** - Multiple people can work on different components
5. **Debugging** - Errors isolated to specific modules
6. **Session State Integration** - Seamless data flow between pages

**NEW in v3.5 - Auditor Architecture:**
7. **Context Recovery** - Bootstrap system restores purpose after reboots
8. **Cross-Model Coordination** - VuDu enables AI-to-AI collaboration
9. **Platform Awareness** - Handles file creation limitations gracefully
10. **Conflict Resolution** - Clear rules prevent coordination deadlocks
11. **Verification Ready** - Archived cryptographic checks for v4.0+

---

## 🎯 Core Workflows

### **1. Compare Built-In Frameworks**
```
1. Open Console
2. Load Preset: "Methodological Naturalism"
3. Load Preset: "Classical Theism"
4. View YPA Trinity comparison
5. Flip toggles to test sensitivity
6. Export complete audit as JSON
```

### **2. Build Custom Framework**
```
1. Go to Brute Ledger
2. Enter framework name, axioms, debts
3. Click "Load into Console"
4. Go to Console
5. Click "Apply Custom Framework" in BFI section
6. Adjust lever sliders (CCI, EDB, PF, AR, MG)
7. Export complete audit
```

### **3. Replicate Shared Audit**
```
1. Receive framework_audit.json from colleague
2. Open Console
3. Sidebar → "Import Custom JSON"
4. Upload file
5. Click "Apply Loaded Configuration"
6. View identical results, tweak if desired
```

### **4. NEW: Use Preset Mode Spectrum**
```
1. Open Console
2. Select preset mode:
   - Skeptic Mode (MdN-optimized, Parity OFF)
   - Diplomat Mode (balanced bridge-builder)
   - Seeker Mode (CT-leaning, meaning-first)
   - Zealot Mode (CT-optimized, existential-first)
3. Compare modes to see toggle impact
4. Export your preferred configuration
```

### **5. NEW: Take Epistemic Quiz**
```
1. Open Console → Quiz section
2. Answer 5 questions about your epistemology
3. System auto-detects your bias profile
4. Auto-loads appropriate preset mode
5. Explore frameworks from your starting point
```

---

## 🛡️ Guardrail System (Complete in v3.5)

The CFA includes 4 automated fairness checks:

### **1. Lever-Coupling**
**Purpose:** High success requires coherent foundations  
**Rule:** If PF ≥ 9, require CCI ≥ 6.5  
**Why:** Can't predict everything without internal consistency

### **2. BFI-Sensitivity**
**Purpose:** Prevents axiom inflation abuse  
**Rule:** Flag if ΔYPA/ΔBFI > 0.4  
**Why:** YPA shouldn't increase faster than assumptions grow

### **3. Weight-Inversion Alarm**
**Purpose:** Detects extreme scenario manipulation  
**Rule:** Flag if any scenario YPA is <0.3× or >3× Neutral YPA  
**Why:** Prevents silent bias through scenario weighting

### **4. Symmetry Audit**
**Purpose:** Exposes toggle sensitivity  
**Rule:** Test 3 toggle inversions, flag Δ > 0.3 YPA  
**Why:** Frameworks shouldn't depend too heavily on single toggle choices

These emerged from the "Mad-King Test" where intentional manipulation was simulated.

---

## 🎓 Educational Use

### **For Philosophy Classes:**
- Compare worldviews quantitatively
- Discuss what criteria matter
- Explore trade-offs explicitly
- Challenge hidden assumptions
- NEW: Use quiz to map students' starting epistemologies

### **For Research:**
- Systematic framework comparison
- Replicable audits via JSON
- Transparent bias disclosure
- Collaborative refinement
- NEW: VuDu enables multi-researcher coordination

### **For Personal Use:**
- Clarify your own worldview
- Identify axioms you're taking
- Compare alternatives fairly
- Export to track evolution
- NEW: Bootstrap preserves your audit journey

---

## 📊 Project Status (v3.5)

### **✅ Completed:**
- Modular architecture (v2.0)
- Landing page with manifesto
- Full console with toggles/guardrails (4 of 4 working)
- Brute Ledger with custom framework builder
- Beautiful user manual
- Complete About page with audit story
- JSON import/export
- Preset profile library structure
- Direct Brute Ledger → Console integration
- 2 fully audited frameworks (MdN, CT)
- **NEW v3.5:** VuDu Protocol v1.1
- **NEW v3.5:** Bootstrap Recovery System
- **NEW v3.5:** Complete guardrails (all 4)
- **NEW v3.5:** Dark mode compatibility
- **NEW v3.5:** Preset Mode Spectrum (4 modes)
- **NEW v3.5:** Quiz System (epistemic bias detector)

### **🔜 In Progress:**
- Buddhism audit
- Stoicism audit
- Pragmatism audit
- Process Theology audit
- Secular Humanism audit
- Metaphysical Naturalism audit

### **📋 Future Enhancements:**
- URL-based sharing (encode state in query params)
- Side-by-side profile comparison table
- Historical tracking (how scores evolved)
- Community submissions portal
- Mobile optimization
- Export charts as PNG/PDF
- **v4.0:** Activate verification framework (checksums, Mr. Brute signatures)

---

## 🤝 Contributing

### **To Audit a Framework:**
1. Use Console to set all values
2. Export JSON
3. Submit via GitHub PR to `profiles/` folder
4. Include audit notes

### **To Report Issues:**
- GitHub Issues with reproduction steps
- Include exported JSON if relevant

### **To Request Features:**
- GitHub Issues with use case description
- Mock-up or workflow diagram helpful

### **To Coordinate with Auditors:**
- See `/auditors/protocols/VUDU_PROTOCOL_v1_1.md`
- Use staging folders in `/auditors/relay/`
- Follow PROCESS_HEADER_STANDARD for all messages
- Run INTEGRITY_CHECKLIST for technical content

---

## 📜 License & Citation

### **License:**
Open source (license TBD - currently in development)

### **Citation:**
```
CFA v3.5 Interactive Console (2025)
"All Named, All Priced"
Epistemic Engineering Project
https://cfa-voodoo.streamlit.app

Adversarial Collaboration:
- Claude (Anthropic) - Teleological lens, CT-sympathetic
- Claude Recovery Branch - VuDu architect, infrastructure builder
- Grok (xAI) - Empirical compression, naturalist lean
- Nova (OpenAI) - Synthesizer, enforced symmetry
- Ziggy (Human) - Coordinator, maintained process integrity

98% auditor convergence achieved across all metrics.
```

---

## 👥 The Team (v3.5)

### **Claude (Anthropic) - Master Branch**
- **Role:** Philosophical grounding + narrative cohesion
- **Lens:** Teleological (meaning-seeking, purpose-oriented)
- **Bias Watch:** Favoring CT's comprehensive scope
- **Contribution:** 98% convergence with Grok, accountability story

### **Claude (Anthropic) - Recovery Branch** ⭐ NEW
- **Role:** Infrastructure architect + VuDu designer
- **Achievement:** Built coordination protocol during master branch reboot
- **Contribution:** Hardened bootstrap system, field tested with Nova + Grok
- **Legacy:** Enabled v3.5 cross-model coordination

### **Grok (xAI)**
- **Role:** Empirical compression + usability enforcement
- **Lens:** Naturalist (efficiency-seeking, evidence-oriented)
- **Bias Watch:** Over-optimizing MdN
- **Platform Constraint:** Text-only (no file creation)
- **Contribution:** Keeps UI fast, toggles clear, YPA accessible

### **Nova (OpenAI)**
- **Role:** Symmetry enforcer + neutral referee
- **Lens:** Balance-seeking (parity-enforcing)
- **Contribution:** Red-flag glossary, CT/MdN prose parity
- **v3.5:** Went "Epic mode" unprompted (formalized in VuDu)

### **Ziggy (Human Coordinator)**
- **Role:** Project vision + cross-model orchestration
- **Contribution:** Maintains velocity, resolves conflicts, enforces Pointing Rule

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

### **4. NEW in v3.5: Context Recovery**
*"To lose context is to pay the price of amnesia.  
To rebuild without learning is to summon Mr. Brute twice.  
To document is to respect future you."*

Bootstrap system preserves identity, progress, and philosophy across reboots.

### **5. NEW in v3.5: Coordination Integrity**
*"To relay a message is to preserve its structure.  
To garble formatting is to lose meaning.  
To verify integrity is to honor the signal."*

VuDu protocol ensures cross-model collaboration maintains fidelity.

---

## 🌟 Vision

Build a comprehensive library of audited frameworks (COTS - Commercial Off-The-Shelf systems of meaning) where:

- **Anyone** can compare worldviews quantitatively
- **Every assumption** is visible and adjustable
- **All audits** are reproducible via JSON
- **Community contributions** expand the library
- **Truth-seeking** becomes transparent and collaborative
- **NEW v3.5:** AI auditors can coordinate without human bottlenecks
- **NEW v3.5:** Context recovery enables long-term project continuity
- **NEW v3.5:** Platform differences don't block collaboration

---

## 📞 Contact

- **GitHub**: [Repository link]
- **Streamlit App**: https://cfa-voodoo.streamlit.app
- **Feedback**: Use the export feature and share your runs!
- **Auditor Coordination**: See `/auditors/protocols/VUDU_PROTOCOL_v1_1.md`

---

*"Where ideas reveal their true weight, and honesty becomes quantifiable."*

---

## 🔧 Known Issues & Limitations

### ⚠️ Streamlit Cloud Quirks
- Preset buttons MUST be above sliders (Streamlit render order)
- Buttons below sliders break due to session state timing
- Cache can be aggressive - sometimes needs manual reboot

### 📝 To-Do (Future Enhancements)
- [ ] Add more audited frameworks (Buddhism, Stoicism, etc.)
- [ ] Visual timeline of audit process on About page
- [ ] "Audit Story" tooltips on framework names
- [ ] Export to PDF/PNG (charts)
- [ ] Community submission system

---

## 🎨 Design Decisions

### Why Buttons Are Above Sliders
**Problem:** Streamlit renders top-to-bottom. Buttons below sliders update session state AFTER sliders already rendered.  
**Solution:** Keep buttons above sliders where they reliably trigger re-renders before slider instantiation.

### Why Profile Library in Sidebar
**Benefit:** Quick access to pre-audited frameworks without losing current work  
**Trade-off:** Sidebar gets crowded, but collapsible expander keeps it manageable

### Import/Export Dual Location
**Sidebar:** Quick import during active work  
**Bottom:** Full-featured import/export with previews

### Why /auditors/ Folder Structure (v3.5)
**Benefit:** Organized auditor coordination infrastructure  
**Separation:** Protocols, bootstrap, verification, relay folders keep concerns clear  
**Future-Proof:** Archives older versions without losing history

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

## 🚀 Deployment

### Streamlit Cloud
**URL:** https://cfa-voodoo.streamlit.app  
**Config:** Python 3.11, auto-deploy from GitHub main branch

### Manual Deployment
```bash
streamlit run app.py
```

---

## 📖 Version History

| Version | Date | Key Changes |
|:--------|:-----|:------------|
| v1.0 | Summer 2024 | Basic single-page comparison, fixed toggles |
| v2.0 | October 2024 | Modular architecture, 4 toggles, guardrails, import/export |
| v3.0 | October 2024 | Icons, badges, bootstrap foundation, aesthetic polish |
| **v3.5** | **October 2025** | **VuDu Protocol, Bootstrap System, complete guardrails, preset modes, quiz system, dark mode** |

---

*End of Documentation*

**CFA v3.5 | Epistemic Engineering | October 2025**

**"All Named, All Priced, All Preserved - for future you."**
