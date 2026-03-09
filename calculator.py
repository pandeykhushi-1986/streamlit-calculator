import streamlit as st
st.title("Calculator App🧮")
num_1 = st.number_input("Enter your first number")
num_2 = st.number_input("Enter your second number")
operation = st.selectbox("Choose operation", ["+", "-", "*", "/"])
if st.button("Calculate"):
    if operation == "+":
        result = num_1 + num_2
    elif operation == "-":
        result = num_1 - num_2
    elif operation == "*":
        result = num_1 * num_2
    elif operation == "/":
        result = num_1 / num_2
    
    st.success(f"Answer = {result}")
    