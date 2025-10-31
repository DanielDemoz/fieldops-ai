# GitHub Repository Setup

## Upload Project to GitHub

### Step 1: Create GitHub Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the "+" icon in the top right corner
3. Select "New repository"
4. Name your repository: `fieldops-ai`
5. Add a description: "Smart scheduling and job costing platform for field service operations"
6. Choose visibility (public or private)
7. Do not initialize with README, .gitignore, or license (we already have these)
8. Click "Create repository"

### Step 2: Initialize Git in Your Project

Open terminal/command prompt in your project directory and run:

```bash
cd "C:\Users\asbda\FieldOp AI"
git init
```

### Step 3: Add All Files

```bash
git add .
```

### Step 4: Create Initial Commit

```bash
git commit -m "Initial commit - FieldOps AI platform"
```

### Step 5: Connect to GitHub Repository

Replace `your-username` with your GitHub username:

```bash
git remote add origin https://github.com/DanielDemoz/fieldops-ai.git
```

### Step 6: Push to GitHub

```bash
git branch -M main
git push -u origin main
```

## Updating the Repository

After making changes:

```bash
git add .
git commit -m "Description of changes"
git push
```

## Repository Settings

After uploading, consider:

1. Go to repository Settings
2. Add topics/tags: `field-service`, `scheduling`, `construction`, `automation`
3. Add repository description
4. Enable Issues (for bug tracking)
5. Enable Wiki (for additional documentation)

## Files Included in Repository

- Source code (app/, database/, services/, utils/)
- Documentation (README.md, QUICKSTART.md, etc.)
- Configuration files (config.py, requirements.txt)
- Demo HTML page (demo.html)
- .gitignore (excludes database files, cache, etc.)

## Files Excluded

- fieldops.db (database file)
- __pycache__/ (Python cache)
- invoices/ (generated PDFs)
- .env (environment variables)

These are listed in `.gitignore` and will not be uploaded.

