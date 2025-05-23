import streamlit as st

# Set the title of the web app
st.title("BMI Calculator")

# Add a subtitle or description
st.write("Calculate your Body Mass Index (BMI) to understand your health status.")

# Input fields for height and weight
weight = st.number_input("Enter your weight (in kg):", min_value=0.0, step=0.1, format="%.2f")
height = st.number_input("Enter your height (in cm):", min_value=0.0, step=0.1, format="%.2f")

# Calculate BMI when both inputs are valid
if weight > 0 and height > 0:
    height_in_meters = height / 100  # Convert height to meters
    bmi = weight / (height_in_meters ** 2)

    # Display the BMI result
    st.write(f"Your BMI is: **{bmi:.2f}**")

    # Interpret the BMI value
    if bmi < 18.5:
        st.warning("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are in the obesity category.")
else:
    st.info("Please enter both weight and height to calculate your BMI.")