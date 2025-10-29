import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.title("이차함수 y = a*(x-h)^2 + k 그래프 (인터랙티브)")

# 파라미터 입력
a = st.slider("a값", -10.0, 10.0, 1.0, 0.1)
h = st.slider("꼭짓점 x좌표 h", -20.0, 20.0, 0.0, 0.1)
k = st.slider("꼭짓점 y좌표 k", -20.0, 20.0, 0.0, 0.1)

# x값 생성
x = np.linspace(-100, 100, 5000)  # 점을 충분히 많이 찍어 부드럽게
y = a * (x - h)**2 + k

# Plotly 그래프
fig = go.Figure()
fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name=f'y={a}*(x-{h})^2 + {k}'))

# 좌표축 표시
fig.update_layout(
    xaxis=dict(title='x', zeroline=True, zerolinewidth=2, zerolinecolor='black'),
    yaxis=dict(title='y', zeroline=True, zerolinewidth=2, zerolinecolor='black'),
    title="이차함수 그래프",
    showlegend=True,
)

st.plotly_chart(fig, use_container_width=True)
