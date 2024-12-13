import streamlit as st
basic_sal=st.number_input("enter salary:")
if st.button("calc Gross Salary"):
    HRA=0
    DA=0
    if(basic_sal < 10000):
        HRA = (basic_sal * 67) / 100
        DA = (basic_sal * 73) / 100
    elif (basic_sal <= 10000):
        HRA = (basic_sal * 69) / 100
        DA = (basic_sal * 76) / 100
    elif (basic_sal > 20000):
        HRA = (basic_sal * 73) / 100
        DA = (basic_sal * 89) / 100

    GS = HRA + DA + basic_sal
    st.title(f"GROSS SALARY IS:{GS}")

