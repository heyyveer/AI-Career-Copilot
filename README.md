# 🚀 AI Career Copilot

An AI-powered **Resume Analyzer & Career Assistant** built using **Streamlit**, **LangChain**, **FAISS**, **RAG**, and **Large Language Models (LLMs)**.

AI Career Copilot helps users analyze their resumes, compare them against job descriptions, receive ATS optimization suggestions, generate professional summaries, and interact with their resumes through natural language.

---

## 🎥 Demo

<p align="center">
  <img src="assets/demo.gif" alt="AI Career Copilot Demo" width="900"/>
</p>

# ✨ Features

### 📄 Resume Processing
- Upload Resume (PDF)
- Automatic Resume Parsing
- Resume Chunking
- Embedding Generation
- FAISS Vector Database Creation

### 📊 Resume Analysis
- ATS Score Analysis
- Resume Match Score
- Resume Strengths & Weaknesses
- Missing Skills Detection
- Missing ATS Keywords
- Resume Formatting Review

### 🎯 Job Matching
- Job Description Matching
- Target Role Analysis
- Skill Gap Analysis

### 📝 AI Resume Assistance
- Professional Resume Summary
- Resume Improvement Suggestions
- Career Recommendations

### 💬 Talk to Resume
Ask anything about your resume.

Examples:

- Explain my projects.
- What are my strongest skills?
- Rewrite my experience.
- Improve my resume.
- Suggest certifications.
- Tailor my resume for AI Engineer.
- What keywords am I missing?

---

# 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Frontend | Streamlit |
| LLM | Groq (GPT-OSS-20B) |
| Framework | LangChain |
| Vector Database | FAISS |
| Embeddings | Gemini Embedding 2 |
| Prompt Engineering | Custom Prompts |
| Environment | Python |

---

# 📂 Project Structure

```text
AI-Career-Copilot/

│── app.py
│── agents.py
│── prompts.py
│── process_resume.py
│── states.py
│── utils.py

│── uploads/
│── vector_store/

│── .env
│── requirements.txt
│── README.md
```

---

# 🏗 Architecture

```text
                  Upload Resume
                        │
                        ▼
                 PDF Processing
                        │
                        ▼
                Text Chunking
                        │
                        ▼
              Gemini Embeddings
                        │
                        ▼
                 FAISS Vector DB
                        │
                        ▼
            Resume Analysis Engine
                        │
      ┌─────────────────┼─────────────────┐
      ▼                 ▼                 ▼
 Resume Analysis    AI Summary      Suggestions
                        │
                        ▼
                Talk To Resume (RAG)
```

---

# 🚀 Application Workflow

```text
Upload Resume
      │
      ▼
Resume Processing
      │
      ▼
FAISS Index Creation
      │
      ▼
Target Role
      │
      ▼
Job Description
      │
      ▼
AI Resume Analysis
      │
      ├── ATS Analysis
      ├── Resume Summary
      ├── Suggestions
      └── Resume Review
      │
      ▼
Talk To Resume
```

---

# 📸 Screenshots

> Screenshots will be added after the UI is completed.

---

# 🔮 Upcoming Features

- [ ] Multi Resume Support
- [ ] Resume Version Comparison
- [ ] Download Resume Analysis Report (PDF)
- [ ] Resume Rewriting
- [ ] Cover Letter Generator
- [ ] LinkedIn Profile Review
- [ ] Portfolio Website Review
- [ ] AI Mock Interview
- [ ] Multi-LLM Support
- [ ] LangGraph Multi-Agent Workflow

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/AI-Career-Copilot.git
```

Move to the project directory

```bash
cd AI-Career-Copilot
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=your_api_key
GROQ_API_KEY=your_api_key
```

Run the application

```bash
streamlit run app.py
```

---

# 🤝 Contributing

Contributions are welcome!

Feel free to fork this repository, improve the project, and submit a pull request.

---

# 📜 License

This project is licensed under the MIT License.

---

# ⭐ Support

If you found this project helpful, please consider giving it a ⭐ on GitHub.
