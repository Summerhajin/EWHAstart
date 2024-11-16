import streamlit as st

a = st.number_input("첫 번째 숫자를 입력하세요.")
b = st.number_input("두 번째 숫자를 입력하세요.")

if st.button("계산"):
    result = a + b
    st.write("결과:", result)
