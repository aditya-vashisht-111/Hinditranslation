# 🇮🇳 Hindi Vision Translator
### AI-Powered Study Companion for Language Learners

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Integration-green?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Model-Gemini%202.0%20Flash-4285F4?style=for-the-badge&logo=google)

> **Transform blurry textbook photos into beautiful, structured English study notes in seconds.**

---

## 📖 About The Project

The **Hindi Vision Translator** is a local AI agent designed to bridge the gap between physical Hindi textbooks and digital study notes. Built using **Streamlit** and powered by Google's latest **Gemini 2.0 Flash** model, this tool doesn't just translate text—it acts as a teacher.

It takes an image of a Hindi page, analyzes the context, and generates a formatted study guide with line-by-line translations, vocabulary highlights, and emojis for better retention.

### ✨ Key Features
* **👁️ Computer Vision:** Instantly reads Hindi text from images (JPG/PNG).
* **⚡ Gemini 2.0 Flash:** Uses Google's fastest multimodal model for near-instant results.
* **📝 Smart Formatting:**
    * **Line-by-Line Translation:** Hindi line first, English line immediately after.
    * **No Parentheses:** Clean, readable text flow.
    * **Auto-Beautification:** Adds emojis, bold text, and bullet points automatically.
* **📥 Export Ready:** Download your generated notes directly as a Markdown/Text file.

---

## 🛠️ Tech Stack

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Frontend** | Streamlit | Fast UI for uploading images and viewing results. |
| **Orchestration** | LangChain | Manages the prompt engineering and model connection. |
| **AI Model** | Gemini 2.0 Flash | The multimodal LLM handling vision and translation. |
| **Language** | Python | Core logic. |
