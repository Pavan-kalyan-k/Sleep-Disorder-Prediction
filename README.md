# 🛌 Sleep Disorder Prediction App

The application is deployed at: https://sleep-disorder-prediction-ml.streamlit.app/

## 📋 Features

- **Interactive Prediction Interface:** Input your health information to get instant sleep disorder predictions
- **Multiple Sleep Categories:** Predicts Normal sleep, Insomnia, or Sleep Apnea
- **Confidence Scores:** View prediction probabilities for each class
- **Health Recommendations:** Get personalized health tips based on predictions
- **Model Information:** Learn about the model's architecture and performance
- **Pre-trained Model:** Automatically trains and caches the model on first run

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Navigate to the project directory:**
   ```bash
   cd c:\Users\91939\Desktop\Project
   ```

2. **Install required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Place your dataset:** 
   - Copy `Sleep_health_and_lifestyle_dataset.csv` to the project directory
   - The app will automatically train the model on first run

## 🚀 Running the App

1. **Start the Streamlit server:**
   ```bash
   streamlit run app.py
   ```

2. **Access the app:**
   - The app will automatically open in your default web browser
   - Usually available at: `http://localhost:8501`

3. **If it doesn't open automatically:**
   - Open your browser and go to `http://localhost:8501`

## 📊 How to Use

### Making a Prediction
1. Go to the **"🔮 Make Prediction"** tab (default view)
2. Enter your health information:
   - Age
   - Sleep Duration (hours)
   - Quality of Sleep (1-10)
   - Heart Rate (bpm)
   - Stress Level (1-10)
   - Physical Activity Level (1-100)
   - Gender
   - Occupation
   - BMI Category
   - Blood Pressure
3. Click the **"🔍 Predict"** button
4. View your prediction and health recommendations

### Viewing Model Information
1. Click on the **"📈 Model Information"** tab in the sidebar
2. See model details, features used, and usage guidelines

## 📁 Project Structure

```
Project/
├── app.py                                    # Main Streamlit app
├── requirements.txt                          # Python dependencies
├── Sleep_health_and_lifestyle_dataset.csv   # Training dataset (required)
├── sleep_model.pkl                          # Saved model (auto-generated)
├── label_encoders.pkl                       # Saved encoders (auto-generated)
└── README.md                                 # This file
```

## 🎯 Model Details

- **Algorithm:** Logistic Regression (Multi-class)
- **Classes:** Normal, Insomnia, Sleep Apnea
- **Training Method:** GridSearchCV with SMOTE for class balancing
- **Cross-Validation:** Stratified K-Fold (5 splits)
- **Features:** 10 health and lifestyle metrics

## 🔧 Troubleshooting

### Error: "Dataset file not found"
- Ensure `Sleep_health_and_lifestyle_dataset.csv` is in the same directory as `app.py`

### Error: "Module not found"
- Run: `pip install -r requirements.txt`
- Make sure all packages are installed

### Slow first run
- The first run will train the model, which may take 2-3 minutes
- Subsequent runs will be much faster as the model is cached

### Port already in use
- Run: `streamlit run app.py --server.port 8502`
- This will use port 8502 instead

## 📚 Dataset Columns

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
- Sleep Disorder (target variable)

## 🤝 Contributing

Feel free to improve the model, add new features, or enhance the UI!

## 📝 License

This project is provided as-is for educational purposes.

---

**Created with ❤️ using Streamlit and scikit-learn**
