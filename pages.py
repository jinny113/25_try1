import streamlit as st

# 페이지 설정
st.set_page_config(page_title="MBTI 직업 추천기", page_icon="🧠", layout="centered")

# 제목 영역
st.title("🔮 MBTI 기반 직업 추천기")
st.markdown("당신의 성격 유형에 어울리는 직업을 찾아보세요! 😎💼")

# MBTI 목록
mbti_types = [
    "INTJ", "INTP", "ENTJ", "ENTP",
    "INFJ", "INFP", "ENFJ", "ENFP",
    "ISTJ", "ISFJ", "ESTJ", "ESFJ",
    "ISTP", "ISFP", "ESTP", "ESFP"
]

# 추천 직업 데이터 (간단 예시)
mbti_jobs = {
    "INTJ": ["🔬 과학자", "📊 전략 기획가", "💻 데이터 분석가"],
    "INTP": ["🧪 연구원", "💡 발명가", "📚 교수"],
    "ENTJ": ["💼 CEO", "📈 경영 컨설턴트", "🏛️ 조직 관리자"],
    "ENTP": ["🎤 방송인", "🚀 스타트업 창업자", "🎭 창의 전략가"],
    "INFJ": ["🧘 상담사", "✍️ 작가", "🎨 예술가"],
    "INFP": ["🎨 일러스트레이터", "🎼 작곡가", "📖 시나리오 작가"],
    "ENFJ": ["🏫 교사", "💬 커뮤니케이션 전문가", "🌍 NGO 활동가"],
    "ENFP": ["🎤 아티스트", "🎬 영화감독", "🎉 이벤트 플래너"],
    "ISTJ": ["📚 공무원", "💼 회계사", "⚖️ 법률가"],
    "ISFJ": ["👩‍⚕️ 간호사", "🧑‍🏫 교사", "🗂️ 사서"],
    "ESTJ": ["🏦 은행원", "🔧 공장 관리자", "📊 프로젝트 매니저"],
    "ESFJ": ["💁‍♀️ 사회복지사", "🏥 병원 코디네이터", "🛍️ 고객 서비스 담당"],
    "ISTP": ["🔧 정비사", "🚓 경찰", "🕹️ 게임 개발자"],
    "ISFP": ["🎨 디자이너", "📷 사진작가", "🌿 플로리스트"],
    "ESTP": ["🎤 세일즈 전문가", "🚗 레이서", "📢 마케팅 담당자"],
    "ESFP": ["🎭 배우", "🎤 MC", "🎉 이벤트 코디네이터"]
}

# MBTI 선택
selected_mbti = st.selectbox("🧬 당신의 MBTI 유형을 선택하세요:", mbti_types)

# 추천 직업 출력
if selected_mbti:
    st.markdown("### 🧭 추천 직업 리스트")
    st.success(f"당신의 MBTI 유형은 **{selected_mbti}** 입니다!")
    st.write("당신에게 어울리는 직업은:")
    for job in mbti_jobs[selected_mbti]:
        st.markdown(f"- {job}")

# 이미지 또는 꾸밈 요소
st.markdown("---")
st.markdown("🎓 **진로는 나를 아는 것에서 시작됩니다!**")
st.markdown("📌 재미로 보는 테스트일 뿐, 자신만의 길을 찾아가세요! 💖")

# 푸터
st.markdown("---")
st.markdown("Made with 💖 by Your Name | Powered by Streamlit 🚀")

