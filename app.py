import streamlit as st
from datetime import date

st.title("Age Calculator")

dob = st.date_input(
    "Enter your Date of Birth",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

if st.button("Calculate Age"):
    today = date.today()

    age = today.year - dob.year

    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1

    st.success(f"Your age is {age} years")