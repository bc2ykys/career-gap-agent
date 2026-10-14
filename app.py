"""Career Gap Agent - Streamlit demo."""
import streamlit as st
from agent.parser import parse_resume_text
from agent.gap import find_gaps
from agent.planner import build_plan
from agent.quiz import build_quiz
from roles import ROLES

st.set_page_config(page_title="Career Gap Agent", layout="wide")
st.title("Career Gap Agent — Education & Career AI")

col1, col2 = st.columns(2)
with col1:
    role = st.selectbox("Target role", list(ROLES.keys()))
    resume_text = st.text_area("Paste resume text (or upload PDF below)", height=200)
    pdf = st.file_uploader("Resume PDF", type=["pdf"])
with col2:
    st.subheader("Role skills")
    st.write(ROLES[role])

if st.button("Analyze gap"):
    if pdf is not None:
        from pypdf import PdfReader
        reader = PdfReader(pdf)
        resume_text = "\n".join([p.extract_text() or "" for p in reader.pages])
    skills = parse_resume_text(resume_text)
    gaps = find_gaps(skills, ROLES[role])
    st.subheader("Parsed skills")
    st.write(skills or "No skills detected — add more text.")
    st.subheader("Skill gaps")
    st.write(gaps or "No gaps — ready for stretch goals.")
    st.subheader("20-day plan")
    st.table(build_plan(gaps))
    st.subheader("Mock quiz")
    for i, q in enumerate(build_quiz(gaps), 1):
        st.write(f"{i}. {q}")
