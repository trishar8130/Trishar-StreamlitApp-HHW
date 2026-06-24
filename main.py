import streamlit as st
st.title("Welcome to AI")
student_name = st.text_input("Enter Student Name")
if student_name:
    st.write(f"Welcome, {student_name}!")
if st.button("Show Details"):
    st.write("Student Name:", student_name)
    st.write("Class: XII")
    st.write("Section: C")
