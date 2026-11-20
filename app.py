import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Hello Streamlit",
    page_icon="👋"
)

# Application
st.title("Hello World! 👋")

st.write("Welcome to my first Streamlit application.")

name = st.text_input("What is your name?")

if name:
    st.success(f"Hello, {name}!")

st.divider()

st.caption("Built with Python and Streamlit")
