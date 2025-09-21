This project is my first hands-on exploration of PySpark for supply chain analytics. It predicts late deliveries using a machine learning pipeline in PySpark and visualizes insights through a Streamlit dashboard. The project demonstrates KPIs, feature importance, and interactive predictions using both sample and user-uploaded order data. Accuracy was improved from ~0.7 to ~0.9 by tuning Random Forest hyperparameters. Unlike traditional Python Pandas workflows, PySpark provides scalability and distributed processing capabilities, making it suitable for larger, real-world datasets. This repository serves as a learning project showcasing PySpark’s potential in supply chain logistics and delivery optimization.

# Supply Chain Late Delivery Prediction 🚚

This repository contains my first project using **PySpark** for machine learning in supply chain analytics.  
The project predicts whether an order will be delivered late, visualizes KPIs, and allows interactive testing using a Streamlit dashboard.  

---

## 📌 Project Overview
- **Goal:** Predict late deliveries in supply chain logistics.  
- **Tech stack:** PySpark, Pandas, Streamlit, Altair, Pickle.  
- **Accuracy Improvement:** Tuned Random Forest model from ~0.7 → ~0.9 ROC-AUC.  
- **Why PySpark?** Unlike Pandas, PySpark allows distributed data processing, scalable ML pipelines, and handles large datasets efficiently.  

---

## ✨ Features
- KPIs: Total Orders, Late %, On-Time %  
- Charts: Late Deliveries by Region, Category, and Shipping Mode  
- Feature Importance: Key drivers of late delivery  
- Predictions:
  - Preloaded **sample orders**  
  - **Upload your own CSV** to test predictions  
  - **Manual input form** for real-time prediction  

---

## 📊 Example Dashboard

<img width="1845" height="903" alt="Screenshot 2025-09-21 145801" src="https://github.com/user-attachments/assets/b05819d6-d3bb-4a9b-beaa-fb386ede773e" />


---

## 📂 Repository Structure


├── SupplyChainDashboard.py # Streamlit dashboard
├── late_per_region.csv # Precomputed metrics (region)
├── late_per_category.csv # Precomputed metrics (category)
├── late_per_shipping.csv # Precomputed metrics (shipping mode)
├── feature_importance.pkl # Model feature importance (pickle file)
├── sample_orders.csv # Demo orders for prediction
└── README.md # Documentation


---

## ⚡ Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/supply-chain-pyspark.git
   cd supply-chain-pyspark





Run the Streamlit dashboard:

streamlit run SupplyChainDashboard.py

📤 Input Template

If you want to upload your own CSV for predictions, use this format:

Order ID	Customer Fname	Customer Lname	Category Name	Order Region	Shipping Mode	Days for shipment (scheduled)	Days for shipping (real)
101	Alice	Smith	Electronics	North	Air	3	4
🔍 Learning Outcomes

Learned the basics of PySpark ML pipelines

Compared PySpark vs Pandas for data handling

Built an interactive Streamlit dashboard

Improved model accuracy from 0.7 to 0.9

🚀 Future Enhancements

Integrate larger real-world datasets

Try Gradient Boosting models in PySpark

Deploy dashboard on cloud (Streamlit Cloud / AWS)

📬 Contact

Feel free to connect with me on LinkedIn linkedin.com/in/vinutha-naik
 or raise issues in this repo for discussions.


---

Would you like me to also create a **`requirements.txt` file** for easy setup (so others can directly install all dependencies)?

