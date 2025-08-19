# Sentiment Analysis App  

A simple **Streamlit web application** for predicting whether a given review is **Positive** or **Negative**.  
This project experiments with multiple **Machine Learning models** including **Logistic Regression, Random Forest, and XGBoost**, with **TF-IDF vectorization** for text preprocessing.  

---

##  Features
-  User-friendly **web interface** built with Streamlit  
-  **TF-IDF Vectorization** for text preprocessing  
-  Models tested: **Logistic Regression, Random Forest, XGBoost**  
-  Final deployed model: **Logistic Regression (best trade-off for accuracy & speed)**  
-  Model + Vectorizer saved with **Joblib** for deployment  

---

## Model Training

1) Vectorizer: TF-IDF

2) Models compared:

    Logistic Regression → Best performance for deployment

    Random Forest → Strong but heavier model

    XGBoost → Good performance, but slower for real-time app

    Final Deployment: Logistic Regression + TF-IDF

    Saved with Joblib for reusability

## Key Insights

Logistic Regression was the most efficient & accurate for text sentiment prediction

Random Forest and XGBoost provided strong benchmarks but were heavier for deployment

TF-IDF captured important textual patterns effectively

Streamlit made deployment easy & interactive
