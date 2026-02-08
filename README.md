
# 📊 Customer Retention Intelligence Dashboard

> ⚠️ **Educational Purpose Notice:**  
> This project is developed purely for **educational and learning
> purposes** to demonstrate data science, machine learning deployment,
> dashboard development, and business analytics concepts.

------------------------------------------------------------------------

## 🚀 Project Overview

The **Customer Retention Intelligence Dashboard** is a complete
end‑to‑end data analytics and machine learning project designed to:

-   Analyze customer churn behavior
-   Predict potential customer churn
-   Provide geographic business insights
-   Visualize retention analytics interactively

This project integrates:

-   Data preprocessing
-   Machine learning prediction
-   Interactive business dashboard
-   Geographic visualization
-   Automated business reporting

------------------------------------------------------------------------

## 🧠 Problem Statement

Customer churn significantly impacts industries such as:

-   Telecommunications
-   Banking
-   SaaS platforms
-   Subscription-based businesses

Understanding churn helps organizations:

✔ Improve retention strategies  
✔ Reduce revenue loss  
✔ Optimize customer experience  
✔ Make data-driven decisions

------------------------------------------------------------------------

## 📂 Dataset Description

The dataset includes:

### Customer Details

-   Customer demographics
-   Location data (city, latitude, longitude)
-   Service subscription information

### Billing Information

-   Monthly charges
-   Total revenue
-   Payment methods

### Target Variable

-   **Churn Value**
    -   0 = Customer retained
    -   1 = Customer churned

Datasets were cleaned, merged, and preprocessed before modeling.

------------------------------------------------------------------------

## 🤖 Machine Learning Model

A classification model was developed to predict churn risk.

### Model Used:

-   Random Forest Classifier

Reasons:

-   Handles categorical + numerical data
-   Robust against overfitting
-   Strong performance on churn prediction

The trained model is saved using:

``` python
joblib.dump(model, "churn_model.pkl")
```

And loaded inside the dashboard for predictions.

------------------------------------------------------------------------

## 🌍 Geographic Analytics

The dashboard includes geographic visualization:

-   Customer distribution map
-   City-wise churn insights
-   Revenue concentration regions

These help businesses identify:

✔ High-risk churn regions  
✔ Expansion opportunities  
✔ Customer density clusters

------------------------------------------------------------------------

## 📈 Dashboard Features

### ✔ KPI Analytics

-   Total customers
-   Retention rate
-   Revenue insights
-   Churn trends

### ✔ Customer Segmentation

Customers categorized into:

-   Champions (high revenue)
-   Emerging customers
-   Vulnerable customers
-   Inactive customers

### ✔ AI Churn Prediction

Predict churn probability based on customer attributes.

### ✔ Interactive Maps

Geo analytics for business decision making.

### ✔ PDF Report Generation

Export business insights automatically.

------------------------------------------------------------------------

## 🎨 User Interface Highlights

-   Glassmorphism UI design
-   Dark/Light theme toggle
-   Animated dashboard transitions
-   Professional analytics layout

------------------------------------------------------------------------

## 📷 Screenshots (Add Your Own)

### Dashboard Overview

    C:\Users\abhis\OneDrive\Desktop\customer_retention_app\Screenshot 2026-02-08 205524.png

    C:\Users\abhis\OneDrive\Desktop\customer_retention_app\Screenshot 2026-02-08 205538.png

------------------------------------------------------------------------

### Churn Prediction Panel

    C:\Users\abhis\OneDrive\Desktop\customer_retention_app\Screenshot 2026-02-08 205607.png

------------------------------------------------------------------------

### Geographic Map

    C:\Users\abhis\OneDrive\Desktop\customer_retention_app\Screenshot 2026-02-08 205921.png

------------------------------------------------------------------------

## 🛠 Technologies Used

### Programming

-   Python

### Data Science

-   Pandas
-   NumPy
-   Scikit-learn

### Visualization

-   Plotly
-   PyDeck

### Dashboard

-   Streamlit

### Model Deployment

-   Joblib

### Reporting

-   ReportLab

C:\Users\abhis\OneDrive\Desktop\customer_retention_app\Screenshot 2026-02-08 205623.png
------------------------------------------------------------------------

## 💼 Business Impact

This project helps organizations:

-   Identify churn risks
-   Improve retention strategies
-   Optimize marketing decisions
-   Increase revenue stability

------------------------------------------------------------------------

## 🔮 Future Enhancements

Potential improvements:

-   Real-time churn prediction
-   Advanced deep learning models
-   Automated business recommendations
-   Cloud deployment
-   Enhanced geographic analytics

------------------------------------------------------------------------

## 👨‍💻 Author

**Abhishek L D**  
Aspiring Data Scientist \| Analytics Enthusiast

------------------------------------------------------------------------

## ⭐ Support

If you found this project helpful:

⭐ Star the repository  
⭐ Share feedback  
⭐ Suggest improvements
