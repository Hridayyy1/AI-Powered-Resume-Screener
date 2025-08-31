import streamlit as st
import pandas as pd
from io import BytesIO
from docx import Document
import PyPDF2
import re
import plotly.express as px

# Gemini API setup (using OpenAI Python client as proxy)
from openai import OpenAI
client = OpenAI(api_key="YOUR_GEMINI_API_KEY")


# --- Helper Functions ---

def extract_text(file):
    """Extract text from PDF/DOCX/TXT"""
    text = ""
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() + "\n"
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    else:
        text = file.read().decode("utf-8")
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


def semantic_score(resume_text, job_desc):
    """Compute similarity score using Gemini API"""
    prompt = f"""
    You are an AI assistant. Evaluate similarity between the resume and the job description.
    Resume: {resume_text}
    Job Description: {job_desc}
    Provide a single similarity score between 0 and 100 (higher is better).
    """
    response = client.chat.completions.create(
        model="gemini-1.5-t",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )
    try:
        score = float(re.findall(r'\d+\.?\d*', response.choices[0].message.content)[0])
    except:
        score = 0
    return score


def highlight_keywords(resume_text, keywords):
    """Highlight matched keywords in resume"""
    highlighted = resume_text
    for kw in keywords:
        highlighted = re.sub(f"(?i)({re.escape(kw)})", r"**\1**", highlighted)
    return highlighted


def get_keywords(job_desc):
    """Extract important keywords from JD"""
    words = re.findall(r'\b\w+\b', job_desc.lower())
    stopwords = set(["and", "or", "with", "the", "a", "to", "for", "of", "in"])
    keywords = [w for w in words if w not in stopwords and len(w) > 2]
    return list(set(keywords))


# --- Streamlit UI ---

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("AI Resume Screening Tool")

job_description = st.text_area("Enter Job Description", height=200)
uploaded_files = st.file_uploader(
    "Upload Resumes (PDF, DOCX, TXT)", 
    type=["pdf", "docx", "txt"], 
    accept_multiple_files=True
)

if st.button("Evaluate Resumes"):
    if not job_description:
        st.warning("Please enter a job description!")
    elif not uploaded_files:
        st.warning("Please upload at least one resume!")
    else:
        results = []
        keywords = get_keywords(job_description)
        with st.spinner("Processing Resumes..."):
            for file in uploaded_files:
                resume_text = extract_text(file)
                score = semantic_score(resume_text, job_description)
                highlighted_text = highlight_keywords(resume_text, keywords)
                results.append({
                    "Resume": file.name, 
                    "Score": score, 
                    "Highlighted": highlighted_text
                })

        # Convert to DataFrame for ranking
        df = pd.DataFrame(results).sort_values(by="Score", ascending=False)
        
        st.subheader("Resume Ranking")
        st.dataframe(df[["Resume", "Score"]], use_container_width=True)

        st.subheader("Top Resume Preview with Keywords Highlighted")
        st.markdown(df.iloc[0]["Highlighted"])

        # Download results as CSV
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            label="Download Ranking as CSV",
            data=csv,
            file_name='resume_ranking.csv',
            mime='text/csv'
        )

        # Visual dashboard
        st.subheader("Resume Score Distribution")
        fig = px.bar(df, x="Resume", y="Score", text="Score", color="Score", color_continuous_scale="Viridis")
        st.plotly_chart(fig, use_container_width=True)
