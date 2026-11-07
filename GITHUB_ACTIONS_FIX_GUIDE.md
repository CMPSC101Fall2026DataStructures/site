# GitHub Actions Workflow Fix Guide for Quarto + GitHub Pages

## Overview
This document outlines the changes made to fix Quarto website builds and deployments to GitHub Pages. These issues were:
1. **DeprecationWarning: The `punycode` module is deprecated** - Node.js runtime compatibility issue
2. **404 Not Found error** - Invalid Quarto version parameter
3. **deployment_queued status** - Deployment queue blocking issue

All these issues have been resolved and can be applied to similar Quarto websites.

---

## Problems and Solutions

### Problem 1: punycode Module Deprecation Warning
**Symptom:** Build warning with message about Node.js's deprecated `punycode` module
```
DeprecationWarning: The `punycode` module is deprecated. Please use a userland alternative instead.
```

**Root Cause:** Quarto uses Node.js internally for rendering, but the GitHub Actions environment wasn't explicitly configured with a compatible Node.js version.

**Solution:** Add explicit Node.js setup step before Quarto setup.

---

### Problem 2: 404 Error When Downloading Quarto
**Symptom:** Workflow fails with HTTP 404 error when downloading Quarto
```
HTTP request sent, awaiting response... 404 Not Found
2026-11-06 17:11:24 ERROR 404: Not Found.
```

**Root Cause:** The version parameter `'latest'` is not a valid value for `quarto-dev/quarto-actions/setup@v2`. The action tried to construct a URL with `vlatest` which doesn't exist.

**Solution:** Remove the `version` parameter to use the default behavior (latest stable release).

---

### Problem 3: Deployment Queued Status
**Symptom:** Deployment gets stuck in `deployment_queued` status and doesn't complete
```
Current status: deployment_queued
Getting Pages deployment status...
Current status: deployment_queued
```

**Root Cause:** Multiple deployments were queuing up due to `cancel-in-progress: false` setting, and the deploy action wasn't timing out properly.

**Solution:** Enable `cancel-in-progress` and add explicit timeouts.

---

## Changes to Make

### File: `.github/workflows/deploy.yml`

#### Change 1: Update concurrency settings
**Location:** Top of the workflow, in the `concurrency` section

**Before:**
```yaml
concurrency:
  group: "pages"
  cancel-in-progress: false
```

**After:**
```yaml
concurrency:
  group: "pages"
  cancel-in-progress: true
```

**Why:** Setting `cancel-in-progress` to `true` prevents multiple deployments from queuing. If you push changes rapidly, newer deployments will cancel older ones, preventing the `deployment_queued` bottleneck.

---

#### Change 2: Add Node.js setup step
**Location:** In the `jobs.build.steps` section, after "Setup Python" step and before "Setup Quarto" step

**Add this new step:**
```yaml
      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'
```

**Why:** Explicitly configures Node.js v20 (a stable, recent version) before running Quarto. This resolves the `punycode` deprecation warning since Node.js v20 has better compatibility with Quarto's dependencies.

---

#### Change 3: Simplify Quarto setup
**Location:** In the `jobs.build.steps` section, the "Setup Quarto" step

**Before:**
```yaml
      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2
        with:
          version: 'release'
```

**After:**
```yaml
      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2
```

**Why:** Removes the `version: 'release'` parameter. The action's default behavior automatically downloads the latest stable release, avoiding any 404 errors from invalid version strings.

---

#### Change 4: Add timeout to deploy job
**Location:** In the `jobs.deploy` section

**Before:**
```yaml
  deploy:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
```

**After:**
```yaml
  deploy:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    timeout-minutes: 10
    
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
```

**Why:** The `timeout-minutes: 10` setting ensures that if GitHub Pages is slow or hung, the deployment won't wait indefinitely.

---

#### Change 5: Add timeout to deploy-pages action
**Location:** In the `jobs.deploy.steps` section, the "Deploy to GitHub Pages" step

**Before:**
```yaml
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
```

**After:**
```yaml
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
        with:
          timeout: 600000
```

**Why:** Adds an explicit timeout parameter (600,000 milliseconds = 10 minutes) to the action itself for additional protection against deployment hangs.

---

## Complete Fixed Workflow

Here's the complete corrected `.github/workflows/deploy.yml` file for reference:

```yaml
name: Build and Deploy Quarto Site with JupyterLite

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

concurrency:
  group: "pages"
  cancel-in-progress: true

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Setup Quarto
        uses: quarto-dev/quarto-actions/setup@v2

      - name: Install Python dependencies
        run: |
          python -m pip install --upgrade pip
          pip install jupyter jupyterlite-core jupyterlite-pyodide-kernel
          pip install numpy pandas matplotlib seaborn plotly scikit-learn scipy statsmodels

      - name: Render Quarto site
        run: |
          quarto render

      - name: Build JupyterLite
        run: |
          python -m jupyterlite_core.app build --contents live/content --output-dir docs/live

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: docs

  deploy:
    if: github.ref == 'refs/heads/main'
    needs: build
    runs-on: ubuntu-latest
    timeout-minutes: 10
    
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    
    steps:
      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
        with:
          timeout: 600000
```

---

## Step-by-Step Application to Another Repository

1. **Navigate to your other Quarto website repository**

2. **Open `.github/workflows/deploy.yml`** (create it if it doesn't exist)

3. **Make the 5 changes outlined above:**
   - Change `cancel-in-progress` to `true`
   - Add Node.js setup step
   - Remove version parameter from Quarto setup
   - Add `timeout-minutes: 10` to deploy job
   - Add `timeout: 600000` to deploy-pages action

4. **Commit and push the changes:**
   ```bash
   git add .github/workflows/deploy.yml
   git commit -m "fix: Apply Quarto/GitHub Pages workflow fixes

   - Setup Node.js 20 explicitly for Quarto compatibility
   - Remove invalid Quarto version parameter
   - Enable cancel-in-progress to prevent deployment queuing
   - Add timeouts to prevent deployment hangs"
   
   git push
   ```

5. **Verify the workflow runs successfully** on GitHub Actions

---

## Expected Results

After applying these changes, you should see:
- ✅ No `DeprecationWarning` about the `punycode` module
- ✅ Quarto setup completes without 404 errors
- ✅ Deployment completes without getting stuck in `deployment_queued` status
- ✅ Site successfully builds and deploys to GitHub Pages with custom domain

---

## Testing the Fix

1. Push a change to the `main` branch of your other repository
2. Go to the **Actions** tab on GitHub
3. Watch the workflow run through all steps
4. Confirm:
   - Build job completes successfully
   - Deploy job moves to `in_progress` and then completes
   - GitHub Pages URL shows the updated site

---

## Notes

- These changes are compatible with Quarto websites that include JupyterLite (as shown in the workflow)
- If your other website doesn't use JupyterLite, you can omit the "Build JupyterLite" step, but the Node.js and Quarto setup changes should still be applied
- Node.js v20 is a stable LTS version and is recommended for production deployments
- The timeouts (10 minutes) are generous and should accommodate even slow GitHub Pages deployments

