import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("이차함수 y = a*x² 그래프 학습 앱")

st.write("a 값을 조절하며 그래프의 모양이 어떻게 변하는지 관찰해보세요.")

# 사용자로부터 a값 입력 받기
a = st.slider("a 값 선택", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# x 값 생성
x = np.linspace(-10, 10, 400)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f"y = {a}x²")
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"y = {a}x²")
ax.legend()
ax.grid(True)

st.pyplot(fig)

# 관찰 포인트 안내
st.write("""
- a > 0 : 그래프가 위로 볼록
- a < 0 : 그래프가 아래로 볼록
- |a|가 커질수록 그래프가 좁아지고, |a|가 작을수록 그래프가 넓어짐
""")
