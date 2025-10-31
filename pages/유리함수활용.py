# app.py
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="유리함수 창의융합 앱", layout="wide")

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"

# 데이터/텍스트 정의
content = {
    "과학": {
        "emoji": "🧪",
        "title": "과학 - 빛의 굴절률",
        "desc": "빛의 굴절률과 유리함수 관계",
        "explanation": """**개념:** 굴절률 n = 진공에서 빛 속도 / 매질 속 빛 속도.  
스넬의 법칙: n1*sinθ1 = n2*sinθ2  
**유리함수 활용:** 입사각 변화에 따른 굴절각 변화가 유리함수 형태로 근사 가능."""
    },
    "코딩": {
        "emoji": "💻",
        "title": "코딩 - UI 최적화",
        "desc": "UI 반응 속도 곡선 최적화",
        "explanation": """**개념:** UI/UX에서 입력 변화에 따른 화면 반응 속도 중요.  
**유리함수 활용:** y = a/(x+b)+c 형태로 부드러운 반응곡선 구현 가능."""
    },
    "예술": {
        "emoji": "🎨",
        "title": "예술 - 건축 디자인 곡선",
        "desc": "유리함수 기반 건축 곡선 디자인",
        "explanation": """**개념:** 건축 곡선 구조로 미적 가치와 공간감 향상.  
**유리함수 활용:** 점근선을 기준으로 곡선 형성 → 시각적 안정감 제공."""
    },
    "사회": {
        "emoji": "📈",
        "title": "사회 - 한계효용체감",
        "desc": "한계효용 그래프와 유리함수",
        "explanation": """**개념:** 소비 증가 → 만족 증가폭 감소  
**유리함수 활용:** y = a/(x+b)+c 형태로 초기 효용 크고, 이후 증가폭 감소 설명 가능."""
    }
}

# 메인 페이지
def main_page():
    st.title("유리함수 창의융합 앱")
    st.write("아래 카드 중 하나를 선택하세요:")

    cols = st.columns(2)
    items = list(content.keys())
    for i, key in enumerate(items):
        with cols[i % 2]:
            if st.button(f"{content[key]['emoji']} {content[key]['title']}"):
                st.session_state.page = key

# 분야 페이지
def detail_page(key):
    st.header(f"{content[key]['emoji']} {content[key]['title']}")
    st.write(content[key]['explanation'])
    st.write("---")
    
    st.subheader("유리함수 그래프 시뮬레이션")
    
    # 슬라이더
    a = st.slider("a 값", 0.1, 10.0, 1.0)
    b = st.slider("b 값", 0.1, 10.0, 1.0)
    c = st.slider("c 값", -5.0, 5.0, 0.0)
    
    # x값 생성
    x = np.linspace(0.1, 10, 500)
    y = a / (x + b) + c
    
    # Plotly 그래프
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines', name='유리함수'))
    fig.update_layout(title="y = a / (x + b) + c",
                      xaxis_title="x",
                      yaxis_title="y",
                      height=500)
    st.plotly_chart(fig, use_container_width=True)
    
    # 뒤로가기 버튼
    if st.button("⬅️ 메인으로 돌아가기"):
        st.session_state.page = "main"

# 페이지 이동
if st.session_state.page == "main":
    main_page()
else:
    detail_page(st.session_state.page)
