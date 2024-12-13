# input emp sal and 3 shopping bills
import streamlit as st
salary =st.number_input("enter employee salary")
bill_1=st.number_input("shopping bill 1:")
bill_2=st.number_input("shopping bill 2:")
bill_3=st.number_input("shopping bill 3:")

if st.button("calculate..."):
    total = bill_1 + bill_2 + bill_3
    st.title(f"your total shopping bill is :{total}")
    sal_left = salary - total
    percentage = (total / salary) * 100
    st.title(f"you spent {percentage}% of your salary on shopping ")

    # total shopping bill and percentage of sal consumed
