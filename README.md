# Loan Default Prediction – XGBoost Model + Streamlit App
[![Python](https://img.shields.io/badge/Python-3.10-blue)](https://www.python.org/)  [![Live App](https://img.shields.io/badge/Streamlit-Live--App-brightgreen?logo=streamlit&logoColor=white)](https://loan-default-prediction-xgboost-app-lgccyltgxl9suauhmcuhqp.streamlit.app/)  [![AWS S3](https://img.shields.io/badge/Data%20Hosted%20on-AWS%20S3-orange?logo=amazonaws&logoColor=white)](https://s3.console.aws.amazon.com/s3/object/loan-default-cleaned-dataset/cleaned_loan_data.csv) [![Google Colab](https://img.shields.io/badge/Built%20With-Google%20Colab-blue?logo=googlecolab&logoColor=white)]()



Built a high-scale loan default prediction system on 1.3M+ LendingClub records. Includes feature-rich preprocessing, class imbalance handling, model benchmarking, and XGBoost-based deployment. A production-ready Streamlit web app allows real-time borrower risk assessment to support financial decision-making.

---

## 📌 Objective

To predict whether a borrower will **fully repay** or **default** on a loan, using key financial, credit, and application data. The goal is to reduce loan loss risk by detecting defaulters early and supporting data-backed approval workflows.

---

## 📦 Dataset Summary

- **Source:** LendingClub public dataset  
- **Final Size:** ~1.3M records × 86 features  
- **Target Classes:**  
  - Fully Paid → `0`  
  - Charged Off → `1`  
- Dropped other statuses like "Current", "Late", "In Grace Period"

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

- Removed leakage and ID-like fields (e.g., `recoveries`, `desc`, `member_id`)
- Handled nulls using domain logic (median for `dti`, mode for `term`, etc.)
- Dropped low-signal or high-missing-value columns
- One-hot encoded key categorical features: `purpose`, `home_ownership`, `term`, etc.
- Scaled numeric columns (e.g., `loan_amnt`, `int_rate`, `dti`)
- Used `scale_pos_weight` in XGBoost to handle class imbalance (default ~20%)

---

## 🤖 Model Training & Comparison

Trained and benchmarked three models to maximize recall and F1-score on **default cases (class 1)**.

| Metric | Logistic Regression | Random Forest | XGBoost ✅ |
|--------|---------------------|----------------|------------|
| **Accuracy** | 80.1% | 79.7% | 79.7% |
| **Precision (Class 1)** | 0.51 | 0.46 | 0.46 |
| **Recall (Class 1)** | 0.07 ❌ | 0.09 ✅ | 0.09 ✅ |
| **F1-Score (Class 1)** | 0.12 | 0.15 ✅ | 0.15 ✅ |
| **True Positives** | 3,782 | 4,637 ✅ | 4,637 ✅ |
| **False Negatives** | 49,930 ❌ | 49,075 ✅ | 49,075 ✅ |

### ✅ Final Model: `XGBoostClassifier`

Reasons:
- Best balance between recall and precision for identifying defaulters
- Fewer false negatives (TP=4,637) → better business risk control
- Tuned with `scale_pos_weight` to handle class imbalance directly
- Scalable, fast, and robust with large datasets (~1.3M records)

---



## 🚀 Streamlit App – Real-Time Risk Scoring

Built a clean, lightweight Streamlit app to simulate loan applications and output default risk in real time.

### 🎯 Inputs:
- Loan Amount, Term, Annual Income  
- FICO Score, DTI, Interest Rate  
- Purpose, Home Ownership (via checkbox/input)

### 📈 Outputs:
- Prediction: **Default** / **Fully Paid**
- Default Probability: e.g., **76.43%**

## 🚀 Live Streamlit App

🔗 **Try the live app here:** [Loan Default Risk Predictor – Streamlit](https://loan-default-prediction-xgboost-app-lgccyltgxl9suauhmcuhqp.streamlit.app/)

📸 ![Live Model](https://github.com/Akwardhan/Loan-Default-Prediction-XGBoost-Streamlit/blob/main/Loan%20%20Fraud%20Model.png)  
📸 ![Output](https://github.com/Akwardhan/Loan-Default-Prediction-XGBoost-Streamlit/blob/main/Output%20of%20Loan%20Fraud.png)


---


---

## 🧠 Tools & Technologies

- Python: pandas, numpy, scikit-learn, XGBoost  
- Streamlit: real-time web app  
- Jupyter & Google Colab: experimentation  
- Matplotlib, Seaborn: visualization  
- Git, GitHub: version control, collaboration

---

## 💼 Business Impact

This ML solution enables:

✅ Early detection of **high-risk borrowers**  
✅ Safer loan approval workflows  
✅ Reduced **default-related revenue loss**  
✅ Interpretable dashboard for **non-technical stakeholders**

---

## 🔗 Dataset Reference

- 📂 [LendingClub Loan Data – Kaggle](https://www.kaggle.com/datasets/wordsforthewise/lending-club)

---

## 📌 Author

**Anmol Kirtiwardhan**  
🌐 Explore all my projects & live apps: [akwardhan.github.io](https://akwardhan.github.io)



