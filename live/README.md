# JupyterLite Configuration for CMPSC 101

This directory contains the JupyterLite setup for the Data Science course, providing an in-browser Python and R environment.

## 🚀 What is JupyterLite?

JupyterLite is a Jupyter environment that runs entirely in the browser, requiring no server infrastructure. Students can:
- Write and execute Python code
- Create notebooks with rich markdown
- Use data science libraries (pandas, numpy, matplotlib, etc.)
- Learn and experiment without installations

## 📦 Installing Packages

### Python Packages
JupyterLite uses Pyodide, which supports many Python packages. To install packages in your notebooks:

```python
import micropip
await micropip.install('package-name')
```

**Commonly available packages:**
- numpy
- pandas
- matplotlib
- seaborn
- plotly
- scikit-learn
- scipy
- statsmodels

**Note:** Not all PyPI packages work in the browser. Only packages with pure Python or WASM-compatible wheels are supported.

### Pre-configured Packages
The `requirements.txt` file lists recommended packages. Users should install them on-demand using micropip as shown above.

## 🛠️ Building JupyterLite

To build and deploy JupyterLite:

1. Install jupyterlite:
   ```bash
   pip install jupyterlite-core
   pip install jupyterlite-pyodide-kernel
   ```

2. Build the site:
   ```bash
   jupyter lite build --output-dir docs/live
   ```

3. The built site will be in `docs/live/` and can be served via GitHub Pages.

## 📚 Adding Content

### Adding Python Packages
Edit `jupyter-lite.json` to add packages to the PyPI environment.

### Adding Example Notebooks
Place `.ipynb` files in `live/content/` directory.

## 🔧 Configuration Files

- **jupyter_lite_config.json**: Build-time configuration
- **jupyter-lite.json**: Runtime configuration for the JupyterLite app
- **requirements.txt**: List of recommended packages (installed on-demand by users)

### Custom Configuration
Modify `jupyter_lite_config.json` for advanced settings.

## 🔗 Access

Once deployed, students can access JupyterLite at:
`https://your-github-username.github.io/repo-name/live/`

Or via the navigation menu: **JupyterLite** tab

## 📝 Usage Instructions for Students

1. Click the **JupyterLite** link in the navigation
2. Wait for the environment to load (first load may take 30-60 seconds)
3. Create a new notebook: File → New → Notebook
4. Choose Python kernel
5. Start coding!

## ⚠️ Important Notes

- **All data is stored in browser**: Work is saved in browser local storage
- **Download your work**: Use File → Download to save notebooks
- **Package limitations**: Some packages may not work in the browser environment
- **Performance**: Large datasets may be slow compared to desktop Jupyter

## 🆘 Troubleshooting

**JupyterLite not loading?**
- Clear browser cache
- Try a different browser (Chrome/Firefox recommended)
- Disable browser extensions that block JavaScript

**Package not available?**
- Check if the package is pure Python (no C dependencies)
- Request addition in Discord or GitHub Issues

**Work disappeared?**
- Check Downloads folder (you may have downloaded it)
- Check browser local storage settings
- Always keep backups of important work!

---

For more information, visit [JupyterLite Documentation](https://jupyterlite.readthedocs.io/)
