import streamlit as st
import joblib
import pandas as pd
import os
st.write("Files in working directory:", os.listdir())


model = joblib.load('loan_default_model.pkl')
features = joblib.load('feature_names.pkl')

st.title("Loan Default Prediction App")
st.write("Enter loan details to predict default probability:")

numeric_cols = ['loan_amnt', 'annual_inc', 'installment', 'dti', 'int_rate']

user_input = {}


term_option = st.selectbox("Loan Term", ["36 months", "60 months"])
user_input['term_ 36 months'] = 1 if term_option == "36 months" else 0
user_input['term_ 60 months'] = 1 if term_option == "60 months" else 0


for col in features:
    if col in ['term_ 36 months', 'term_ 60 months']:
        continue  
    label = col.replace('_', ' ').title()

    if col in numeric_cols:
        user_input[col] = st.number_input(label, value=0.0)
    else:
        user_input[col] = st.checkbox(label)


input_df = pd.DataFrame([user_input], columns=features)


if st.button("Predict", key="predict_btn"):
    pred = model.predict(input_df)[0]
    prob = model.predict_proba(input_df)[0][1]

    st.markdown(f"## Prediction: {'Default' if pred == 1 else 'Fully Paid'}")
    st.markdown(f"### Default Probability: {prob:.2%}")
