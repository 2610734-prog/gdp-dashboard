import streamlit as st

# 1. 페이지 제목 및 레이아웃 설정
st.set_page_config(page_title="자외선 지수 안내 서비스", page_icon="☀️")
st.title("☀️ 실시간 자외선 지수 행동 요령")
st.write("현재 자외선 지수를 입력하시면 단계별 대처 방법을 안내해 드립니다.")

st.markdown("---")

# 2. 데이터 정의 (기존 리스트 유지)
uv_levels = ['낮음', '보통', '높음', '매우높음', '위험']
actions = [
    '자유롭게 야외활동 할 수 있습니다.',
    '모자 착용을 권장합니다.',
    '선크림을 바르고 외출을 자제하세요.',
    '오전10시부터 오후2시 사이에 외출을 자제하고 긴 옷을 착용하세요.',
    '야외활동을 금지하고 실내에 머무르세요.'
]

# 3. 스트림릿 위젯으로 입력 받기
# min_value=0 설정으로 음수 입력을 원천 차단하고, step=1로 정수만 입력받도록 유도합니다.
uv = st.number_input(
    '현재 자외선 지수를 입력하세요 (0 이상의 정수):', 
    min_value=0, 
    value=0, 
    step=1
)

st.markdown("### 📋 진단 결과")

# 4. 조건문 처리 및 스트림릿 전용 컴포넌트로 출력
if uv <= 2:
    st.info(f"**[{uv_levels[0]}]** 단계입니다. \n\n {actions[0]}")
elif uv <= 5:
    st.success(f"**[{uv_levels[1]}]** 단계입니다. \n\n {actions[1]}")
elif uv <= 7:
    st.warning(f"**[{uv_levels[2]}]** 단계입니다. \n\n {actions[2]}")
elif uv <= 10:
    st.error(f"**[{uv_levels[3]}]** 단계입니다. \n\n {actions[3]}")
else:
    # '위험' 단계는 강력한 빨간색 상자(st.error)로 시각적 경고 효과를 줍니다.
    st.error(f"🚨 **[{uv_levels[4]}]** 단계입니다. \n\n **{actions[4]}**")