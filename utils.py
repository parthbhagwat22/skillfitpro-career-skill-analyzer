import fitz  # PyMuPDF for PDF text extraction
import cohere
import os
from dotenv import load_dotenv
from rapidfuzz import fuzz

# Load .env for API key
load_dotenv()

# Initialize Cohere client
co = cohere.Client(os.getenv("COHERE_API_KEY"))

# ✅ 1. Extract text from PDF resume
def extract_text_from_pdf(uploaded_file):
    """
    Reads an uploaded PDF file and extracts all text from it.
    """
    text = ""
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text.strip()

# ✅ 2. Extract skills using Cohere LLM
def extract_skills(text):
    """
    Uses Cohere's LLM to extract only technical & soft skills as a list.
    """
    prompt = (
        "Extract only the technical and soft skills as a comma-separated list from the following text. "
        "Avoid extra explanations or formatting.\n\n" + text
    )

    try:
        response = co.generate(
            model="command-r-plus",
            prompt=prompt,
            max_tokens=300,
            temperature=0.3
        )
    except Exception as e:
        return []

    raw_skills = response.generations[0].text.strip()
    skills = [skill.strip() for skill in raw_skills.split(',') if skill.strip()]
    return skills

# ✅ 3. Compare and find missing skills
def get_missing_skills(jd_skills, resume_skills):
    """
    Finds skills in the job description that are not present in the resume.
    Uses fuzzy matching for flexibility in skill wording.
    """
    resume_skills_lower = [skill.lower() for skill in resume_skills]
    missing_skills = []

    for jd_skill in jd_skills:
        jd_lower = jd_skill.lower()
        match_score = max([fuzz.partial_ratio(jd_lower, res) for res in resume_skills_lower], default=0)
        if match_score < 70:
            missing_skills.append(jd_skill)

    return missing_skills

# ✅ 4. Generate a learning roadmap for missing skills
def generate_learning_roadmap(missing_skills):
    """
    For each missing skill, uses Cohere to suggest a short 4-step learning plan.
    """
    roadmap = {}
    for skill in missing_skills:
        clean_skill = skill.strip().replace(".", "").title()

        prompt = (
            f"You are a career coach. Suggest a short, practical learning roadmap for mastering '{clean_skill}'.\n"
            f"Include exactly 4 steps:\n"
            f"1. A brief theory/fundamentals learning step\n"
            f"2. A free or popular online course/resource suggestion\n"
            f"3. A hands-on project or practice activity suggestion\n"
            f"4. A way to showcase this skill on a resume or portfolio"
        )

        try:
            response = co.generate(
                model="command-r-plus",
                prompt=prompt,
                max_tokens=200,
                temperature=0.5
            )
            roadmap[clean_skill] = response.generations[0].text.strip()
        except:
            roadmap[clean_skill] = "Roadmap generation failed. Please try again."

    return roadmap

# ✅ 5. Export report to PDF
def export_pdf(resume_skills, jd_skills, missing_skills, roadmap, jd_text=None):
    """
    Creates a PDF report summarizing the analysis.
    """
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.pagesizes import A4
    from reportlab.lib import colors

    doc = SimpleDocTemplate("career_report.pdf", pagesize=A4)
    styles = getSampleStyleSheet()
    story = []

    # Title
    story.append(Paragraph("SkillFitPro Career Report", styles['Title']))
    story.append(Paragraph("Developed by: Parth Bhagwat", styles['Normal']))
    story.append(Spacer(1, 12))

    # Resume Skills
    story.append(Paragraph("Resume Skills", styles['Heading2']))
    story.append(Paragraph(", ".join(resume_skills) if resume_skills else "No skills found.", styles['Normal']))
    story.append(Spacer(1, 12))

    # JD Skills
    story.append(Paragraph("Job Description Skills", styles['Heading2']))
    story.append(Paragraph(", ".join(jd_skills) if jd_skills else "No skills found.", styles['Normal']))
    story.append(Spacer(1, 12))

    # Missing Skills Table
    story.append(Paragraph("Missing Skills", styles['Heading2']))
    if missing_skills:
        table_data = [[skill] for skill in missing_skills]
        table = Table(table_data, colWidths=[250])
        table.setStyle(TableStyle([
            ('GRID', (0, 0), (-1, -1), 0.5, colors.black),
            ('FONTNAME', (0, 0), (-1, -1), 'Helvetica')
        ]))
        story.append(table)
    else:
        story.append(Paragraph("No missing skills! You are a good match.", styles['Normal']))
    story.append(Spacer(1, 12))

    # Learning Roadmap
    story.append(Paragraph("Learning Roadmap", styles['Heading2']))
    if roadmap:
        for skill, steps in roadmap.items():
            story.append(Paragraph(f"<b>{skill}</b>", styles['Heading3']))
            for line in steps.split("\n"):
                story.append(Paragraph(f"- {line}", styles['Normal']))
            story.append(Spacer(1, 6))

    # Job Description at the end
    if jd_text:
        story.append(Spacer(1, 12))
        story.append(Paragraph("Full Job Description", styles['Heading2']))
        story.append(Paragraph(jd_text, styles['Normal']))

    doc.build(story)
