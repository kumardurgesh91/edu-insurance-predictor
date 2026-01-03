import streamlit as st
import pickle
import numpy as np
import pickle
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Medical Insurance Predictor",
    page_icon="🏥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for background and styling
st.markdown(
    """
    <style>
    .stApp::before {
        content: "";
        background-image: url("https://images.unsplash.com/photo-1559757148-5c350d0d3c56?ixlib=rb-4.0.3&auto=format&fit=crop&w=1920&q=80");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        opacity: 0.3;
        z-index: -1;
    }
    .stApp {
        background: none;
    }
    .main {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 10px;
        margin: 20px;
    }
    .stTitle {
        color: #2E8B57;
        text-align: center;
        font-size: 3em;
        font-weight: bold;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 10px 20px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 5px;
    }
    .stSuccess {
        background-color: #D4EDDA;
        color: #155724;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #C3E6CB;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the model
with open('medical_insurance_model.pkl', 'rb') as file:
    package = pickle.load(file)

model = package["model"]
scaler = package["scaler"]
print(package["columns"])

# App title
st.markdown('<h1 class="stTitle">🏥 Medical Insurance Cost Prediction</h1>', unsafe_allow_html=True)
st.markdown("### Predict your medical insurance costs with our AI-powered tool! 💡")

# Important Disclaimer
st.error("⚠️ **IMPORTANT DISCLAIMER: This is a TEST/DEMO Project Only**")
st.warning("""
**Please Read Carefully:**

🔸 **This application is for educational and demonstration purposes only**  
🔸 **Trained on a small dataset with limited records**  
🔸 **Predictions may not be accurate or reliable**  
🔸 **DO NOT use this for real medical insurance decisions**  
🔸 **Consult with qualified insurance professionals for actual quotes**  
🔸 **This is not a substitute for professional financial/medical advice**

**Dataset Info:** The model was trained on approximately 1,338 records from a public insurance dataset, which may not represent all demographics or current market conditions.
""")

st.markdown("---")

# Default values
default_age = 19
default_sex = "female"
default_bmi = 27.9
default_children = 0
default_smoker = "yes"
default_region = "southwest"

# Create columns for inputs
col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("👤 Personal Information")
    age_input = st.number_input("Age", min_value=0, max_value=100, value=default_age, step=1)
    gender = st.selectbox("Sex", ["male", "female"], index=1 if default_sex == "female" else 0)

with col2:
    st.subheader("⚖️ Health Metrics")
    bmi_input = st.slider("BMI", min_value=10.0, max_value=50.0, value=default_bmi, step=0.1)
    smoker_input = st.selectbox("Smoker", ["no", "yes"], index=1 if default_smoker == "yes" else 0)

with col3:
    st.subheader("👨‍👩‍👧‍👦 Family Details")
    children_input = st.number_input("Number of Children", min_value=0, max_value=10, value=default_children, step=1)
    selected_region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"], index=3 if default_region == "southwest" else 0)

# Process region dummies
region_nw = 1 if selected_region == "northwest" else 0
region_se = 1 if selected_region == "southeast" else 0
region_sw = 1 if selected_region == "southwest" else 0

# Prepare input data
input_data = {
    'age': age_input,
    'sex': 1 if gender == "male" else 0,
    'bmi': bmi_input,
    'children': children_input,
    'smoker': 1 if smoker_input == "yes" else 0,
    'region_northwest': region_nw,
    'region_southeast': region_se,
    'region_southwest': region_sw
}

# Convert to array for prediction
input_array = np.array(list(input_data.values())).reshape(1, -1)

# Predict button in center
st.markdown("---")
col1, col2, col3 = st.columns([1, 1, 1])
with col2:
    if st.button("🔮 Predict Insurance Cost", use_container_width=True):
        input_df = pd.DataFrame([input_data])
        print(input_df)
        
        # Scale the input
        input_scaled = scaler.transform(input_df)
        prediction = model.predict(input_scaled)
        st.success(f"💰 Predicted Insurance Cost: **${prediction[0]:.2f}** per year")
        st.balloons()