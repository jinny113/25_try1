import streamlit as st
from PIL import Image

# 페이지 기본 설정
st.set_page_config(page_title="나의 소개 페이지", page_icon="👤", layout="centered")

# 제목
st.title("👋 안녕하세요! 반갑습니다.")
st.subheader("이곳은 나를 소개하는 페이지입니다.")

# ======= 여기에 당신의 정보를 입력하세요 =======
name = "이수진"        # ← 이름을 여기에 입력
school = "고려대학교"  # ← 학교 이름을 여기에 입력
hobby = "독서, 게임, 음악 감상"  # ← 취미를 여기에 입력
email = "hong@example.com"  # ← 이메일을 여기에 입력
image_path = "profile.jpg"  # ← 프로필 사진 파일명 (같은 폴더에 있어야 함)
# =============================================

# 프로필 사진 표시
try:
    image = Image.open(image_path)
    st.image(image, caption="나의 프로필 사진", use_column_width=True)
except FileNotFoundError:
    st.warning("⚠️ 프로필 사진 파일을 찾을 수 없습니다. 파일 이름을 확인하세요.")

# 나의 정보 표시
st.markdown("### 👤 나의 소개")
st.write(f"**이름:** {name}")
st.write(f"**학교:** {school}")
st.write(f"**취미:** {hobby}")
st.write(f"**이메일:** {email}")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
