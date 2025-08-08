# 📄 SkillFitPro – AI-Powered Career Skill Analyzer

**SkillFitPro** is an AI-powered tool that analyzes your resume against a job description, identifies missing skills, and generates a personalized learning roadmap — helping job seekers close skill gaps faster.

🚀 **Live Demo:** [Click Here](https://skillfitpro.streamlit.app/)  
💻 **GitHub Repo:** [Click Here](https://github.com/yourusername/skillfitpro-career-skill-analyzer)  

---

## ✨ Features
- **Upload Resume (PDF)** – Extracts all text using PyMuPDF.
- **Paste Job Description** – Extracts skills using Cohere AI.
- **Skill Comparison** – Finds missing skills with fuzzy matching.
- **Learning Roadmap** – AI-generated 4-step plan for each missing skill.
- **Downloadable Report** – Generates a recruiter-ready PDF.

---

## 🛠 Tech Stack
| Technology | Purpose |
|------------|---------|
| **Python** | Core programming language |
| **Streamlit** | Web app UI |
| **Cohere API** | AI-powered skill extraction & roadmap generation |
| **PyMuPDF (fitz)** | PDF text extraction |
| **RapidFuzz** | Fuzzy string matching |
| **ReportLab** | PDF report generation |
| **python-dotenv** | Environment variable management |

---

## 📂 Project Structure
.
├── app.py # Streamlit frontend
├── utils.py # Backend utility functions
├── requirements.txt # Python dependencies
├── .env.example # API key template (no real key)
├── .gitignore # Ignore sensitive files
└── README.md # Project documentation


---

## ⚡ How It Works
1. **Upload your resume (PDF)**.
2. **Paste a job description** in the text box.
3. The app:
   - Extracts text from your resume & JD.
   - Uses Cohere AI to extract technical & soft skills.
   - Finds missing skills with fuzzy matching.
   - Generates a 4-step learning roadmap.
4. **Download your personalized career report** as a PDF.

---

## 📸 Screenshots

### 1️⃣ Upload Resume & Paste JD
![Upload Resume](https://github.com/parthbhagwat22/skillfitpro-career-skill-analyzer/blob/a93599d0fad410edbec3055eebc71bd9d8370a09/screenshots/upload_resume/Screenshot%202025-08-08%20140336.png)

### 2️⃣ Skills Analysis
![Analysis Results](https://github.com/parthbhagwat22/skillfitpro-career-skill-analyzer/blob/a93599d0fad410edbec3055eebc71bd9d8370a09/screenshots/skill_comparison/Screenshot%202025-08-08%20140425.png)

### 3️⃣ Learning Roadmap
![Learning Roadmap](https://github.com/parthbhagwat22/skillfitpro-career-skill-analyzer/blob/a93599d0fad410edbec3055eebc71bd9d8370a09/screenshots/roadmap/Screenshot%202025-08-08%20140457.png)

### 4️⃣ PDF Report
![PDF Report](https://github.com/parthbhagwat22/skillfitpro-career-skill-analyzer/tree/a93599d0fad410edbec3055eebc71bd9d8370a09/screenshots/pdf_report)


## 📦 Installation & Setup (Local)
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/yourusername/skillfitpro-career-skill-analyzer.git
cd skillfitpro-career-skill-analyzer
pip install -r requirements.txt


🚀 Future Improvements
Support for scanned resumes via OCR.

Multiple JD comparison.

Semantic matching with embeddings.

LinkedIn job scraping integration.

👨‍💻 Author
Parth Bhagwat
Aspiring Data Scientist | AI & GenAI Enthusiast
🔗 LinkedIn | Portfolio

📜 License
This project is licensed under the MIT License.

yaml
Copy
Edit

---

If you want, I can now make you a **LinkedIn post draft** from this README so you can announce your project the same day you push it to GitHub and deploy it.  
Do you want me to prepare that next?








Ask ChatGPT
