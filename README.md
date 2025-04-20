Awesome! Let’s build a **beautiful and feature-rich Streamlit chatbot** using **DeepSeek via Ollama**, with:

✅ Local LLM (DeepSeek)  
✅ Save chat as `.txt`  
✅ Clear chat button  
✅ Streamlit theme & logo  
✅ Full folder + files + code + explanations

---

## 🏗️ Full Project Structure: `job_advisor_bot/`

```
job_advisor_bot/
├── app.py
├── requirements.txt
├── assets/
│   └── logo.png        ← optional logo
└── README.md           ← (optional for docs)
```

---

## 📦 Step 1: `requirements.txt`

```txt
streamlit
```

Install with:

```bash
pip install -r requirements.txt
```

---

## 🔧 Step 2: Pull the DeepSeek Model

If not yet done:

```bash
ollama pull deepseek-coder
```

---

## 🖼️ Step 3: Add a Logo

Create a folder `assets/` and place a logo named `logo.png`.

Example: `job_advisor_bot/assets/logo.png`

You can use any image (~200x200px) for this.

---

## 🧠 Step 4: Full Code — `app.py`

```python
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
```

---

## 🎨 Streamlit Theming (optional in `.streamlit/config.toml`)

Create a folder `.streamlit/` and a file `config.toml`:

```toml
[theme]
base="light"
primaryColor="#0e76a8"
backgroundColor="#f4f4f4"
secondaryBackgroundColor="#e3e3e3"
textColor="#000000"
font="sans serif"
```

---

## 🚀 Run Your App

```bash
streamlit run app.py
```

---

## ✅ What You Now Have

| Feature               | Enabled ✅ |
|-----------------------|------------|
| Local DeepSeek LLM    | ✅         |
| Save chat as `.txt`   | ✅         |
| Clear chat button     | ✅         |
| Logo support          | ✅         |
| Sidebar options       | ✅         |
| Chat history display  | ✅         |
| Stylish theme         | ✅         |

---

## 💡 Want to Add More?

- 🌍 Support multiple LLMs (dropdown: `deepseek`, `llama3`, etc.)
- 📤 Allow uploading user resumes for role-based suggestions
- 📈 Role trends (using job market data)

Would you like me to build a **multi-model selector** or **upload-resume + suggest jobs** version next?
