import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
import joblib
import os
import pydeck as pdk
from reportlab.pdfgen import canvas

# ================= PAGE CONFIG =================
st.set_page_config(page_title="SegmentIQ Analytics", layout="wide")

# ================= LOGIN =================
if "login" not in st.session_state:
    st.session_state.login = False

def login():
    st.title("🔐 SegmentIQ Login")
    user = st.text_input("Username")
    pwd = st.text_input("Password", type="password")

    if st.button("Login"):
        if user == "admin" and pwd == "1234":
            st.session_state.login = True
            st.rerun()
        else:
            st.error("Invalid credentials")

if not st.session_state.login:
    login()
    st.stop()

# ================= THEME TOGGLE =================
dark_mode = st.toggle("🌙 Dark Mode")
bg_color = "rgba(0,40,80,0.75)" if dark_mode else "rgba(0,70,120,0.55)"

# ================= UI STYLE =================
st.markdown(f"""
<style>
.stApp {{
    background-image: url("https://images.unsplash.com/photo-1486406146926-c627a92ad1ab");
    background-size: cover;
    background-attachment: fixed;
}}

.block-container {{
    background: {bg_color};
    padding: 30px;
    border-radius: 15px;
    animation: fadeIn 1s ease-in-out;
}}

@keyframes fadeIn {{
    from {{opacity:0; transform:translateY(20px)}}
    to {{opacity:1; transform:translateY(0)}}
}}

[data-testid="metric-container"]:hover {{
    transform: translateY(-5px);
    transition: 0.3s;
}}

h1,h2,h3,h4,p,label {{
    color: white !important;
}}
</style>
""", unsafe_allow_html=True)

# ================= LOAD DATA =================
DATA_PATH = "data/cleaned_customer_churn.csv"
MODEL_PATH = "data/churn_model.pkl"

df = pd.read_csv(DATA_PATH)
model = joblib.load(MODEL_PATH) if os.path.exists(MODEL_PATH) else None

st.title("📊 SegmentIQ Customer Intelligence")

# ================= NAVIGATION =================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Customer Intelligence",
    "Predict Churn",
    "Geo Analytics",
    "Reports"
])

# ==================================================
# OVERVIEW TAB
# ==================================================
with tab1:

    total = len(df)
    retention = round((1 - df["Churn Value"].mean()) * 100, 2)
    revenue = round(df["Total Revenue"].mean(), 0)
    risk = df["Churn Value"].sum()

    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Customers", f"{total:,}")
    c2.metric("Retention Rate", f"{retention}%")
    c3.metric("Avg LTV", f"${revenue:,}")
    c4.metric("Risk Customers", risk)

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        fig = px.pie(
            df,
            names="Churn Value",
            hole=0.5,
            color_discrete_sequence=px.colors.sequential.Blues
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        trend = df.groupby("Tenure in Months")["Churn Value"].mean().reset_index()
        fig = px.line(trend, x="Tenure in Months", y="Churn Value")
        st.plotly_chart(fig, use_container_width=True)

# ==================================================
# CUSTOMER INTELLIGENCE TAB
# ==================================================
with tab2:

    st.subheader("Customer Segmentation Insights")

    champions = df[df["Total Revenue"] > df["Total Revenue"].quantile(0.75)]
    emerging = df[df["Tenure in Months"] < 6]
    vulnerable = df[df["Churn Value"] == 1]
    inactive = df[df["Tenure in Months"] > 24]

    s1, s2, s3, s4 = st.columns(4)
    s1.metric("🏆 Champions", len(champions))
    s2.metric("🚀 Emerging", len(emerging))
    s3.metric("⚠ Vulnerable", len(vulnerable))
    s4.metric("💤 Inactive", len(inactive))

    fig = px.histogram(df, x="Contract", color="Churn Value", barmode="group")
    st.plotly_chart(fig, use_container_width=True)

# ==================================================
# PREDICTION TAB
# ==================================================
with tab3:

    st.subheader("AI Churn Prediction")

    monthly = st.number_input("Monthly Charges", 0, 200, 70)
    tenure = st.number_input("Tenure Months", 0, 72, 12)

    if st.button("Predict Risk"):
        score = (monthly/200) + (1-tenure/72)

        if score > 1:
            st.error("High Churn Risk")
        else:
            st.success("Customer Stable")

# ==================================================
# GEO ANALYTICS TAB (SATELLITE MAP)
# ==================================================
# SET TOKEN ONCE
import os
import pydeck as pdk

os.environ["MAPBOX_API_KEY"] = "pk.eyJ1IjoiYWJoaTIxMDIiLCJhIjoiY21sZHV0Zng0MGRhbjNmc2R6OXc3dHU1ZCJ9.EBveILHhUG4tYH8S9-mnKw"

with tab4:

    st.subheader("City-wise Customer Churn Analysis")

    if {"Latitude", "Longitude", "City", "Churn Value", "Total Revenue"}.issubset(df.columns):

        # Aggregate data
        city_df = df.groupby("City").agg({
            "Latitude": "mean",
            "Longitude": "mean",
            "Churn Value": "mean",
            "Total Revenue": "sum"
        }).reset_index()

        # Rename columns safely
        city_df.rename(columns={
            "Churn Value": "churn_value",
            "Total Revenue": "total_revenue"
        }, inplace=True)

        # Compute churn rate
        city_df["churn_rate"] = city_df["churn_value"] * 100

        # Precompute color (NO JS expressions)
        city_df["color"] = city_df["churn_value"].apply(
            lambda x: [255, 80, 80] if x > 0.5 else [0, 150, 255]
        )

        # Precompute radius
        city_df["radius"] = city_df["churn_rate"] * 200

        layer = pdk.Layer(
            "ScatterplotLayer",
            data=city_df,
            get_position=["Longitude", "Latitude"],
            get_fill_color="color",
            get_radius="radius",
            pickable=True
        )

        view_state = pdk.ViewState(
            latitude=city_df["Latitude"].mean(),
            longitude=city_df["Longitude"].mean(),
            zoom=4
        )

        deck = pdk.Deck(
            layers=[layer],
            initial_view_state=view_state,
            map_style="mapbox://styles/mapbox/light-v10",
            tooltip={
                "html": """
                <b>City:</b> {City}<br/>
                <b>Churn Rate:</b> {churn_rate}%<br/>
                <b>Total Revenue:</b> ${total_revenue}
                """
            }
        )

        st.pydeck_chart(deck)

    else:
        st.warning("Required columns missing")

# ==================================================
# REPORT TAB
# ==================================================
with tab5:

    st.subheader("Generate Business Report")

    if st.button("Export PDF Report"):

        file = "report.pdf"
        c = canvas.Canvas(file)

        c.drawString(100, 750, "Customer Churn Report")
        c.drawString(100, 700, f"Customers: {total}")
        c.drawString(100, 670, f"Retention Rate: {retention}%")
        c.drawString(100, 640, f"Avg Revenue: ${revenue}")

        c.save()

        with open(file, "rb") as f:
            st.download_button("Download PDF", f, file_name="report.pdf")
