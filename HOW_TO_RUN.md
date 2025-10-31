# How to Run the Dashboard

## 📍 Where to Run the Command

You need to run the command from the **project root directory**:
```
C:\Users\asbda\FieldOp AI
```

## ✅ Method 1: Use the Batch File (Easiest!)

**Simply double-click:** `START_STREAMLIT.bat`

This automatically:
- Changes to the correct directory
- Checks if the file exists
- Starts Streamlit

## ✅ Method 2: Run from Command Line

### Step 1: Open Command Prompt or PowerShell

### Step 2: Navigate to the project folder

**In Command Prompt:**
```cmd
cd "C:\Users\asbda\FieldOp AI"
```

**In PowerShell:**
```powershell
cd "C:\Users\asbda\FieldOp AI"
```

### Step 3: Verify you're in the right place

You should see files like:
- `app/` folder
- `database/` folder  
- `run_demo.py`
- `requirements.txt`

**Check with:**
```cmd
dir app
```
You should see `dashboard.py` in that folder.

### Step 4: Run Streamlit

```cmd
py -m streamlit run app\dashboard.py
```

Or if using forward slashes:
```cmd
py -m streamlit run app/dashboard.py
```

## ✅ Method 3: Quick Start from Anywhere

If you're not sure what directory you're in:

```cmd
cd "C:\Users\asbda\FieldOp AI"
py -m streamlit run "app\dashboard.py"
```

The quotes help with paths that have spaces.

## 🔍 Troubleshooting

### Error: "File does not exist: app/dashboard.py"

**Solution:** You're not in the project root directory.

**Fix:**
1. Navigate to: `C:\Users\asbda\FieldOp AI`
2. Then run: `py -m streamlit run app\dashboard.py`

### How to Check Your Current Directory

**In Command Prompt:**
```cmd
cd
```
This shows your current directory.

**In PowerShell:**
```powershell
Get-Location
```

### Verify the File Exists

Run this to check:
```cmd
dir app\dashboard.py
```

If you see "File Not Found", you're in the wrong directory!

## 📍 Correct Directory Structure

You should be in a directory that contains:
```
FieldOp AI/           ← YOU SHOULD BE HERE
├── app/
│   └── dashboard.py  ← The file Streamlit needs
├── database/
├── services/
├── utils/
└── run_demo.py
```

## 🚀 Quick Reference

**Current Directory:** `C:\Users\asbda\FieldOp AI`

**Command to Run:**
```cmd
py -m streamlit run app\dashboard.py
```

**Expected Output:**
```
You can now view your Streamlit app in your browser.
Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

Then open **http://localhost:8501** in your browser!

