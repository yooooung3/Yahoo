import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title("이차함수 y = a*(x-h)^2 + k 그래프 학습 앱")

# 파라미터 입력
a = st.slider("a값", -10.0, 10.0, 1.0, 0.1)
h = st.slider("꼭짓점 x좌표 h", -10.0, 10.0, 0.0, 0.1)
k = st.slider("꼭짓점 y좌표 k", -10.0, 10.0, 0.0, 0.1)

# x값 생성 (점 많게 해서 끊기지 않도록)
x = np.linspace(-50, 50, 2000)
y = a * (x - h)**2 + k

# 그래프 그리기
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, label=f'y = {a}*(x-{h})^2 + {k}')

# 좌표평면
ax.axhline(0, color='black', linewidth=1)  # x축
ax.axvline(0, color='black', linewidth=1)  # y축

# 눈금, 레이블
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title("이차함수 그래프")
ax.grid(True, which='both', linestyle='--', linewidth=0.5)
ax.legend()

st.pyplot(fig)

# 설명
if a > 0:
    st.write("a가 양수이므로 그래프는 위로 볼록입니다.")
elif a < 0:
    st.write("a가 음수이므로 그래프는 아래로 볼록입니다.")
else:
    st.write("a가 0이면 y=k인 직선입니다。")

st.write(f"꼭짓점 위치: ({h}, {k})")
st.write("a의 절댓값이 클수록 그래프가 좁아지고, 작을수록 넓어집니다.")
