# SupplyChainDashboard.py
import streamlit as st
import altair as alt
import pandas as pd

# ===============================
# Load precomputed metrics CSVs
# ===============================
late_region_pdf = pd.read_csv("D:/SupplyChain/late_per_region.csv")
late_category_pdf = pd.read_csv("D:/SupplyChain/late_per_category.csv")
late_shipping_pdf = pd.read_csv("D:/SupplyChain/late_per_shipping.csv")

# ===============================
# Compute overall KPIs
# ===============================
total_orders = late_region_pdf['Total_Orders'].sum()
total_late = late_region_pdf['Total_Late'].sum()
late_percent = (total_late / total_orders) * 100
on_time = total_orders - total_late
on_time_percent = (on_time / total_orders) * 100

# ===============================
# Streamlit App Config
# ===============================
st.set_page_config(page_title="Supply Chain Late Delivery Dashboard", layout="wide")
st.markdown("<h1 style='color:#0D47A1'>Supply Chain Late Delivery Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border:2px solid #87CEEB'>", unsafe_allow_html=True)

# -------------------------------
# KPIs
# -------------------------------
st.header("Overall Delivery Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Orders", total_orders)
col2.metric("Total Late Deliveries", total_late)
col3.metric("Late %", f"{late_percent:.2f}%")
col4.metric("On-Time %", f"{on_time_percent:.2f}%")

# -------------------------------
# Charts
# -------------------------------
def plot_bar(df, x_col, y_col, color="#87CEEB", title="Chart"):
    chart = alt.Chart(df).mark_bar(color=color).encode(
        x=alt.X(x_col, sort='-y'),
        y=y_col,
        tooltip=df.columns.tolist()
    ).properties(title=title)
    return chart

st.header("Late Deliveries by Region")
st.altair_chart(plot_bar(late_region_pdf, 'Order Region', 'Late_Percent'), use_container_width=True)

st.header("Late Deliveries by Category")
st.altair_chart(plot_bar(late_category_pdf, 'Category Name', 'Late_Percent', color="#0D47A1"), use_container_width=True)

st.header("Late Deliveries by Shipping Mode")
st.altair_chart(plot_bar(late_shipping_pdf, 'Shipping Mode', 'Late_Percent', color="#1E90FF"), use_container_width=True)

# -------------------------------
# Feature Importance Table
# -------------------------------
st.header("Feature Importance")
try:
    import pickle
    sorted_features = pickle.load(open("D:/SupplyChain/feature_importance.pkl", "rb"))
    feature_df = pd.DataFrame(sorted_features, columns=["Feature", "Importance"])
    st.dataframe(feature_df.style.background_gradient(cmap="Blues"))
except:
    st.info("Feature importance not available. Compute `sorted_features` in PySpark and save as CSV/pickle.")

# -------------------------------
# Sample Orders for Demo
# -------------------------------
st.header("Sample Orders with Late Delivery Prediction")
sample_orders_demo = pd.DataFrame({
    "Order ID": [101, 102, 103, 104],
    "Customer Fname": ["Alice", "Bob", "Charlie", "David"],
    "Customer Lname": ["Smith", "Johnson", "Lee", "Brown"],
    "Category Name": ["Electronics", "Clothing", "Furniture", "Electronics"],
    "Order Region": ["North", "South", "East", "West"],
    "Shipping Mode": ["Air", "Ground", "Air", "Ground"],
    "Days for shipment (scheduled)": [3, 5, 4, 2],
    "Days for shipping (real)": [4, 4, 5, 2]
})

# Rule-based prediction: Late if real days > scheduled
sample_orders_demo['Predicted_Late'] = (
    sample_orders_demo['Days for shipping (real)'] - 
    sample_orders_demo['Days for shipment (scheduled)'] > 0
).astype(int)

st.subheader("Sample Demo Predictions")
st.dataframe(sample_orders_demo)

# -------------------------------
# Upload CSV for Prediction
# -------------------------------
st.header("Upload Your Orders to Predict Late Delivery")
st.markdown(
    "Upload a CSV with the following columns:\n"
    "- Order ID\n"
    "- Customer Fname\n"
    "- Customer Lname\n"
    "- Category Name\n"
    "- Order Region\n"
    "- Shipping Mode\n"
    "- Days for shipment (scheduled)\n"
    "- Days for shipping (real)\n"
)

uploaded_file = st.file_uploader("Upload CSV of orders", type=["csv"])
if uploaded_file:
    try:
        user_df = pd.read_csv(uploaded_file, encoding='latin1')  # Handles encoding issues
        user_df['Predicted_Late'] = (
            user_df['Days for shipping (real)'] - 
            user_df['Days for shipment (scheduled)'] > 0
        ).astype(int)
        user_df['Predicted_Status'] = user_df['Predicted_Late'].apply(lambda x: "Late" if x else "On-Time")
        st.subheader("Uploaded Orders Predictions")
        st.dataframe(user_df)
        
        # KPIs for uploaded data
        total_user = user_df.shape[0]
        total_late_user = user_df['Predicted_Late'].sum()
        total_on_time_user = total_user - total_late_user
        late_percent_user = (total_late_user / total_user) * 100
        on_time_percent_user = (total_on_time_user / total_user) * 100
        st.markdown(f"**Uploaded Data Metrics:** Total Orders: {total_user}, Late: {total_late_user}, Late %: {late_percent_user:.2f}%, On-Time %: {on_time_percent_user:.2f}%")
        
    except Exception as e:
        st.error(f"Error reading uploaded file: {e}")

# -------------------------------
# Manual Input Section
# -------------------------------
st.header("Manual Input to Predict Late Delivery")
with st.form("manual_input_form"):
    order_id = st.text_input("Order ID", "105")
    fname = st.text_input("Customer Fname", "John")
    lname = st.text_input("Customer Lname", "Doe")
    category = st.selectbox("Category Name", ["Electronics", "Clothing", "Furniture"])
    region = st.selectbox("Order Region", ["North", "South", "East", "West"])
    shipping_mode = st.selectbox("Shipping Mode", ["Air", "Ground", "Sea"])
    scheduled_days = st.number_input("Days for shipment (scheduled)", min_value=1, value=3)
    actual_days = st.number_input("Days for shipping (real)", min_value=1, value=3)
    
    submitted = st.form_submit_button("Predict Late Delivery")
    
    if submitted:
        predicted_late = int(actual_days > scheduled_days)
        status = "Late Delivery" if predicted_late else "On-Time Delivery"
        st.markdown(f"**Prediction:** {status}")
