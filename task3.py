import streamlit as st
proj=st.number_input("enter your project score:")
internal=st.number_input("enter your internal score:")
external=st.number_input("enter your external score:")
if st.button("Obtain student certificate"):
    total = 0
    if (proj > 50 and internal > 50 and external > 50):
        total = ((proj * 70) / 100) + ((internal * 10) / 100) + ((external * 20) / 100)
        st.title(f"Total score is :{ total}")
    else:
        if (proj <= 50):
            st.title(f"failed in project,score is: {proj}")
        if (internal <= 50):
            st.title(f"failed in internal,score is: {internal}")
        if (external <= 50):
            st.title(f"failed in external,score is:{external}")

    if (total > 90):
        st.title("A grade")
    elif (total > 80):
       st.title("B grade")
    elif (total > 50):
        st.title("c grade")
