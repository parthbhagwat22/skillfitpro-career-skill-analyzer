import streamlit as st
from utils import (
    extract_text_from_pdf,
    extract_skills,
    get_missing_skills,
    generate_learning_roadmap,
    export_pdf
)

# ---------- STREAMLIT APP ----------
st.set_page_config(page_title="SkillFitPro - Career Skill Analyzer", layout="centered")

st.title("📄 SkillFitPro")
st.markdown(
    """
    **Developed by:** Parth Bhagwat  
    **Role:** Aspiring Data Scientist | AI & GenAI Enthusiast  

    This tool analyzes your resume against a Job Description,  
    finds missing skills, and gives you a focused learning roadmap.
    """,
    unsafe_allow_html=True
)

# ---- Resume Upload ----
resume_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

# ---- Job Description Text ----
jd_text = st.text_area("Paste Job Description here", height=200, placeholder="Paste the JD here...")

# ---- Analyze Button ----
if st.button("Analyze") and resume_file and jd_text.strip():
    with st.spinner("Analyzing your resume..."):

        # 1. Extract text from resume
        resume_text = extract_text_from_pdf(resume_file)

        # 2. Extract skills from resume and JD
        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(jd_text)

        # 3. Find missing skills
        missing_skills = get_missing_skills(jd_skills, resume_skills)

        # 4. Generate learning roadmap
        roadmap = generate_learning_roadmap(missing_skills)

        # 5. Export PDF report
        export_pdf(resume_skills, jd_skills, missing_skills, roadmap, jd_text)

    st.success("✅ Analysis complete!")

    # Display results
    st.subheader("Skills in Resume")
    st.write(", ".join(resume_skills) if resume_skills else "No skills found.")

    st.subheader("Skills in Job Description")
    st.write(", ".join(jd_skills) if jd_skills else "No skills found.")

    st.subheader("Missing Skills")
    st.write(", ".join(missing_skills) if missing_skills else "No missing skills!")

    st.subheader("Learning Roadmap")
    for skill, steps in roadmap.items():
        st.markdown(f"**{skill}**")
        st.write(steps)

    # Download button
    with open("career_report.pdf", "rb") as pdf_file:
        st.download_button(
            label="📥 Download Career Report",
            data=pdf_file,
            file_name="career_report.pdf",
            mime="application/pdf"
        )

else:
    st.info("Please upload your resume and paste a job description to start.")
