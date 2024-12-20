import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set the title of the website
st.title("My Streamlit Website")

# Add a sidebar menu
st.sidebar.title("Menu")
options = st.sidebar.radio("Go to", ["Home", "About", "Data", "Contact"])

# 1. Home Page
if options == "Home":
    st.header("Welcome to My Website!")
    st.write("This is a simple website built with Streamlit.")
    st.image("images/home_image.jpg", caption="Streamlit makes web development easy.", use_container_width=True)

# 2. About Page
elif options == "About":
    st.header("About Me")
    st.write("""
    Hi! I'm [Your Name]. I am passionate about Python, web development, and data science.
    This website demonstrates how to use Streamlit for building web apps quickly.
    """)
    st.image("images/about_image.jpg", caption="Streamlit: Python-Powered Web Apps")

# 3. Data Page
elif options == "Data":
    st.header("Data Visualization")
    st.write("Here, we visualize some sample data.")

    # Load sample data
    data = pd.DataFrame({
        "Category": ["A", "B", "C", "D"],
        "Values": [23, 45, 56, 78]
    })

    # Show data as a table
    st.table(data)

    # Plot data as a bar chart
    fig, ax = plt.subplots()
    ax.bar(data["Category"], data["Values"], color="skyblue")
    st.pyplot(fig)

# 4. Contact Page
elif options == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out!")
    st.write("Email: example@example.com")
    st.write("GitHub: [My GitHub](https://github.com/)")

    # Add a contact form
    name = st.text_input("Your Name")
    message = st.text_area("Your Message")
    if st.button("Send"):
        st.success("Thank you! Your message has been sent.")