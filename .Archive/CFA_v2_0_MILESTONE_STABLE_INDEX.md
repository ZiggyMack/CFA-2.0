# 📦 CFA v2.0 MILESTONE - Archive Index

**Archive:** `CFA_v2.0_MILESTONE_STABLE.tar.gz`
**Size:** 2.3 MB
**Date:** October 24, 2025
**Status:** Production Ready ✅

---

## 📋 Contents

### 📄 Documentation (5 files)
1. **README.md** - Complete project overview, features, design decisions
2. **CHANGELOG.md** - Version history and bug fixes
3. **DEPLOYMENT.md** - Step-by-step deployment guide
4. **CFA_v2.0_Manual.pdf** - Full technical white paper (1.4 MB)
5. **requirements.txt** - Python dependencies

### 💻 Application Files (4 files)
1. **app.py** - Main router (32 KB)
2. **console.py** - Comparison console with all features (21 KB)
3. **landing.py** - Landing page with manifesto (7.7 KB)
4. **brute_ledger.py** - Framework browser + builder (16 KB)

---

## 🎯 What's Working

### Core Features
✅ Multi-page navigation (Landing, Console, Manual, About, Brute Ledger)
✅ Dual-framework comparison with 6 levers each
✅ 4 configuration toggles (Parity, PF-Type, Fallibilism, BFI-Weight)
✅ YPA Trinity scenarios (Neutral/Existential/Empirical)
✅ Visual charts (Plotly)
✅ Preset Profile Library (MdN, CT + 6 coming soon)
✅ Import/Export (JSON)
✅ Per-framework quick adjust buttons (MAX/MID/RESET/MIN)
✅ Guardrails & Symmetry audits

### Audited Frameworks
✅ **Methodological Naturalism (MdN)** - YPA 3.62 (Neutral)
✅ **Classical Theism (CT)** - YPA 3.65 (Neutral)
- 98% convergence between Claude & Grok auditors

---

## 🚀 Quick Deploy

### Extract Archive
```bash
tar -xzf CFA_v2.0_MILESTONE_STABLE.tar.gz
cd CFA_v2.0_MILESTONE_STABLE
```

### Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

### Deploy to Streamlit Cloud
1. Upload files to GitHub repo
2. Connect at share.streamlit.io
3. Set main file: `app.py`
4. Deploy!

---

## 📊 File Breakdown

| File | Purpose | Size | Critical? |
|------|---------|------|-----------|
| app.py | Main entry point | 32 KB | ⚠️ YES |
| console.py | Core functionality | 21 KB | ⚠️ YES |
| landing.py | First impression | 7.7 KB | ✅ Important |
| brute_ledger.py | Framework tools | 16 KB | ✅ Important |
| requirements.txt | Dependencies | 47 B | ⚠️ YES |
| README.md | Overview | 4 KB | 📖 Docs |
| CHANGELOG.md | History | 1.6 KB | 📖 Docs |
| DEPLOYMENT.md | Setup guide | 3.5 KB | 📖 Docs |
| CFA_v2.0_Manual.pdf | Full specs | 1.4 MB | 📖 Reference |

---

## 🔑 Key Files Explained

### app.py (MUST NOT EDIT)
- Page router
- Default framework definitions (MdN, CT)
- Core math functions
- Session state initialization

**⚠️ Note:** This file imports from pages. If you need to modify functionality, edit the page files instead!

### console.py (MAIN WORKSPACE)
- All comparison logic
- Slider controls
- Preset buttons (position critical: MUST be above sliders)
- Import/Export UI
- Charts and visualizations

### landing.py
- Manifesto display
- Navigation to other pages
- Mr. Brute easter egg button

### brute_ledger.py
- Framework browser (MdN/CT tabs)
- Custom framework builder
- Axiom/Debt tracking
- Export to console functionality

---

## ⚠️ Known Constraints

### Streamlit Render Order
**Issue:** Preset buttons break when placed BELOW sliders
**Reason:** Session state updates happen after slider render
**Solution:** Keep buttons ABOVE sliders (current stable position)

### Deployment Caching
**Issue:** Changes sometimes don't appear immediately
**Solution:** Reboot app in Streamlit Cloud dashboard

---

## 📈 Next Steps (Post-Milestone)

### Planned Enhancements
- [ ] Audit Buddhism framework
- [ ] Audit Stoicism framework
- [ ] Add "Audit Story" tooltips
- [ ] Export charts as PNG/PDF
- [ ] Community submission system
- [ ] Visual audit timeline

### Optional Improvements
- [ ] Dark mode toggle
- [ ] Mobile-responsive layout
- [ ] Keyboard shortcuts
- [ ] Comparison history
- [ ] Share link generator

---

## 🎓 Learning Resources

**New to CFA?**
1. Read README.md first
2. Read CFA_v2.0_Manual.pdf (comprehensive theory)
3. Try console with defaults (MdN vs CT)
4. Experiment with toggles
5. Build custom framework in Brute Ledger

**Want to Contribute?**
1. Read DEPLOYMENT.md
2. Fork repo
3. Make changes
4. Test locally
5. Submit pull request

---

## 📞 Support & Contact

**Bug Reports:** Check DEPLOYMENT.md → Common Issues
**Questions:** See CFA_v2.0_Manual.pdf
**Suggestions:** Open GitHub issue (if repo public)

**Live App:** https://cfa-voodoo.streamlit.app

---

## 🏆 Milestone Achievement

This archive represents a **stable, production-ready** version of CFA v2.0 with:
- ✅ All core features implemented
- ✅ Known bugs fixed
- ✅ Two complete framework audits
- ✅ Full documentation
- ✅ Deployment tested

**You can confidently:**
- Deploy this to production
- Share with collaborators
- Use as teaching tool
- Build new frameworks
- Extend with additional features

---

*"All Named, All Priced" — The CFA v2.0 Promise*

**End of Index**
