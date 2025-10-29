import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("이차함수 y = a*x² 그래프 학습 앱 (Plotly 버전)")

st.write("슬라이더로 a 값을 조절하며 그래프 모양 변화를 확인하세요.")

# a값 입력
a = st.slider("a 값 선택", min_value=-10.0, max_value=10.0, value=1.0, step=0.1)

# x, y값 계산
x = np.linspace(-10, 10, 400)
y = a * x**2

# 그래프 생성
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f"y = {a}x²"))
fig.update_layout(
    title=f"y = {a}x²",
    xaxis_title="x",
    yaxis_title="y",
    showlegend=True
)
fig.update_xaxes(showgrid=True, zeroline=True)
fig.update_yaxes(showgrid=True, zeroline=True)

st.plotly_chart(fig, use_container_width=True)

# 관찰 포인트 안내
st.write("""
- a > 0 : 그래프가 위로 볼록  
- a < 0 : 그래프가 아래로 볼록  
- |a|가 커질수록 그래프가 좁아지고, |a|가 작을수록 그래프가 넓어짐
""")
