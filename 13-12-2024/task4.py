import streamlit as st
st.title("EVEN ODD CHECKER")
num=st.number_input("enter a number ")
if st.button("check"):
    if(num %2==0):
        st.title(f"{num} is a even number ..")
    else:
        st.title(f"{num} is a odd number ..")
