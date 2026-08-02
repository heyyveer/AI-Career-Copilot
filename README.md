# 🚀 AI Career Copilot

An AI-powered Resume Analyzer and Career Assistant built using **LangChain**, **LangGraph**, **RAG**, and **Large Language Models (LLMs)**. The application helps users analyze resumes, interact with their resumes through natural language, evaluate ATS compatibility, and receive AI-driven career recommendations.

---

## ✨ Planned Features

- 📄 Resume Upload & Parsing
- 💬 Talk to Your Resume (RAG)
- 📊 ATS Score Analysis
- 🎯 Resume Improvement Suggestions
- 🧠 Skill Extraction
- 📌 Experience & Project Analysis
- 📝 Resume Summary Generation
- 📋 Job Description Matching
- ❓ AI-Generated Interview Questions
- 💼 Career Guidance & Recommendations

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangGraph**
- **FastAPI**
- **LLMs (Gemini / Groq / OpenAI)**
- **FAISS / ChromaDB**
- **Pydantic**
- **python-dotenv**

---

## 📂 Project Structure

```text
AI-Career-Copilot/
│
├── agents/
├── utils/
├── uploads/
├── vector_store/
├── data/
│
├── app.py
├── graph.py
├── states.py
├── prompts.py
│
├── .env
├── requirements.txt
└── README.md
```

---

## 🧠 Architecture

```text
Resume Upload
      │
      ▼
PDF Parsing
      │
      ▼
Text Chunking
      │
      ▼
Embeddings
      │
      ▼
Vector Database
      │
      ▼
LangGraph Workflow
      │
      ├── Resume Chat Agent
      ├── ATS Analysis Agent
      ├── Suggestion Agent
      ├── JD Match Agent
      ├── Interview Agent
      └── Summary Agent
```

---

## 🚧 Project Status

> 🚀 Currently under active development.

Upcoming milestones:

- [ ] Resume Parsing
- [ ] Embedding Pipeline
- [ ] Vector Database Integration
- [ ] LangGraph Workflow
- [ ] Resume Chat
- [ ] ATS Analyzer
- [ ] Job Description Matching
- [ ] Interview Question Generator
- [ ] FastAPI Integration
- [ ] Frontend Integration

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you find this project interesting, consider giving it a star!