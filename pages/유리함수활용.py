# app.py
import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(page_title="유리함수 창의융합 앱", layout="wide")

# 세션 상태 초기화
if "page" not in st.session_state:
    st.session_state.page = "main"

# 콘텐츠 정의
content = {
    "과학": {
        "emoji": "🧪",
        "title": "과학 - 빛의 굴절률",
        "desc": "빛의 굴절률과 유리함수 관계",
        "explanation": """**개념:**  
빛은 매질이 바뀌면 속도가 달라져 경로가 꺾입니다.  
굴절률 n = 진공에서 빛 속도 / 매질 속 속도  
입사각과 굴절각 변화는 유리함수 형태로 근사 가능.  

**활용:**  
광학 장치에서 빛 경로 설계 시 각 변화 예측 → 설계 최적화"""
    },
    "코딩": {
        "emoji": "💻",
        "title": "코딩 - UI 최적화",
        "desc": "UI 반응 속도 곡선 최적화",
        "explanation": """**개념:**  
화면 입력/조작에 따른 반응 속도를 설계.  
선형 변화는 부드럽지 않아 사용자 경험 저하.  

**유리함수 활용:**  
y = a / (x + b) + c  
- a: 초기 변화 폭  
- b: x축 이동/지연  
- c: 최종 y값 오프셋  
→ 슬라이더 조절로 반응 곡선 실험 가능"""
    },
    "예술": {
        "emoji": "🎨",
        "title": "예술 - 건축 디자인 곡선",
        "desc": "유리함수 기반 건축 곡선 디자인",
        "explanation": """**개념:**  
곡선 구조로 시각적 안정감과 공간감 향상, 직선보다 자연스러운 곡선 선호.  

**유리함수 사례:**  
- 루브르 피라미드 내부 통로: 점근선을 기준으로 곡선 벽 설계 → 안정감  
- 런던 밀레니엄 돔 내부 회랑: 접근하면서 좁아지는 곡선 → 유리함수 근사  
→ 점근선 기준으로 곡선 설계 → 디자인 미적 가치 + 이동 동선 최적화"""
    },
    "사회": {
        "emoji": "📈",
        "title": "사회 - 한계효용체감",
        "desc": "한계효용 그래프와 유리함수",
        "explanation": """**개념:**  
소비량 증가 → 만족 증가폭 감소 (한계효용 체감).  

**유리함수 활용:**  
y = a / (x + b) + c  
- 초기 만족 크고, 이후 증가폭 감소  
→ 경제 모델에서 소비·가격·수요 분석 활용"""
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
    # 맨 위에 뒤로가기
    if st.button("⬅️ 메인으로 돌아가기"):
        st.session_state.page = "main"
    
    st.header(f"{content[key]['emoji']} {content[key]['title']}")
    st.write(content[key]['explanation'])
    st.write("---")
    
    st.subheader("유리함수 그래프 시뮬레이션")
    st.write("슬라이더로 a, b, c 값을 바꾸어 그래프 형태를 확인할 수 있습니다.")
    st.write("y = a / (x + b) + c\n- a: 초기 값 크기\n- b: x축 이동/점근선 위치\n- c: y축 오프셋")
    
    # 슬라이더
    a = st.slider("a 값", 0.1, 10.0, 1.0)
    b = st.slider("b 값", 0.1, 10.0, 1.0)
    c = st.slider("c 값", -5.0, 5.0, 0.0)
    
    # x, y 계산
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

# 페이지 이동
if st.session_state.page == "main":
    main_page()
else:
    detail_page(st.session_state.page)
