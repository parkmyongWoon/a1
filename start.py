import streamlit as st

st.title('사칙연산 계산기')

a = st.number_input('첫번째 숫자를 입력하세요:', value=0.0)
b = st.number_input('두번째 숫자를 입력하세요:', value=0.0)

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button('더하기'):
        result = a + b
        st.write(f'결과: {result}')

with col2:
    if st.button('빼기'):
        result = a - b
        st.write(f'결과: {result}')
        
with col3:
    if st.button('곱하기'):
        result = a * b
        st.write(f'결과: {result}')
        
with col4:
    if st.button('나누기'):
        if b != 0:
            result = a / b
            st.write(f'결과: {result}')
        else:
            st.error('0으로 나눌 수 없습니다!')
