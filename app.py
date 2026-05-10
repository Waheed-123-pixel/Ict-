import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Header
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")
st.subheader("Developed by Waheed Akhtar | Roll Number: 25F-ME-80")

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
        [
            "Meters to Millimeters",
            "Millimeters to Meters",
            "Meters to Inches",
            "Inches to Meters"
        ]
    )

    if st.button("Convert Length"):

        if conversion == "Meters to Millimeters":
            result = value * 1000
            st.success(f"{value} m = {result} mm")

        elif conversion == "Millimeters to Meters":
            result = value / 1000
            st.success(f"{value} mm = {result} m")

        elif conversion == "Meters to Inches":
            result = value * 39.3701
            st.success(f"{value} m = {result} inches")

        elif conversion == "Inches to Meters":
            result = value / 39.3701
            st.success(f"{value} inches = {result} m")

# ---------------- FORCE CONVERTER ----------------

elif option == "Force Converter":

    st.header("💪 Force Converter")

    value = st.number_input("Enter Force", value=0.0)

    conversion = st.selectbox(
        "Conversion Type",
        [
            "Newton to Kilonewton",
            "Kilonewton to Newton"
        ]
    )

    if st.button("Convert Force"):

        if conversion == "Newton to Kilonewton":
            result = value / 1000
            st.success(f"{value} N = {result} kN")

        elif conversion == "Kilonewton to Newton":
            result = value * 1000
            st.success(f"{value} kN = {result} N")

# ---------------- PRESSURE CONVERTER ----------------

elif option == "Pressure Converter":

    st.header("🧪 Pressure Converter")

    value = st.number_input("Enter Pressure", value=0.0)

    conversion = st.selectbox(
        "Conversion Type",
        [
            "Pascal to Bar",
            "Bar to Pascal"
        ]
    )

    if st.button("Convert Pressure"):

        if conversion == "Pascal to Bar":
            result = value / 100000
            st.success(f"{value} Pa = {result} bar")

        elif conversion == "Bar to Pascal":
            result = value * 100000
            st.success(f"{value} bar = {result} Pa")

# ---------------- TEMPERATURE CONVERTER ----------------

elif option == "Temperature Converter":

    st.header("🌡️ Temperature Converter")

    value = st.number_input("Enter Temperature", value=0.0)

    conversion = st.selectbox(
        "Conversion Type",
        [
            "Celsius to Fahrenheit",
            "Fahrenheit to Celsius"
        ]
    )

    if st.button("Convert Temperature"):

        if conversion == "Celsius to Fahrenheit":
            result = (value * 9 / 5) + 32
            st.success(f"{value} °C = {result} °F")

        elif conversion == "Fahrenheit to Celsius":
            result = (value - 32) * 5 / 9
            st.success(f"{value} °F = {result} °C")

# ---------------- TORQUE CONVERTER ----------------

elif option == "Torque Converter":

    st.header("🔩 Torque Converter")

    value = st.number_input("Enter Torque", value=0.0)

    conversion = st.selectbox(
        "Conversion Type",
        [
            "Nm to lb-ft",
            "lb-ft to Nm"
        ]
    )

    if st.button("Convert Torque"):

        if conversion == "Nm to lb-ft":
            result = value * 0.73756
            st.success(f"{value} Nm = {result} lb-ft")

        elif conversion == "lb-ft to Nm":
            result = value / 0.73756
            st.success(f"{value} lb-ft = {result} Nm")

# ---------------- SPEED CONVERTER ----------------

elif option == "Speed Converter":

    st.header("🚗 Speed Converter")

    value = st.number_input("Enter Speed", value=0.0)

    conversion = st.selectbox(
        "Conversion Type",
        [
            "m/s to km/h",
            "km/h to m/s"
        ]
    )

    if st.button("Convert Speed"):

        if conversion == "m/s to km/h":
            result = value * 3.6
            st.success(f"{value} m/s = {result} km/h")

        elif conversion == "km/h to m/s":
            result = value / 3.6
            st.success(f"{value} km/h = {result} m/s")

# ---------------- MATERIAL DENSITY CHECKER ----------------

elif option == "Material Density Checker":

    st.header("🧱 Material Density Checker")

    materials = {
        "Steel": 7850,
        "Aluminum": 2700,
        "Copper": 8960,
        "Brass": 8500,
        "Titanium": 4500
    }

    material = st.selectbox(
        "Select Material",
        list(materials.keys())
    )

    st.info(f"Density of {material} = {materials[material]} kg/m³")

# Footer
st.markdown("---")
st.caption("Mechanical Engineering Mini Project using Streamlit")
