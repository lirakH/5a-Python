"""
Introduction to Streamlit

Streamlit is an open-source Python library that is
designed to make it easy to create web applications for
data science and machine learning. It's particularly
useful for turning data scripts into shareable web apps
quickly.


This library provides widgets like sliders, buttons,
and text inputs that you can use to interact with your
data.

pip install streamlit

streamlit run 16.py

"""
import shuma as sh
import streamlit as st

def main():
    st.title("Hello 5a!!") #title = h1

    emri = sh.shuma(5,6)


    if st.button("Click me"): #button = button
        st.write("Button Clicked") #write = p

    st.title(f"{emri}")
    st.checkbox("Check me") # checkbox = checkbox

    user_input = st.text_input("Enter Your Name", "Sample text")

    st.write("You entered:", user_input)

    age = st.number_input("Enter your age", min_value=10, max_value=100)

    st.write(f"Your age is: {age}")

    message = st.text_area("Enter a message")

    st.write(f"Your message is: {message}")

    choice = st.radio("Pick one", ["Choice 1", "Choice 2", "Choice 3"])

    st.write(f"You chose: {choice}")

    if st.button("Success"):
        st.success("Operation was successful!")

    try:
        1/0
    except Exeption as e:
        st.exception(e)


if __name__ == "__main__":
    main()











