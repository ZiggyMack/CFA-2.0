# CFA v2.0 - MILESTONE: STABLE BUILD
**Date:** October 24, 2025
**Status:** Production Ready

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

**Why This Matters:**
This 98% convergence is the project's credibility. Solo audits hide bias - adversarial checking makes scores trustworthy.

---

## 🎯 What's Working

### ✅ Complete Features
1. **Landing Page** with Launch Manifesto
2. **Console** with dual-framework comparison
3. **User Manual** (4 tabs: Quick Start, Toggle Guide, Results, Full Docs)
4. **About Page**
5. **Mr. Brute's Ledger** (framework browser + custom builder)
6. **Import/Export** (sidebar + bottom of page)

### ✅ Console Functionality
- Per-framework preset buttons (⚡ MAX, ⚖️ MID, 🔄 RESET, 🚫 MIN)
- 6 levers per framework (CCI, EDB, PF-I, PF-E, AR, MG)
- BFI tracking (Axioms + Debts)
- 4 toggles (Lever-Parity, PF-Type, Fallibilism, BFI-Weight)
- YPA Trinity (Neutral/Existential/Empirical scenarios)
- Visual charts (Lever Comparison + YPA Trinity)
- Guardrails & Symmetry audits

### ✅ Preset Library
- Methodological Naturalism (MdN) - fully audited
- Classical Theism (CT) - fully audited
- 6 frameworks "coming soon"

---

## 📁 File Structure

```
/
├── app.py                      # Main router (DO NOT EDIT - use pages/)
├── pages/
│   ├── landing.py             # Landing page with manifesto
│   ├── console.py             # Main comparison console
│   ├── manual.py              # User manual (4 tabs)
│   ├── about.py               # About CFA v2.0
│   └── brute_ledger.py        # Mr. Brute's Ledger
├── utils/
│   ├── calculations.py        # Core YPA math
│   ├── visualizations.py      # Plotly charts
│   └── frameworks.py          # Default profiles (MdN, CT)
└── requirements.txt           # Dependencies
```

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
