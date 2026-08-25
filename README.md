# 🤖 AI Job Resume Matcher

An intelligent web application that compares a candidate’s resume with a job description and calculates a compatibility score. It identifies matched skills, missing skills, and skills found in the resume.

## 📌 Project Overview

The AI Job Resume Matcher helps job seekers understand how well their resume matches a particular job description.

Users can upload a resume in PDF or DOCX format, paste a job description, and receive an instant analysis.

## ✨ Features

- Upload resumes in PDF or DOCX format
- Extract text automatically from resumes
- Compare resume content with a job description
- Calculate a resume match score
- Display the match level
- Identify matched technical skills
- Highlight missing skills
- Show all recognized skills found in the resume
- Clean and responsive Flask web interface
- Analyze multiple resumes

## 🛠️ Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- PyPDF
- python-docx

## 📂 Project Structure

```text
AI_Job_Resume_Matcher/
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── matcher.py
│   ├── resume_parser.py
│   └── skill_extractor.py
│
├── templates/
│   ├── index.html
│   └── results.html
│
├── static/
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── script.js
│
├── uploads/
├── test.py
├── requirements.txt
└── README.md
```

## ⚙️ How It Works

1. The user uploads a resume.
2. The application extracts text from the PDF or DOCX file.
3. The user enters a job description.
4. TF-IDF converts the resume and job description into numerical vectors.
5. Cosine similarity calculates the compatibility score.
6. The application extracts technical skills.
7. The result page displays matched and missing skills.

## 🚀 Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/shumaila-usha/AI-Job-Resume-Matcher.git
```

### 2. Open the project folder

```bash
cd AI-Job-Resume-Matcher
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

For Command Prompt:

```bat
venv\Scripts\activate
```

### 5. Install the required packages

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
python -m src.main
```

### 7. Open the application

Open the following address in your browser:

```text
http://127.0.0.1:5000/
```

## 📊 Example Result

```text
Match Score: 24.74%
Match Level: Low Match

Matched Skills:
Flask, Machine Learning, Pandas, Python, SQL, Scikit-learn

Skills to Improve:
AWS, Docker, Git, GitHub, NumPy
```

## 🎯 Purpose of the Project

This project helps job seekers improve their resumes by identifying missing technical skills and measuring compatibility with job descriptions.

It also demonstrates practical experience in:

- Natural Language Processing
- Text extraction
- Similarity measurement
- Skill extraction
- Flask web development
- Front-end design

## 🔮 Future Improvements

- Add AI-generated resume recommendations
- Support additional resume formats
- Improve skill recognition
- Add resume ranking for recruiters
- Generate downloadable analysis reports
- Add user accounts and analysis history
- Deploy the application online

## 🤝 Contributing

Contributions, suggestions, and improvements are welcome. Fork the repository and submit a pull request.

## 👩‍💻 Author

Developed as an AI and Machine Learning portfolio project.

## 📄 License

This project is intended for educational and portfolio purposes.

---

⭐ If you find this project useful, please give the repository a star!