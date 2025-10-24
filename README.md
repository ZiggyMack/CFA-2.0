# CFA v2.0 - Interactive Console [Modular Architecture]

## 🎯 Problem Solved
No more recompiling everything for small changes! Each component is now its own file.

## 📁 Project Structure

```
cfa_app/
├── app.py                      # Main entry point (thin orchestrator)
├── utils/
│   ├── __init__.py
│   ├── calculations.py         # All math/scoring logic
│   ├── visualizations.py       # All Plotly charts
│   └── frameworks.py           # Default framework configs
└── pages/
    ├── __init__.py
    ├── landing.py              # Landing page
    ├── console.py              # Main console/comparison tool
    ├── manual.py               # User manual
    └── about.py                # About page
```

## 🔧 How to Edit

### To change the landing page only:
1. Edit `pages/landing.py`
2. Run `streamlit run app.py`
3. Changes are isolated - no risk of breaking other pages

### To modify calculations:
1. Edit `utils/calculations.py`
2. All pages using calculations update automatically

### To add a new framework:
1. Add to `utils/frameworks.py`
2. Framework immediately available in console

### To update a chart:
1. Edit `utils/visualizations.py`
2. All pages using that chart update

## 🚀 Running the App

```bash
cd cfa_app
streamlit run app.py
```

## 📦 Dependencies

```bash
pip install streamlit pandas plotly
```

## ✨ Benefits of This Structure

1. **Modularity** - Edit one file, change one thing
2. **Testability** - Each module can be tested independently
3. **Scalability** - Easy to add new pages or utilities
4. **Collaboration** - Multiple people can work on different files
5. **Debugging** - Errors isolated to specific modules

## 🎨 Customization Tips

### Change colors:
- Edit the CSS in individual page files
- Or create a `utils/styles.py` for shared styling

### Add a new page:
1. Create `pages/newpage.py`
2. Add `def render():` function
3. Import in `app.py`
4. Add navigation button

### Modify scoring:
- All in `utils/calculations.py`
- Test changes without touching UI code

## 📝 Example: Adding Buddhism Framework

```python
# In utils/frameworks.py
BUDDHISM_DEFAULT = {
    "name": "Buddhism",
    "bf_i": {"axioms": 5, "debts": 3},
    "levers": {
        "CCI": 8.5,
        "EDB": 8.0,
        # ... rest of config
    },
    "admits_limits": True
}

# Add to FRAMEWORK_TEMPLATES dict
FRAMEWORK_TEMPLATES["Buddhism"] = BUDDHISM_DEFAULT
```

That's it! No other files need changing.

## 🔄 Migration from Monolithic App

If you have the old single-file `app.py`:
1. Backup your current `app.py`
2. Replace with this modular version
3. All functionality preserved, just better organized

## 🐛 Troubleshooting

**Import errors?**
- Make sure `__init__.py` files exist in each package
- Run from the `cfa_app` directory

**Page not updating?**
- Streamlit caches aggressively
- Use `st.cache_data.clear()` or restart server

**Emojis not rendering?**
- Ensure file encoding is UTF-8
- Check terminal supports Unicode

## 📚 Next Steps

1. ✅ Landing page fixed and modular
2. ⏳ Create other page modules (console, manual, about)
3. ⏳ Add more frameworks
4. ⏳ Enhanced visualizations
5. ⏳ Export/import functionality
