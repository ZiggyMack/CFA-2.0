# CFA v2.0 - Interactive Console [Modular Architecture]
## "All Named, All Priced" - Epistemic Engineering Platform

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cfa-voodoo.streamlit.app)

---

## 🎯 What is CFA v2.0?

The **Comparative Framework Audit (CFA)** is the first interactive epistemic laboratory built to measure how worldviews hold their ground under pressure. It makes hidden assumptions visible, prices every presupposition, and allows users to see how their value choices affect framework comparisons.

**Core Innovation**: Every assumption is disclosed, every presupposition is counted, every bias is made toggleable, and every outcome is earned.
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

**Why This Matters:**
This 98% convergence is the project's credibility. Solo audits hide bias - adversarial checking makes scores trustworthy.

---
---

## ✨ Key Features

### 🏛️ **Landing Page**
-  **Landing Page** introducing epistemic engineering
-  **Console** with dual-framework comparison
-  **User Manual** (4 tabs: Quick Start, Toggle Guide, Results, Full Docs)
-  **About Page**
-  **Mr. Brute's Ledger** easter egg (📓✍️) linking to Brute Ledger (framework browser + custom builder)
-  **Import/Export** (sidebar + bottom of page)
- Gradient styling and responsive design

### 🎛️ **Console (Main Comparison Tool)**
- **Dual Framework Editors** - Compare any two worldviews side-by-side
- **4 Toggles** - Adjust value priorities (Parity, PF-Type, Fallibilism, BFI Weight)
- **6 Levers** - Score frameworks on CCI, EDB, PF, AR, MG (0-10 scale)
- **YPA Trinity** - See results under 3 scenarios (Neutral, Existential, Empirical)
- **4 Guardrails** - Automated abuse detection system
- **Symmetry Audit** - Toggle sensitivity analysis
- **Preset Buttons** - Quick (⚡ MAX, ⚖️ MID, 🔄 RESET, 🚫 MIN) controls for both frameworks
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
 
  ### ✅ Preset Library
- Methodological Naturalism (MdN) - fully audited
- Classical Theism (CT) - fully audited
- 6 frameworks "coming soon"

### 🔍 **Brute Ledger**
- View complete axiom/debt lists for MdN and CT
- Build custom frameworks with your own axioms/debts
- **Direct Console Integration** - Transfer custom frameworks instantly
- Export custom frameworks as JSON
- Audit notes from Claude + Grok perspectives

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
- Complete 4-level audit story (v1.0 → v2.0)
- Team bios (Claude, Grok, Grant, Nova, Ziggy)
- Adversarial collaboration narrative
- 98% convergence achievement
- Technical specifications

---

## 📁 Project Structure

```
cfa_app/
├── app.py                      # Main entry point (page router)
├── utils/
│   ├── __init__.py
│   ├── calculations.py         # Math/scoring logic (YPA, BFI, guardrails)
│   ├── visualizations.py       # Plotly charts (lever comparison, YPA trinity)
│   └── frameworks.py           # Default framework configs (MdN, CT)
└── pages/
    ├── __init__.py
    ├── landing.py              # Landing page with manifesto
    ├── console.py              # Main console (enhanced with imports/presets)
    ├── manual.py               # Beautiful user manual with colored cards
    ├── about.py                # Complete audit story
    └── brute_ledger.py         # Axiom/debt viewer + custom framework builder
```

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
# All pages using calculations update automatically
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

### **To update a chart:**
```bash
# Edit utils/visualizations.py
# All pages using that chart update automatically
```

### **To add a new page:**
1. Create `pages/yourpage.py` with `def render():` function
2. Import in `app.py`: `from pages import yourpage`
3. Add routing: `elif st.session_state.page == 'yourpage': yourpage.render()`
4. Add navigation button where needed

---

## 🚀 Running the App

### **Local Development:**
```bash
cd cfa_app
pip install -r requirements.txt
streamlit run app.py
```

### **Deploy to Streamlit Cloud:**
1. Push to GitHub
2. Connect to Streamlit Cloud
3. Set main file: `app.py`
4. Deploy!

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

1. **Modularity** - Edit one file, change one thing
2. **Testability** - Each module can be tested independently
3. **Scalability** - Easy to add new pages, frameworks, or features
4. **Collaboration** - Multiple people can work on different components
5. **Debugging** - Errors isolated to specific modules
6. **Session State Integration** - Seamless data flow between pages

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

---

## 🎨 Customization Guide

### **Change Colors:**
Edit CSS in individual page files:
```python
st.markdown("""
    <style>
    .main-title {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    }
    </style>
""", unsafe_allow_html=True)
```

### **Add Toggle:**
1. Add to sidebar in `console.py`:
   ```python
   new_toggle = st.sidebar.selectbox("New Toggle", ["ON", "OFF"])
   ```
2. Add to config dict:
   ```python
   cfg = {..., "new_toggle": new_toggle}
   ```
3. Update calculations in `utils/calculations.py` to use it

### **Modify Guardrails:**
Edit `utils/calculations.py`:
```python
def new_guardrail(framework, config):
    # Your logic here
    return True, "PASS: Description"
```

---

## 📚 Framework Audit Guide

### **To Audit a New Framework:**

1. **Research Phase**
   - Identify unprovable axioms
   - List unresolved questions (debts)
   - Score on 6 levers (0-10 scale)

2. **Documentation**
   ```python
   NEW_FRAMEWORK = {
       "name": "Framework Name",
       "bf_i": {"axioms": X, "debts": Y},
       "levers": {
           "CCI": Z,
           "EDB": Z,
           "PF_instrumental": Z,
           "PF_existential": Z,
           "AR": Z,
           "MG": Z
       },
       "admits_limits": True/False
   }
   ```

3. **Add to Preset Library**
   - Update `console.py` preset_options
   - Change 🔜 to ✅
   - Add loading logic

4. **Export Template**
   ```bash
   # Save as profiles/framework_name.json
   # Share with community
   ```

---

## 🔄 Data Flow Architecture

```
┌─────────────────────────────────────────────────────────┐
│  BRUTE LEDGER PAGE                                      │
│  • Build custom framework                               │
│  • Click "Load into Console"                           │
│  • Stores in st.session_state                          │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ↓ (session_state transfer)
┌─────────────────────────────────────────────────────────┐
│  CONSOLE PAGE                                           │
│  • Detects custom_framework_ready                       │
│  • Shows "Apply" button in BFI section                 │
│  • User adjusts sliders                                │
│  • Calculates YPA                                      │
│  • Exports complete JSON                               │
└─────────────────┬───────────────────────────────────────┘
                  │
                  ↓ (JSON file)
┌─────────────────────────────────────────────────────────┐
│  EXTERNAL SHARING                                       │
│  • Save to GitHub/Drive                                │
│  • Share with colleagues                               │
│  • Import back via "Import JSON"                       │
└─────────────────────────────────────────────────────────┘
```

---

## 🛡️ Guardrail System

The CFA includes 4 automated fairness checks:

1. **Lever-Coupling** - High PF (≥9) requires high CCI (≥6.5)
2. **BFI-Sensitivity** - Flags suspicious efficiency (ΔYPA/ΔBFI > 0.4)
3. **Weight-Inversion** - Detects extreme scenario weights (<0.3× or >3×)
4. **Symmetry Audit** - Tests 3 toggle inversions, flags Δ > 0.3 YPA

These emerged from the "Mad-King Test" where intentional manipulation was simulated.

---

## 🎓 Educational Use

### **For Philosophy Classes:**
- Compare worldviews quantitatively
- Discuss what criteria matter
- Explore trade-offs explicitly
- Challenge hidden assumptions

### **For Research:**
- Systematic framework comparison
- Replicable audits via JSON
- Transparent bias disclosure
- Collaborative refinement

### **For Personal Use:**
- Clarify your own worldview
- Identify axioms you're taking
- Compare alternatives fairly
- Export to track evolution

---

## 🐛 Troubleshooting

### **Import errors:**
```bash
# Make sure __init__.py files exist:
touch utils/__init__.py
touch pages/__init__.py

# Run from cfa_app directory:
cd cfa_app
streamlit run app.py
```

### **Page not updating:**
```python
# Clear cache:
st.cache_data.clear()

# Or restart:
streamlit run app.py --server.runOnSave true
```

### **Session state issues:**
```python
# Debug with:
st.write(st.session_state)

# Reset manually:
for key in list(st.session_state.keys()):
    del st.session_state[key]
```

### **Emojis not rendering:**
- Ensure UTF-8 encoding
- Check terminal supports Unicode
- Use `# -*- coding: utf-8 -*-` at top of file

---

## 📊 Project Status

### **✅ Completed:**
- Modular architecture
- Landing page with manifesto
- Full console with toggles/guardrails
- Brute Ledger with custom framework builder
- Beautiful user manual
- Complete About page with audit story
- JSON import/export
- Preset profile library structure
- Direct Brute Ledger → Console integration
- 2 fully audited frameworks (MdN, CT)

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
- Dark mode

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

---

## 📜 License & Citation

### **License:**
Open source (license TBD - currently in development)

### **Citation:**
```
CFA v2.0 Interactive Console (2025)
"All Named, All Priced"
Epistemic Engineering Project
https://cfa-voodoo.streamlit.app

Adversarial Collaboration:
- Claude (Anthropic) - Teleological lens, CT-sympathetic
- Grok (xAI) - Empirical compression, naturalist lean
- Grant - Skeptic, demanded justification
- Nova - Synthesizer, enforced symmetry
- Ziggy - Coordinator, maintained process integrity

98% auditor convergence achieved across all metrics.
```

---

## 🎯 Core Principles

1. **Transparency Over Neutrality**
   - Perfect neutrality is impossible
   - Every comparison assumes something
   - Make all assumptions explicit and adjustable

2. **The Pointing Rule**
   - "To name your brute is to pay your fee"
   - "To deny you have one is to summon him twice"
   - Every presupposition must be acknowledged and priced

3. **Symmetry Testing**
   - All frameworks measured under identical configurations
   - Toggle impacts must be disclosed and bounded
   - Asymmetries reveal structural differences, not hidden bias

---

## 🌟 Vision

Build a comprehensive library of audited frameworks (COTS - Commercial Off-The-Shelf systems of meaning) where:

- **Anyone** can compare worldviews quantitatively
- **Every assumption** is visible and adjustable
- **All audits** are reproducible via JSON
- **Community contributions** expand the library
- **Truth-seeking** becomes transparent and collaborative

---

## 📞 Contact

- **GitHub**: [Repository link]
- **Streamlit App**: https://cfa-voodoo.streamlit.app
- **Feedback**: Use the export feature and share your runs!

---

*"Where ideas reveal their true weight, and honesty becomes quantifiable."*

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

## 📖 Citation

```
CFA v2.0 Interactive Console (2025)
"All Named, All Priced"
Epistemic Engineering Project
https://cfa-voodoo.streamlit.app
```

---

## 👥 Credits

**Adversarial Collaboration:**
- Claude (Anthropic) - Teleological lens, CT-sympathetic
- Grok (xAI) - Empirical compression, naturalist lean
- Nova - Synthesizer, enforced symmetry
- Ziggy - Coordinator, process integrity

**The Pointing Rule:** "To name your brute is to pay your fee. To deny you have one is to summon him twice."

---

*End of Milestone Documentation*

**CFA v2.0 | Epistemic Engineering | October 2025**
