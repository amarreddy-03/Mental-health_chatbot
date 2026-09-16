import streamlit as st
from responses import get_response

st.set_page_config(
    page_title="MindCare",
    page_icon="🧠",
    layout="wide"
)
def load_css():
    with open("style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ---------------- Session State ---------------- #

if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- Sidebar ---------------- #

st.sidebar.title("🧠 MindCare")

page = st.sidebar.radio(
    "Navigation",
    [
        "🏠 Home",
        "💬 Chat",
        "📖 Self Help",
        "🧘 Relax",
        "📞 Help",
        "ℹ About"
    ]
)

# ---------------- Home ---------------- #

if page == "🏠 Home":

    st.title("🧠 MindCare")

    st.subheader("Your Mental Wellness Companion ❤️")

    st.write(
        """
Welcome to MindCare.

This chatbot provides supportive conversations using
simple rule-based responses.

✔ Stress Relief

✔ Motivation

✔ Study Tips

✔ Positive Thinking

✔ Friendly Conversations
"""
    )

    st.info("Choose 'Chat' from the sidebar to start chatting.")

# ---------------- Chat ---------------- #

elif page == "💬 Chat":

    st.title("💬 Mental Health Chatbot")

    for message in st.session_state.messages:

        with st.chat_message(message["role"]):
            st.write(message["content"])

    user_input = st.chat_input("Type your message...")

    if user_input:

        st.session_state.messages.append(
            {
                "role":"user",
                "content":user_input
            }
        )

        with st.chat_message("user"):
            st.write(user_input)

        reply = get_response(user_input)

        st.session_state.messages.append(
            {
                "role":"assistant",
                "content":reply
            }
        )

        with st.chat_message("assistant"):
            st.write(reply)

    if st.button("🗑 Clear Chat"):
        st.session_state.messages = []
        st.rerun()

# ---------------- Self Help ---------------- #

elif page == "📖 Self Help":

    st.title("📖 Self Help")

    st.success("Stress Management")

    st.write("""
• Take deep breaths.

• Exercise daily.

• Drink enough water.

• Talk with friends.

• Sleep for 7–8 hours.
""")

    st.success("Study Tips")

    st.write("""
• Study for 25 minutes.

• Take a 5-minute break.

• Avoid distractions.

• Revise regularly.
""")

    st.success("Positive Thinking")

    st.write("""
• Believe in yourself.

• Celebrate small achievements.

• Learn from mistakes.
""")

# ---------------- Relax ---------------- #

elif page == "🧘 Relax":

    st.title("🧘 Relaxation")

    st.write("### Deep Breathing")

    st.info("""
Inhale for 4 seconds

Hold for 4 seconds

Exhale for 4 seconds

Repeat five times.
""")

    st.write("### Relaxation Tips")

    st.write("""
🎵 Listen to soft music

🚶 Go for a walk

🧘 Practice meditation

📖 Read a book

🌿 Spend time in nature
""")

# ---------------- Help ---------------- #

elif page == "📞 Help":

    st.title("📞 Need Help?")

    st.warning("""
If you're feeling overwhelmed or in immediate danger,
please contact someone you trust or your local emergency
or mental health services right away.

You don't have to face it alone.
""")

# ---------------- About ---------------- #

elif page == "ℹ About":

    st.title("ℹ About")

    st.write("""
Project Name:
Mental Health Chatbot

Type:
Rule-Based Chatbot

Technologies Used:

• Python

• Streamlit

• Dictionary

• Session State

Developed For:

Mini Project
""")