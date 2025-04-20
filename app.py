import streamlit as st
import subprocess
from datetime import datetime
import os

# ==== Page Config ====
st.set_page_config(
    page_title="💼 Job Advisor Chatbot",
    page_icon="🤖",
    layout="centered"
)

# ==== Logo ====
st.image("assets/logo.png", width=100)
st.title("🤖💬 Local Job Role Advisor Chatbot")
st.markdown("Ask about any **job role**, **career path**, or **skills** — powered by *DeepSeek* (offline).")

# ==== Session State ====
if "messages" not in st.session_state:
    st.session_state.messages = []

# ==== Sidebar ====
st.sidebar.title("🛠️ Options")
if st.sidebar.button("🧹 Clear Chat"):
    st.session_state.messages = []

if st.sidebar.button("💾 Save Chat as .txt"):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"chat_{timestamp}.txt"
    with open(filename, "w", encoding="utf-8") as f:
        for msg in st.session_state.messages:
            role = "User" if msg["role"] == "user" else "Bot"
            f.write(f"{role}: {msg['content']}\n\n")
    st.sidebar.success(f"Saved as {filename}")

st.sidebar.markdown("---")
st.sidebar.markdown("Built with ❤️ using Streamlit + Ollama (DeepSeek)")

# ==== Show Chat History ====
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ==== Chat Input ====
user_input = st.chat_input("Ask me about jobs, roles, or skills...")

if user_input:
    st.chat_message("user").markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.spinner("Thinking with DeepSeek..."):
        prompt = f"You are a helpful job and career advisor. Answer the following:\n{user_input}"

        result = subprocess.run(
            ["ollama", "run", "deepseek-coder", prompt],
            capture_output=True,
            text=True
        )

        response = result.stdout.strip()

    st.chat_message("assistant").markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
