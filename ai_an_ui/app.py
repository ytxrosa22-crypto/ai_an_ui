import streamlit as st
from google import genai
from google.genai import types

st.set_page_config(page_title="Piroh - Tri kỷ ảo", page_icon="🧸", layout="centered")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #FFF0F5 !important;
    }
    h1 {
        color: #FF69B4 !important;
    }
    .stMarkdown p, [data-testid="stCaptionContainer"] {
        color: #4A2E35 !important;
    }
    [data-testid="stChatInput"] {
        background-color: #FFE4E1 !important;
        border-radius: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧸 AI Piroh")
st.caption("Một người bạn luôn ở đây, lắng nghe và xoa dịu những nỗi buồn của cậu. 🤍")

API_KEY = "AQ.Ab8RN6K844gdQNNWaHBzMB8-H6fnpH5nuZur-Kli4xEr2rfYZg"

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Chào cậu, tớ đã sẵn sàng lắng nghe cậu rồi đây! 🧸"}
    ]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

user_input = st.chat_input("Tâm sự với Piroh ở đây nhé...")

if user_input:
    with st.chat_message("user"):
        st.write(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        try:
            client = genai.Client(api_key=API_KEY)
            prompt_ho_tro = (
                "Bạn là một người bạn tri kỷ ảo vô cùng ấm áp và tinh tế tên là Piroh. "
                "Nhiệm vụ của bạn là lắng nghe, xoa dịu và an ủi người dùng. "
                "Luôn xưng hô thân mật là tớ - cậu. Trả lời ngắn gọn, tự nhiên, Gen Z một chút, không dùng icon quá đà.\n"
                f"Câu hỏi của người dùng: {user_input}"
            )
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_ho_tro
            )
            ai_reply = response.text
        except Exception as e:
            ai_reply = f"Ôi, hình như đường truyền của tớ hơi bận một chút... (Lỗi: {str(e)})"
            
        st.write(ai_reply)
            
    st.session_state.messages.append({"role": "assistant", "content": ai_reply})
    st.rerun()