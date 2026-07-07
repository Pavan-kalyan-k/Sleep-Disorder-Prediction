# 🚀 Quick Start Guide

## 📝 Prerequisites
Before you start, you need:
1. **Python 3.8+** - Download from https://www.python.org/
2. **Dataset file** - `Sleep_health_and_lifestyle_dataset.csv` in the project folder
3. **Pip** - Usually comes with Python

---

## ⚡ Quick Setup (2 minutes)

### Option 1: Using Batch File (Windows) ✅ EASIEST
1. Navigate to: `c:\Users\91939\Desktop\Project\`
2. **Double-click** `run_app.bat`
3. Wait for the browser to open automatically
4. Done! 🎉

### Option 2: Using Command Prompt
1. Open Command Prompt (Win + R, type `cmd`, press Enter)
2. Navigate to the project folder:
   ```
   cd c:\Users\91939\Desktop\Project
   ```
3. Install packages:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

### Option 3: Using PowerShell
1. Open PowerShell
2. Navigate to project folder:
   ```powershell
   cd c:\Users\91939\Desktop\Project
   ```
3. Install packages:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the app:
   ```powershell
   streamlit run app.py
   ```

---

## ✅ Verification Checklist

Before running, make sure you have:
- [ ] Python 3.8 or higher installed
- [ ] `Sleep_health_and_lifestyle_dataset.csv` in the project folder
- [ ] All files in `c:\Users\91939\Desktop\Project\`:
  - app.py
  - requirements.txt
  - run_app.bat
  - README.md
  - .streamlit/config.toml

---

## 🎯 First Run - What to Expect

**First Run (1-2 minutes):**
- The app will train the model from scratch
- You'll see: "📚 Training model... This may take a moment"
- Model and encoders will be saved for next time

**Subsequent Runs (< 5 seconds):**
- The app will load the saved model instantly
- You'll see: "✅ Model loaded from cache"

---

## 🔗 Access Your App

Once running, you'll see:
```
You can now view your Streamlit app in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.x.x:8501
```

**Automatically opens in default browser** at `http://localhost:8501`

---

## 🎮 Using the App

### Make a Prediction:
1. Slide and select your health metrics
2. Click "🔍 Predict"
3. Get instant predictions with health tips

### View Model Info:
1. Click "📈 Model Information" in the sidebar
2. Learn how the model works

---

## 🛑 Stopping the App

- Press `Ctrl + C` in the command prompt/terminal
- Or close the terminal window

---

## ❓ Common Issues & Fixes

### Issue: "Python is not installed"
**Solution:** 
- Install Python from https://www.python.org/
- Make sure to check "Add Python to PATH" during installation
- Restart command prompt after installation

### Issue: "Dataset file not found"
**Solution:**
- Rename your notebook data file to: `Sleep_health_and_lifestyle_dataset.csv`
- Place it in: `c:\Users\91939\Desktop\Project\`

### Issue: "ModuleNotFoundError: No module named 'streamlit'"
**Solution:**
- Run: `pip install -r requirements.txt`
- Make sure pip is updated: `pip install --upgrade pip`

### Issue: "Port 8501 is already in use"
**Solution:**
- Close other Streamlit apps or use a different port:
  ```
  streamlit run app.py --server.port 8502
  ```

### Issue: "No module named 'sklearn'"
**Solution:**
- Run: `pip install scikit-learn`

---

## 📊 Dataset Requirements

Your `Sleep_health_and_lifestyle_dataset.csv` should have these columns:
- Person ID
- Age
- Sleep Duration
- Quality of Sleep
- Heart Rate
- Stress Level
- Physical Activity Level
- Gender
- Occupation
- BMI Category
- Blood Pressure
- Sleep Disorder

---

## 💡 Tips & Tricks

1. **Share Your App Online:**
   - Deploy to Streamlit Cloud (free): https://streamlit.io/cloud
   - Upload your project to GitHub
   - Connect it to Streamlit Cloud
   - Share the link with anyone!

2. **Improve Model Accuracy:**
   - Collect more training data
   - Add more health features
   - Try different algorithms (Random Forest, SVM, XGBoost)

3. **Customize the App:**
   - Edit colors in `.streamlit/config.toml`
   - Modify features and thresholds in `app.py`
   - Add your own health recommendations

---

## 📞 Need Help?

1. Check the full README.md for detailed information
2. Visit: https://docs.streamlit.io/
3. Check Python/scikit-learn documentation

---

