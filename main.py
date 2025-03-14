


import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Health Insurance Cost Predictor", layout="wide")

# Custom CSS for refined design
st.markdown("""
    <style>
        .stTextInput>div>div>input, .stSelectbox>div>div>select, .stNumberInput>div>div>input {
            border-radius: 10px;
            padding: 8px;
            font-size: 16px;
        }
        .stButton>button {
            background-color: #204F79;
            color: white;
            border-radius: 8px;
            padding: 12px 20px;
            font-size: 18px;
            font-weight: bold;
            width: 60%;
            display: block;
            margin: auto;
            transition: 0.3s;
        }
        .stButton>button:hover {
            background-color: #163A5F;
        }
        .custom-heading {
            text-align: center;
            font-size: 20px;
            font-weight: bold;
            color: #204F79;
            padding: 5px;
            background-color: #E6F0FA;
            border-radius: 5px;
        }
        .bold-label {
            font-weight: bold;
            font-size: 16px;
        }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #204F79;'>Health Insurance Cost Predictor</h1>", unsafe_allow_html=True)

# Dictionary to store inputs
input_dict = {}

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("<p class='custom-heading'>Personal Details</p>", unsafe_allow_html=True)
    input_dict["Age"] = st.number_input("**Age**", min_value=18, max_value=100, value=18, step=1)
    input_dict["Genetical Risk"] = st.number_input("**Genetical Risk**", min_value=0, max_value=10, value=0, step=1)
    input_dict["Gender"] = st.selectbox("**Gender**", ["Male", "Female"])
    input_dict["Smoking Status"] = st.selectbox("**Smoking Status**", ["Regular", "Occasional", "Non Smoker"])

with col2:
    st.markdown("<p class='custom-heading'>Insurance Details</p>", unsafe_allow_html=True)
    input_dict["Number of Dependants"] = st.number_input("**Number of Dependents**", min_value=0, max_value=10, value=0, step=1)
    input_dict["Insurance Plan"] = st.selectbox("**Insurance Plan**", ["Bronze", "Silver", "Gold"])
    input_dict["Marital Status"] = st.selectbox("**Marital Status**", ["Unmarried", "Married"])
    input_dict["Region"] = st.selectbox("**Region**", ["Northwest", "Northeast", "Southwest", "Southeast"])

with col3:
    st.markdown("<p class='custom-heading'>Financial & Health Info</p>", unsafe_allow_html=True)
    input_dict["Income in Lakhs"] = st.number_input("**Income in Lakhs**", min_value=0, max_value=100, value=0, step=1)
    input_dict["Employment Status"] = st.selectbox("**Employment Status**", ["Salaried", "Self-Employed", "Freelancer"])
    input_dict["BMI Category"] = st.selectbox("**BMI Category**", ["Underweight", "Normal", "Overweight", "Obese"])
    input_dict["Medical History"] = st.selectbox("**Medical History**", [
        "No Disease", "Diabetes", "High blood pressure",
        "Diabetes & High blood pressure", "Thyroid",
        "Heart disease", "High blood pressure & Heart disease",
        "Diabetes & Thyroid", "Diabetes & Heart disease"
    ])

# Center the Predict button and Predicted Premium
st.markdown("<br>", unsafe_allow_html=True)
col_center = st.columns([1, 2, 1])

with col_center[1]:
    if st.button("Predict"):
        prediction = predict(input_dict)
        formatted_prediction = f"₹{prediction:,.2f}"  # Format as currency with commas
        st.markdown(f"""
            <div style="text-align: center; font-size: 22px; font-weight: bold; color: #204F79; padding: 10px; border: 2px solid #204F79; border-radius: 10px; background-color: #E6F0FA;">
                Predicted Premium: {formatted_prediction}
            </div>
        """, unsafe_allow_html=True)
