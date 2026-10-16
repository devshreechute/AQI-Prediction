
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AQI Prediction Dashboard",
    page_icon="🌿",
    layout="wide"
)

st.title("🌿 AQI Prediction Dashboard")
st.write(
    "Machine Learning Based Air Quality Index Prediction System"
)

st.info(
    "Enter pollutant measurements below. "
    "The trained ML model will be connected later."
)

st.subheader("Enter Pollutant Measurements")

col1, col2 = st.columns(2)

with col1:
    pm25 = st.number_input("PM2.5 (µg/m³)", min_value=0.0, value=25.0)
    pm10 = st.number_input("PM10 (µg/m³)", min_value=0.0, value=50.0)
    no2 = st.number_input("NO2 (µg/m³)", min_value=0.0, value=20.0)
    co = st.number_input("CO (mg/m³)", min_value=0.0, value=1.0)

with col2:
    no = st.number_input("NO (µg/m³)", min_value=0.0, value=10.0)
    so2 = st.number_input("SO2 (µg/m³)", min_value=0.0, value=10.0)
    o3 = st.number_input("O3 (µg/m³)", min_value=0.0, value=30.0)

input_data = pd.DataFrame({
    "PM2.5": [pm25],
    "PM10": [pm10],
    "NO2": [no2],
    "CO": [co],
    "NO": [no],
    "SO2": [so2],
    "O3": [o3]
})

if st.button("Predict AQI", type="primary"):
    st.subheader("Prediction Result")
    st.warning(
        "Demo placeholder: the actual trained model "
        "has not been connected yet."
    )
    st.write("Entered pollutant values:")
    st.dataframe(input_data, use_container_width=True)

st.subheader("Pollutant Input Overview")
st.bar_chart(input_data.T)

st.caption(
    "The chart displays input values, not a predicted AQI."
)
