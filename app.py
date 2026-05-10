import streamlit as st

# Page Configuration
st.set_page_config(page_title="Mechanical Unit Converter", page_icon="⚙️", layout="centered")

# Header
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")
st.subheader("Developed by Muhammad Bilal | Roll Number: 25-ME-124")

st.markdown("---")

# Sidebar
st.sidebar.header("Choose a Feature")
option = st.sidebar.selectbox(
    "Select Option",
    [
        "Length Converter",
        "Force Converter",
        "Pressure Converter",
        "Temperature Converter",
        "Torque Converter",
        "Speed Converter",
        "Material Density Checker"
    ]
)

# ---------------- LENGTH CONVERTER ----------------
if option == "Length Converter":
    st.header("📏 Length Converter")

    value = st.number_input("Enter Length", value=0.0)

    conversion = st.selectbox(
        "Conversion Type",
st.caption("Mechanical Engineering Mini Project using Streamlit")
