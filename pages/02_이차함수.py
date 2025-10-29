import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("이차함수 y = a*(x-h)^2 + k 그래프 (인터랙티브)")

# 파라미터 입력
a = st.slider("a값을 선택하세요", -10.0, 10.0, 1.0, 0.1)
h = st.slider("꼭짓점 x좌표 h", -10.0, 10.0, 0.0, 0.1)
k = st.slider("꼭짓점 y좌표 k", -10.0, 10.0, 0.0, 0.1)

# x, y값 생성
x = np.linspace(-100, 100, 1000)  # 넓은 범위
y = a * (x - h)**2 + k

# Plotly 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'y={a}*(x-{h})^2 + {k}'))
fig.update_layout(
    title="y = a*(x-h)^2 + k",
    xaxis_title="x",
    yaxis_title="y",
    showlegend=True
)

st.plotly_chart(fig, use_container_width=True)
