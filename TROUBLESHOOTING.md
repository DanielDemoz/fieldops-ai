# Troubleshooting Guide

## Issue: Connection Refused / Can't Reach localhost:8501

### Solution 1: Verify Streamlit is Running

Run this command in your terminal:
```bash
py -m streamlit run app/dashboard.py
```

**What to expect:**
- You should see output like:
```
  You can now view your Streamlit app in your browser.
  Local URL: http://localhost:8501
```

- If you see an error, note what it says

### Solution 2: Check if Port is Already in Use

If you see "Address already in use":
1. Streamlit is already running
2. Open http://localhost:8501 in your browser
3. Or try: http://localhost:8502 (next available port)

### Solution 3: Verify All Files Exist

Make sure these files are in the correct locations:
```
FieldOp AI/
├── app/
│   └── dashboard.py  ← Must exist!
├── database/
├── services/
└── utils/
```

### Solution 4: Test Imports First

Run the test script:
```bash
py test_dashboard.py
```

If this fails, fix the import errors before running Streamlit.

### Solution 5: Run from Correct Directory

Make sure you're in the project root directory:
```bash
cd "C:\Users\asbda\FieldOp AI"
py -m streamlit run app/dashboard.py
```

### Solution 6: Check Windows Firewall

If still not working:
1. Windows might be blocking the connection
2. Allow Python through Windows Firewall
3. Or temporarily disable firewall to test

### Solution 7: Try Different Port

Manually specify a port:
```bash
py -m streamlit run app/dashboard.py --server.port 8502
```

Then open: http://localhost:8502

## Common Errors

### "ModuleNotFoundError: No module named 'streamlit'"
**Fix:** 
```bash
py -m pip install streamlit
```

### "File does not exist: app/dashboard.py"
**Fix:** 
1. Make sure you're in the project root
2. Check the file exists: `dir app\dashboard.py`
3. Run: `py -m streamlit run "app\dashboard.py"` (with quotes)

### "ImportError: cannot import name..."
**Fix:**
```bash
py -m pip install -r requirements.txt
```

Or install individually:
```bash
py -m pip install streamlit pandas plotly sqlalchemy faker
```

## Still Not Working?

1. **Check Python version:**
   ```bash
   py --version
   ```
   Should be Python 3.8 or higher

2. **Reinstall Streamlit:**
   ```bash
   py -m pip uninstall streamlit
   py -m pip install streamlit
   ```

3. **Run with verbose output:**
   ```bash
   py -m streamlit run app/dashboard.py --logger.level=debug
   ```

4. **Check for error messages** in the terminal output and share them

