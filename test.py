import pandas as pd
import streamlit as st

st.title("Streamlit 과제")

# 본인의 이름과 학번 정보 작성
name = ":red[본인의 이름으로 수정합니다.]"
student_id = ":red[본인의 학번으로 수정합니다.]"

st.markdown(
    f"""
- 이름: {name}
- 학번: {student_id}
"""
)

desc = """
다음의 코드를 활용해 도서관표준데이터를 분석하고, 질문에 맞게 코드를 작성해주세요.
"""
st.markdown(desc)

st.code(
    """
df = pd.read_csv("data/전국도서관표준데이터.csv", encoding="cp949")
""",
    language="python",
)

# 과제1: 도서관유형별 도서관의 개수 시각화
st.markdown("1. 도서관유형별 도서관의 개수를 `st.bar_chart`를 활용해 시각화하세요.")
# 여기에 코드를 작성하세요


# 과제2: 데이터 분석 결과 설명
st.markdown("2. 위에서 시각화한 결과를 `st.markdown`을 사용해 설명하세요.")
# 여기에 코드를 작성하세요
