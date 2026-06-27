![Python](https://img.shields.io/badge/Python-3.10-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Llama](https://img.shields.io/badge/Model-Llama_3.3_70B-green)
![Streamlit](https://img.shields.io/badge/UI-Streamlit-red)
![Docker](https://img.shields.io/badge/Container-Docker-blue)
![Prompt Engineering](https://img.shields.io/badge/Prompt-Engineering-orange)
![JSON](https://img.shields.io/badge/Output-Structured_JSON-green)

# 📄 AI Resume Reviewer

An AI-powered Resume Reviewer built using **Groq API**, **Llama 3.3**, and **Streamlit** that analyzes PDF resumes, compares them against job descriptions, calculates ATS and job match scores, and rewrites resumes for better ATS optimization.

This project demonstrates how modern LLM-powered applications process PDF documents, engineer prompts, generate structured JSON outputs, and build production-ready AI workflows.

---

## 🚀 Features

- 📄 Upload Resume PDFs
- 📋 Compare Resume with Job Description
- 📊 Generate ATS Score
- 🎯 Generate Job Match Score
- 🔍 Identify Matching Keywords
- ❌ Detect Missing Keywords
- 💪 Highlight Resume Strengths
- ⚠️ Detect Resume Weaknesses
- ✍️ AI-Powered Resume Rewriting
- 🤖 Powered by Groq API & Llama 3.3
- 🧠 Prompt Engineering
- 📦 Structured JSON Responses
- 🎨 Interactive Streamlit Web Interface
- 🐳 Dockerized Application
- 🔐 Secure API Key Management using Environment Variables

---

## 🏗️ Architecture

```text
                Resume PDF
                     │
                     ▼
             PDF Text Extraction
                     │
                     ▼
            Job Description Input
                     │
                     ▼
             Prompt Engineering
                     │
                     ▼
          Groq API (Llama 3.3)
                     │
                     ▼
         Structured JSON Response
                     │
        ┌────────────┴─────────────┐
        ▼                          ▼
 Resume Analysis          Resume Rewriting
        │                          │
        ▼                          ▼
 ATS Score               ATS Optimized Resume
 Match Score
 Missing Keywords
 Suggestions
```

---

## 📂 Project Structure

```text
resume-reviewer/
│
├── app.py                     # CLI application
├── streamlit_app.py           # Streamlit web interface
├── parser.py                  # PDF & JD parsing
├── reviewer.py                # Groq API integration
├── prompts.py                 # Prompt templates
├── config.py                  # Environment configuration
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| LLM Provider | Groq API |
| Model | Llama 3.3 70B Versatile |
| Frontend | Streamlit |
| PDF Parsing | pypdf |
| Prompting | Prompt Engineering |
| Output Format | Structured JSON |
| Containerization | Docker |
| Environment Variables | python-dotenv |

---

## 📦 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/resume-reviewer.git

cd resume-reviewer
```

---

### 2. Create Virtual Environment

```bash
python -m venv venv
```

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file inside the project root.

```env
GROQ_API_KEY=your_groq_api_key
```

---

## ▶️ Running the CLI Version

```bash
python app.py
```

---

## 🌐 Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

Then open

```text
http://localhost:8501
```

---

## 🐳 Running with Docker

### Build Docker Image

```bash
docker build -t resume-reviewer .
```

### Run Docker Container

```bash
docker run -p 8501:8501 --env-file .env resume-reviewer
```

---

## 💡 How It Works

1. User uploads a resume PDF.
2. User pastes a Job Description.
3. PDF text is extracted using `pypdf`.
4. A prompt is dynamically generated.
5. Resume and Job Description are sent to Groq's Llama 3.3 model.
6. The model returns structured JSON.
7. Python parses the JSON response.
8. The application displays:
   - ATS Score
   - Match Score
   - Matching Keywords
   - Missing Keywords
   - Strengths
   - Weaknesses
   - Suggestions
9. Users can generate an ATS-optimized rewritten resume.

---

## 🧠 Key Concepts Learned

### 📄 PDF Parsing

Extracting text from PDF documents for LLM processing.

### 🤖 LLM API Integration

Integrating Python applications with Groq's ultra-fast inference API.

### 🧠 Prompt Engineering

Designing prompts that generate reliable, structured, and context-aware AI responses.

### 📦 Structured JSON Outputs

Generating machine-readable responses from LLMs.

### 📊 Resume ↔ Job Description Matching

Using LLMs to compare resumes against job requirements and identify skill gaps.

### ✍️ AI Resume Rewriting

Rewriting resumes while preserving factual information and improving ATS compatibility.

### 🎨 Streamlit

Building an interactive web interface for AI applications.

### 🐳 Docker

Containerizing AI applications for consistent deployment across environments.

---

## 🚀 Future Improvements

- 📄 Export analysis as PDF
- 📑 Export rewritten resume as DOCX
- 📈 ATS score visualization
- 📊 Resume benchmarking
- ⚡ FastAPI REST API
- 💾 Resume history
- 🔐 User authentication
- 🌍 Multi-language support
- 🧠 Native Structured Outputs
- ☁️ Cloud deployment (Render/AWS)

---

## ⚠️ Limitations

- ATS scores are AI-generated estimates and may differ from commercial ATS systems.
- Resume quality depends on PDF text extraction.
- Requires an active internet connection.
- Supports one resume at a time.

---

## 📚 Learning Outcomes

After building this project, you understand:

- PDF processing
- Prompt Engineering
- Groq API integration
- LLM application architecture
- Structured JSON outputs
- Resume ↔ Job Description matching
- AI-powered content rewriting
- Streamlit application development
- Docker containerization
- Environment variable management
- Modular Python project organization

---

## 🤝 Contributing

Contributions are welcome!

Possible improvements:

- Better prompt optimization
- Better error handling
- Improved UI/UX
- Additional export formats
- Multi-model support
- Cloud deployment

---

## ⭐ Acknowledgements

- Groq for ultra-fast LLM inference
- Meta for the Llama models
- Streamlit for rapid web app development
- pypdf for PDF parsing
- Docker for containerization

---

## 👨‍💻 Author

Built as a hands-on learning project while exploring **Generative AI**, **Prompt Engineering**, **LLM Applications**, **AI Engineering**, and **Production-Ready AI Systems**.
