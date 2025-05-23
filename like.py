import streamlit as st
import random

# 페이지 설정
st.set_page_config(page_title="영단어 퀴즈", page_icon="🧠", layout="centered")

# 타이틀
st.title("🔤 수능 고난도 영단어 퀴즈")
st.markdown("고등학생을 위한 뇌를 깨우는 단어 테스트! ✍️\n")

# 퀴즈 데이터 (단어: 뜻)
quiz_data = {
    "alleviate": "완화하다",
    "ambiguous": "애매한",
    "benevolent": "자비로운",
    "candid": "솔직한",
    "deteriorate": "악화되다",
    "eradicate": "근절하다",
    "feasible": "실현 가능한",
    "impartial": "공정한",
    "meticulous": "꼼꼼한",
    "plausible": "그럴듯한"
}

# 퀴즈 준비
word, correct_answer = random.choice(list(quiz_data.items()))
wrong_answers = random.sample([v for k, v in quiz_data.items() if v != correct_answer], 3)
options = wrong_answers + [correct_answer]
random.shuffle(options)

# 퀴즈 출제
st.markdown(f"### ❓ 단어의 뜻을 고르세요: **{word}**")
user_answer = st.radio("선택지", options, index=None, key=word)

# 피드백
if user_answer:
    if user_answer == correct_answer:
        st.success("🎉 정답입니다! 잘했어요!")
    else:
        st.error(f"😢 아쉽네요. 정답은 **{correct_answer}** 입니다.")

    st.markdown("🔁 [다시 풀기](#)", unsafe_allow_html=True)
    st.markdown("---")
    st.caption("Tip: 단어는 수능 빈출 고난도 단어로 구성되어 있어요!")

# 푸터
st.markdown("---")
st.markdown("Made with ❤️ for 고등학생 | Powered by Streamlit 🚀")

