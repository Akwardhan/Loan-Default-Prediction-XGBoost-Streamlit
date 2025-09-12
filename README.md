# Loan Risk Analysis – 1.3M Records + Streamlit App
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)  [![Live App](https://img.shields.io/badge/Streamlit-Live--App-brightgreen?logo=streamlit&logoColor=white)](https://loan-default-prediction-xgboost-app-lgccyltgxl9suauhmcuhqp.streamlit.app/) [![Google Colab](https://img.shields.io/badge/Built%20With-Google%20Colab-blue?logo=googlecolab&logoColor=white)]()

Conducted **end-to-end analysis** of 1.3M+ LendingClub loan records to uncover borrower risk patterns and support safer lending. Work included **data cleaning, anomaly detection, exploratory analysis, and insight reporting**, followed by building a **Streamlit app** that allows real-time borrower risk simulation for credit teams.

---

## 📌 Objective

To analyze loan applications, detect **high-risk borrowers**, and provide **data-driven recommendations** that reduce financial losses. Focus was on **cleaning, analysis, and actionable insights**, with a supportive model powering the risk simulation app.

---

## 📦 Dataset Summary

- **Source:** LendingClub public dataset  
- **Final Size:** ~1.3M records × 86 features  
- **Target Classes:**  
  - Fully Paid → `0`  
  - Charged Off (Default) → `1`  
- Dropped intermediate statuses like "Current", "Late", etc.

---

## 📊 Exploratory Data Analysis (EDA)

| Feature        | Key Insight                                                                 |
|----------------|------------------------------------------------------------------------------|
| 💰 Loan Amount | Defaults skewed higher (median ₹12L vs ₹9.5L for paid)                      |
| 💳 Income      | Lower-income borrowers showed higher default probability                    |
| 📈 DTI         | DTI > 35% strongly correlated with default                                   |
| 🔎 FICO Score  | FICO < 660 had 4× higher default risk                                        |
| 🛒 Purpose     | Small business/vacation loans showed 3× default rates                        |
| ⏱️ Term        | 60-month loans defaulted 2× more than 36-month terms                        |
| 📉 Interest    | Higher interest rates aligned with higher default likelihood                |

---

## 🛠️ Data Cleaning & Preprocessing

- Removed leakage and ID-like fields (`recoveries`, `desc`, `member_id`)
- Handled nulls using domain logic (median for `dti`, mode for `term`)
- Dropped low-signal or high-missing-value columns
- One-hot encoded categorical features (`purpose`, `home_ownership`, `term`)
- Scaled numeric features (`loan_amnt`, `int_rate`, `dti`)
- Addressed class imbalance (~20% defaults) with weighting

---

## 🚀 Streamlit App – Real-Time Risk Simulation

Created a **dashboard-style app** in Streamlit to simulate loan applications and display borrower risk.

### 🎯 Inputs:
- Loan Amount, Term, Annual Income  
- FICO Score, DTI, Interest Rate  
- Purpose, Home Ownership  

### 📈 Outputs:
- Prediction: **Default** / **Fully Paid**
- Default Probability: e.g., **76.43%**

## 🚀 Live Streamlit App

🔗 **Try the live app here:** [Loan Risk Predictor – Streamlit](https://loan-default-prediction-xgboost-app-lgccyltgxl9suauhmcuhqp.streamlit.app/)

📸 ![Live Model](https://github.com/Akwardhan/Loan-Default-Prediction-XGBoost-Streamlit/blob/main/Loan%20%20Fraud%20Model.png)  
📸 ![Output](https://github.com/Akwardhan/Loan-Default-Prediction-XGBoost-Streamlit/blob/main/Output%20of%20Loan%20Fraud.png)

---

## 🤖 Supporting Model

A predictive model was included to **power the app** and demonstrate how analysis can scale:

| Metric | Logistic Regression | Random Forest | XGBoost ✅ |
|--------|---------------------|----------------|------------|
| Accuracy | 80.1% | 79.7% | 79.7% |
| Precision (Class 1) | 0.51 | 0.46 | 0.46 |
| Recall (Class 1) | 0.07 | 0.09 | 0.09 ✅ |
| F1-Score (Class 1) | 0.12 | 0.15 | 0.15 ✅ |

✅ **XGBoost** was chosen to reduce false negatives and provide consistent results for the risk tool.

---

## 💼 Business Impact

This analytics project enabled:

✅ **Early identification** of high-risk borrowers  
✅ **Data-backed loan approvals**  
✅ Reduced **default-related revenue loss**  
✅ A **shareable dashboard** for non-technical stakeholders  

---

## 🧠 Tools & Technologies

- Python: pandas, numpy, scikit-learn, XGBoost  
- Streamlit: interactive app  
- Jupyter & Google Colab: analysis environment  
- Matplotlib, Seaborn: visualization  
- Git, GitHub: version control  

---

## 🔗 Dataset Reference

- 📂 [LendingClub Loan Data – Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)

---

## 📌 Author

**Anmol Kirtiwardhan**  
🌐 Portfolio: [akwardhan.github.io](https://akwardhan.github.io)
