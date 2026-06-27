import streamlit as st
from reviewer import ResumeReviewer
from parser import extract_text, extract_job_description

st.title("📄 AI Resume Reviewer")

resume = st.file_uploader(
    "Upload Resume",
    type=["pdf"]
)

jd = st.text_area(
    "Paste Job Description"
)

if st.button("Analyze"):
    resume_text = extract_text(resume)
    reviewer = ResumeReviewer()
    result = reviewer.review_resume(
        resume_text,
        jd
    )
    st.metric(
        "ATS Score",
        result['ats_score']
    )

    st.metric(
        "Match Score",
        result['match_score']
    )

    st.write(result['missing_keywords'])