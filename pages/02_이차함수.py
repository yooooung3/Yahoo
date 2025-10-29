import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("이차함수 y = a*x^2 그래프 학습 앱")

# a값 선택
a = st.slider("a값을 선택하세요", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# x값 생성
x = np.linspace(-10, 10, 400)
y = a * x**2

# 그래프 그리기
fig, ax = plt.subplots()
ax.plot(x, y, label=f'y = {a}x^2')
ax.axhline(0, color='black', linewidth=0.5)
ax.axvline(0, color='black', linewidth=0.5)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("y = a*x^2")
ax.grid(True)
ax.legend()

st.pyplot(fig)

# a값에 대한 설명
if a > 0:
    st.write("a가 양수이므로 그래프는 위로 볼록입니다.")
elif a < 0:
    st.write("a가 음수이므로 그래프는 아래로 볼록입니다.")
else:
    st.write("a가 0이면 그래프는 x축 위의 직선입니다.")

st.write("a의 절댓값이 클수록 그래프가 좁아지고, 작을수록 넓어집니다.")
