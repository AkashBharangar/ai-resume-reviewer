![Python](https://img.shields.io/badge/Python-3.10-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Llama](https://img.shields.io/badge/Model-Llama_3.3_70B-green)
![Prompt Engineering](https://img.shields.io/badge/Prompt-Engineering-orange)
![JSON](https://img.shields.io/badge/Output-JSON-red)

# 📄 AI Resume Reviewer

An AI-powered Resume Reviewer built using **Groq API** and **Llama 3.3** that analyzes PDF resumes, generates an ATS score, identifies missing keywords, highlights strengths and weaknesses, and provides actionable improvement suggestions.

This project demonstrates how modern LLM-powered applications process PDF documents, engineer prompts, generate structured JSON outputs, and integrate AI into real-world workflows.

---

## 🚀 Features

- 📄 Accepts resume PDFs
- 📖 Extracts text from PDF documents
- 🤖 Uses Groq API with Llama 3.3
- 📊 Generates ATS score
- 🔍 Identifies missing keywords
- 💪 Highlights resume strengths
- ⚠️ Detects weaknesses
- 💡 Provides actionable improvement suggestions
- 🧠 Uses Prompt Engineering for reliable outputs
- 📦 Returns structured JSON responses
- 🔐 Secure API key management using environment variables

---

## 🏗️ Architecture

```text
Resume PDF
      │
      ▼
PDF Text Extraction
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
      ▼
JSON Parsing
      │
      ▼
ATS Score
Missing Keywords
Strengths
Weaknesses
Suggestions
```

---

## 📂 Project Structure

```text
resume-reviewer/
│
├── app.py                 # Main application
├── parser.py              # PDF text extraction
├── reviewer.py            # Groq API integration
├── prompts.py             # Prompt templates
├── config.py              # Environment configuration
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Language | Python |
| LLM | Groq API |
| Model | Llama 3.3 70B Versatile |
| PDF Parsing | pypdf |
| Prompting | Prompt Engineering |
| Output Format | JSON |
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

#### Mac/Linux

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

Obtain your API key from the Groq Console.

---

## ▶️ Running the Project

```bash
python app.py
```

Enter the path to your resume PDF.

Example:

```text
Enter Resume Path:
C:\Users\User\Documents\Resume.pdf
```

---

## 💡 How It Works

1. User provides the path to a resume PDF.
2. The application extracts text using `pypdf`.
3. A prompt is dynamically generated.
4. The resume is analyzed using Groq's Llama 3.3 model.
5. The model returns structured JSON.
6. Python parses the JSON response.
7. The application displays:
   - ATS Score
   - Missing Keywords
   - Strengths
   - Weaknesses
   - Suggestions

---

## 🧠 Key Concepts Learned

### 1. PDF Parsing

Extracting text from PDF documents for LLM processing.

### 2. Prompt Engineering

Designing prompts that generate reliable and structured AI responses.

### 3. LLM API Integration

Connecting Python applications with Groq's ultra-fast inference API.

### 4. Structured JSON Outputs

Generating machine-readable outputs from LLMs.

### 5. JSON Parsing

Converting LLM responses into Python dictionaries for downstream processing.

### 6. Modular Application Design

Separating application responsibilities into reusable modules.

---

## 🚀 Future Improvements

- 📋 Resume vs Job Description matching
- ✍️ AI-powered resume rewriting
- 🎨 Streamlit web interface
- ⚡ FastAPI REST API
- 📄 PDF report generation
- 📊 ATS score visualization
- 💾 Resume history
- 🌍 Multi-model support
- 🧠 Structured Outputs API
- 🐳 Docker deployment

---

## ⚠️ Limitations

- ATS score is AI-generated and may differ from commercial ATS systems.
- PDF parsing quality depends on the document format.
- Internet connection is required.
- Currently supports one resume at a time.

---

## 📚 Learning Outcomes

After building this project, you understand:

- PDF processing in Python
- Prompt Engineering
- Groq API integration
- LLM application architecture
- Structured JSON generation
- JSON parsing
- Environment variable management
- Modular Python application design

---

## 🤝 Contributing

Contributions are welcome!

Potential improvements include:

- Better prompt optimization
- Improved error handling
- Resume benchmarking
- Multiple model support
- Better CLI/UI
- Export reports

---

## ⭐ Acknowledgements

- Groq for ultra-fast LLM inference
- Meta for the Llama models
- pypdf for PDF text extraction

---

## 👨‍💻 Author

Built as a learning project while exploring **Generative AI**, **Prompt Engineering**, **LLM Applications**, and **AI Engineering**.
