import streamlit as st

st.title("이차함수 y = a*x² 학습 앱 (설치 필요 없음)")

st.write("슬라이더로 a 값을 바꿔가며 그래프를 관찰하세요.")

# a값 입력
a = st.slider("a 값 선택", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# x, y값 계산
x_values = list(range(-10, 11))  # -10부터 10까지 정수
y_values = [a * (x**2) for x in x_values]

# 데이터 준비
data = {"x": x_values, "y": y_values}

# 차트 그리기
st.line_chart(data={"y": y_values}, use_container_width=True)

# 관찰 포인트 안내
st.write("""
- a > 0 : 그래프가 위로 볼록  
- a < 0 : 그래프가 아래로 볼록  
- |a|가 커질수록 그래프가 좁아지고, |a|가 작을수록 그래프가 넓어짐
""")
