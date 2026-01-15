import streamlit as st
import numpy as np
import pandas as pd


st.title("이것이 타이틀이다")
st.header("이것이 헤더이다")
st.subheader("이것이 서브헤더이다")
st.text("이것이 일반 텍스트이다")
st.title('스마일 : 😊')

sample_code = "print('hello')" # 먼저 정의
st.code(sample_code, language='python')
#마크다운 문법 지원
st.markdown("텍스트의 색상을 :green[초록색]으로 , 그리고 **:blue[파란색]** 볼드체를 설정 할 수 있다")
st.markdown(":green[$\sqrt{x^2 + y^2} = 1$] 와 같은 수식도 지원한다.")

dataframe = pd.DataFrame({
    "first column": [1, 2, 3, 4],
    "second column": [10, 20, 30, 40]
})

# 2. 데이터프레임 출력 (오타 수정: dataframe)
st.write("데이터프레임 (인터랙티브)")
st.dataframe(dataframe) 

# 3. 테이블 출력 (오타 수정: dataframe)
st.write("테이블 (정적)")
st.table(dataframe)

st.metric(label="온도", value="25 °C", delta="1.2 °C")
st.metric(label="삼성전자", value="140,000 원", delta="-1,000 원")

st.title("위젯들")

#컬럼으로 영역 나누어 표기
col1, col2, col3 = st.columns(3)

# 단위(km/h 등)를 value에 넣고 delta에는 숫자만 넣어보세요.
col1.metric(label="속도", value="120 km/h", delta="10")
col2.metric(label="고도", value="1,200 m", delta="-50")
col3.metric(label="온도", value="22 °C", delta="2")

#버튼을 눌러주세요
st.button("버튼")

button = st.button("버튼을 눌러주세요")
if button:
    st.write(":blue[버튼]이 눌렸습니다! 👌")

agree =st.checkbox("체크박스를 눌러주세요")
if agree:
    st.write("체크박스가 선택되었습니다! ✅")

st.radio("라디오 버튼을 선택해주세요", ("옵션 1", "옵션 2", "옵션 3"))
st.selectbox("셀렉트 박스에서 선택해주세요", ("옵션 A", "옵션 B", "옵션 C"))
st.multiselect("셀렉트 박스에서 선택해주세요", ("선택1", "선택2", "선택3"))

# 1. selectbox를 만들고 사용자의 선택을 'mbti' 변수에 저장합니다.
mbti = st.selectbox(
    "당신의 MBTI는 무엇인가요?",
    ('INTJ', 'INTP', 'ENTJ', 'ENTP'),
    index=2
)

# 2. 선택된 값(mbti)에 따라 문구를 출력합니다.
if mbti == 'INTJ':
    st.write("당신은 전략가형입니다.")
elif mbti == 'INTP':
    st.write("당신은 논리주의자형입니다.")
elif mbti == 'ENTJ':
    st.write("당신은 지도자형입니다.")
elif mbti == 'ENTP':
    st.write("당신은 발명가형입니다.")

#슬라이더
age = st.slider("당신의 나이는 어떻게 되나요?", 0, 120, 25)
st.write(f"당신의 나이는 :blue [{age}]세 입니다.")

value = st.slider("범위의 값을 다음과 같은 범위로 설정하세요", 0.0, 100.0, 25.0, 0.5)



from datetime import datetime as dt  # <--- 이 줄이 반드시 있어야 합니다!

# ... 그 아래에 기존 코드 작성 ...
value = 25.0
st.write(f"선택된 값은 :green[{value}] 입니다.")

start_time = st.slider(
    "언제 약속을 잡는 것이 좋을까요?",
    min_value=dt(2026, 1, 1, 0, 0),
    max_value=dt(2026, 1, 31, 23, 59),
    value=dt(2026, 1, 15, 12, 0),
    format="YYYY-MM-DD HH:mm"
)

# 1. 컬러 텍스트 출력 수정
# :green[...] 형식을 지켜야 합니다.
st.write(f"선택된 시간: :green[{start_time}] 입니다.")

# 2. 텍스트 입력 (괄호 닫기 확인!)
title = st.text_input(
    label="가고 싶은 여행지가 있나요?",
    placeholder="예: 제주도, 파리, 뉴욕, 도쿄"
) # 여기서 괄호를 꼭 닫아줘야 합니다!

# 3. 결과 출력
st.write(f"당신이 가고 싶은 여행지는 :green[{title}] 입니다.")

#파일 다운로드
st.download_button(
    label="CSV 다운로드",
    data="이것은 샘플 파일의 내용입니다.",
    file_name="sample.txt",
    mime="text/plain"
)