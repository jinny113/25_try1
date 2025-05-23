import streamlit as st
from PIL import Image

# 페이지 기본 설정
st.set_page_config(page_title="나의 소개 페이지", page_icon="👤", layout="centered")

# 제목
st.title("👋 안녕하세요! 반갑습니다.")
st.subheader("이곳은 나를 소개하는 페이지입니다.")

# 사진 업로드
st.markdown("### 📷 프로필 사진 업로드")
uploaded_image = st.file_uploader("사진을 선택하세요", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    image = Image.open(uploaded_image)
    st.image(image, caption="나의 프로필 사진", use_column_width=True)

# 사용자 정보 입력
st.markdown("### 📝 나의 정보 입력")

name = st.text_input("이름")
school = st.text_input("학교")
hobby = st.text_area("취미")
email = st.text_input("이메일")

# 결과 출력
if name and school and hobby and email:
    st.markdown("---")
    st.markdown("### 👤 나의 소개")
    st.write(f"**이름:** {name}")
    st.write(f"**학교:** {school}")
    st.write(f"**취미:** {hobby}")
    st.write(f"**이메일:** {email}")
    st.success("정보가 성공적으로 입력되었습니다!")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")
