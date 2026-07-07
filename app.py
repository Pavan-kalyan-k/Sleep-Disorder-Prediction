import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split, GridSearchCV, StratifiedKFold, cross_val_score
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from imblearn.over_sampling import SMOTE
import pickle
import os

# Set page config
st.set_page_config(page_title="Sleep Disorder Predictor", layout="wide")

st.title("🛌 Sleep Disorder Prediction Model")
st.markdown("---")

# Load or train model
@st.cache_resource
def load_or_train_model():
    model_path = "sleep_model.pkl"
    encoder_path = "label_encoders.pkl"
    classes_path = "encoder_classes.pkl"
    features_path = "feature_names.pkl"
    
    if os.path.exists(model_path) and os.path.exists(encoder_path) and os.path.exists(classes_path) and os.path.exists(features_path):
        with open(model_path, 'rb') as f:
            model = pickle.load(f)
        with open(encoder_path, 'rb') as f:
            encoders = pickle.load(f)
        with open(classes_path, 'rb') as f:
            encoder_classes = pickle.load(f)
        with open(features_path, 'rb') as f:
            feature_names = pickle.load(f)
        # st.success("✅ Model loaded from cache")
        return model, encoders, encoder_classes, feature_names
    else:
        st.info("📚 Training model... This may take a moment")
        
        # Load dataset
        try:
            df = pd.read_csv(r"C:\Users\91939\Downloads\Sleep_health_and_lifestyle_dataset.csv")
        except FileNotFoundError:
            st.error("⚠️ Dataset file 'Sleep_health_and_lifestyle_dataset.csv' not found!")
            st.stop()
        
        # Store original categories before encoding
        categorical_col = ['Gender', 'Occupation', 'BMI Category', 'Blood Pressure']
        encoder_classes = {col: df[col].unique().tolist() for col in categorical_col}
        
        # Data preparation
        df['Sleep Disorder'] = df['Sleep Disorder'].fillna("Normal")
        df.drop("Person ID", axis=1, inplace=True)
        df['BMI Category'] = df['BMI Category'].replace("Normal Weight", "Normal")
        
        # Re-capture classes after modifications
        encoder_classes['BMI Category'] = df['BMI Category'].unique().tolist()
        
        # Encoding
        encoders = {}
        
        for col in categorical_col:
            le = LabelEncoder()
            df[col] = le.fit_transform(df[col])
            encoders[col] = le
        
        # Prepare train-test split
        x = df.drop('Sleep Disorder', axis=1)
        y = df["Sleep Disorder"]
        
        # Store feature names for later use
        feature_names = x.columns.tolist()
        
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=20)
        
        # SMOTE for class imbalance
        smote = SMOTE(random_state=42)
        x_train_smote, y_train_smote = smote.fit_resample(x_train, y_train)
        
        # Grid Search for best parameters
        param_grid = {
            'C': [0.01, 0.1, 1, 10, 100],
            'penalty': ['l2', 'l1'],
            'solver': ['lbfgs', 'newton-cg', 'sag', 'saga'],
            'max_iter': [50, 100, 200, 300, 400, 500],
            'random_state': [10, 20, 30, 50, 40]
        }
        
        grid = GridSearchCV(
            LogisticRegression(),
            param_grid=param_grid,
            cv=5,
            scoring='accuracy',
            n_jobs=-1,
            verbose=0
        )
        
        grid.fit(x_train_smote, y_train_smote)
        model = grid.best_estimator_
        
        # Save model, encoders, and encoder classes
        with open(model_path, 'wb') as f:
            pickle.dump(model, f)
        with open(encoder_path, 'wb') as f:
            pickle.dump(encoders, f)
        with open(classes_path, 'wb') as f:
            pickle.dump(encoder_classes, f)
        with open(features_path, 'wb') as f:
            pickle.dump(feature_names, f)
        
        st.success("✅ Model trained and saved successfully!")
        return model, encoders, encoder_classes, feature_names

# Load model
model, encoders, encoder_classes, feature_names = load_or_train_model()

# Sidebar for navigation
st.sidebar.header("📊 Navigation")
page = st.sidebar.radio("Choose a page:", ["🔮 Make Prediction", "📈 Model Information"])

if page == "🔮 Make Prediction":
    st.header("Make a Sleep Disorder Prediction")
    st.markdown("Enter your health information below:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        age = st.slider("Age (years)", 18, 80, 30)
        sleep_duration = st.slider("Sleep Duration (hours)", 3.0, 12.0, 7.0, step=0.1)
        heart_rate = st.slider("Heart Rate (bpm)", 50, 120, 75)
        
    with col2:
        stress_level = st.slider("Stress Level (1-10)", 1, 10, 5)
        quality_of_sleep = st.slider("Quality of Sleep (1-10)", 1, 10, 7)
        physical_activity_level = st.slider("Physical Activity Level (1-100)", 1, 100, 6)
        daily_steps = st.slider("Daily Steps", 1000, 20000, 8000, step=100)
    
    col3, col4 = st.columns(2)
    
    with col3:
        gender = st.selectbox("Gender", sorted(encoder_classes['Gender']))
        occupation = st.selectbox("Occupation", sorted(encoder_classes['Occupation']))
    
    with col4:
        bmi_category = st.selectbox("BMI Category", sorted(encoder_classes['BMI Category']))
        blood_pressure = st.selectbox("Blood Pressure", sorted(encoder_classes['Blood Pressure']))
    
    # Create input dataframe
    if st.button("🔍 Predict", use_container_width=True):
        try:
            # Encode categorical features with validation
            try:
                gender_encoded = encoders['Gender'].transform([gender])[0]
                occupation_encoded = encoders['Occupation'].transform([occupation])[0]
                bmi_encoded = encoders['BMI Category'].transform([bmi_category])[0]
                bp_encoded = encoders['Blood Pressure'].transform([blood_pressure])[0]
            except ValueError as e:
                st.error(f"❌ Invalid input value: {str(e)}. Please select from the available options.")
                st.stop()
            
            # Create a dictionary with all encoded features
            input_data = {
                'Age': age,
                'Sleep Duration': sleep_duration,
                'Quality of Sleep': quality_of_sleep,
                'Heart Rate': heart_rate,
                'Stress Level': stress_level,
                'Physical Activity Level': physical_activity_level,
                'Daily Steps': daily_steps,
                'Gender': gender_encoded,
                'Occupation': occupation_encoded,
                'BMI Category': bmi_encoded,
                'Blood Pressure': bp_encoded
            }
            
            # Create DataFrame with features in the same order as training
            input_df = pd.DataFrame([input_data])
            
            # Reorder columns to match training data
            input_df = input_df[feature_names]
            
            # Make prediction
            prediction = model.predict(input_df)[0]
            probabilities = model.predict_proba(input_df)[0]
            
            # Display results
            st.markdown("---")
            st.subheader("🎯 Prediction Result")
            
            col1, col2 = st.columns(2)
            
            with col1:
                if prediction == "Normal":
                    st.success(f"### Predicted Sleep Status: **{prediction}** ✅")
                else:
                    st.warning(f"### Predicted Sleep Status: **{prediction}** ⚠️")
            
            with col2:
                st.info("### Confidence Scores:")
                for i, class_name in enumerate(model.classes_):
                    st.metric(label=class_name, value=f"{probabilities[i]*100:.1f}%")
            
            # Health tips
            st.markdown("---")
            st.subheader("💡 Health Recommendations:")
            
            if prediction == "Normal":
                st.success("""
                ✅ Your sleep patterns are normal. Keep maintaining:
                - Consistent sleep schedule
                - Physical activity regularly
                - Manage stress levels
                - Avoid screens before bed
                """)
            elif prediction == "Insomnia":
                st.warning("""
                ⚠️ You may have signs of Insomnia. Recommendations:
                - Establish a consistent bedtime routine
                - Reduce caffeine intake, especially in the evening
                - Try relaxation techniques (meditation, deep breathing)
                - Consider consulting a sleep specialist
                - Limit screen time before bed
                """)
            else:  # Sleep Apnea
                st.error("""
                🚨 You may have signs of Sleep Apnea. Recommendations:
                - **Consult a sleep specialist immediately**
                - Get a sleep apnea test (polysomnography)
                - Avoid sleeping on your back
                - Maintain healthy weight
                - Avoid alcohol before bedtime
                - Sleep apnea can be serious - professional evaluation is recommended
                """)
                
        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

elif page == "📈 Model Information":
    st.header("Model Performance & Information")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Model Details")
        st.info(f"""
        **Model Type:** Logistic Regression (Multi-class)
        **Training Method:** GridSearchCV with SMOTE
        **Classes:** Normal, Insomnia, Sleep Apnea
        **Cross-Validation:** Stratified K-Fold (5 splits)
        """)
    
    with col2:
        st.subheader("📋 Features Used")
        features_list = [
            "Age",
            "Sleep Duration",
            "Quality of Sleep",
            "Heart Rate",
            "Stress Level",
            "Physical Activity Level",
            "Daily Steps",
            "Gender (encoded)",
            "Occupation (encoded)",
            "BMI Category (encoded)",
            "Blood Pressure (encoded)"
        ]
        for i, feat in enumerate(features_list, 1):
            st.write(f"{i}. {feat}")
    
    st.markdown("---")
    st.subheader("ℹ️ How to Use This Model")
    st.write("""
    1. **Enter Your Information:** Go to the "Make Prediction" tab and input your health details
    2. **Get Prediction:** Click the "Predict" button to see your sleep disorder prediction
    3. **Review Results:** See the predicted status and confidence scores
    4. **Follow Recommendations:** Get personalized health recommendations based on your prediction
    """)

st.markdown("---")
# st.markdown("*Built with ❤️ using Streamlit | Sleep Health & Lifestyle Dataset*")
