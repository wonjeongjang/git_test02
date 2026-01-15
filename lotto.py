import streamlit as st
st.title("로또 번호 생성기")
st.header("행운의 로또 번호를 생성해보세요!")
import random

# 로또 번호 생성 함수
def generate_lotto_numbers():
    numbers = list(range(1, 46))
    random.shuffle(numbers)
    return sorted(numbers[:6])

# 버튼 클릭 시 로또 번호 생성
if st.button("로또 번호 생성"):
    lotto_numbers = generate_lotto_numbers()
    st.write(f"행운의 로또 번호: {', '.join(map(str, lotto_numbers))}")

st.write(f"생성된 시각 : {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')")