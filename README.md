# AI-Powered-Resume-Screener

Absolutely! Here's a **professional, clean, and visually appealing README** for your AI Resume Screener project:

---

# AI-Powered Resume Screening Tool

**Developed by:** Hriday Ranawat
**Tech Stack:** Streamlit, Python, Gemini API, PyPDF2, python-docx, Pandas, Plotly

---

## **Project Overview**

This project is an **AI-based resume screening tool** that helps HR teams and recruiters **automatically evaluate and rank resumes** against a given job description.

Using **semantic matching powered by Gemini API**, the tool assesses how closely each candidate’s resume aligns with the job requirements and provides an **intuitive ranked list** along with highlighted key skills.

---

## **Features**

* **Resume Upload:** Supports `.pdf`, `.docx`, and `.txt` files.
* **Job Description Input:** Paste your job description to evaluate candidate fit.
* **Semantic Matching:** Uses Gemini API to score resumes on a scale of 0–100.
* **Keyword Highlighting:** Automatically highlights skills and keywords in resumes that match the job description.
* **Ranking Table:** Displays resumes sorted by match score.
* **Download Results:** Export ranked resumes and scores as a CSV file.
* **Interactive Dashboard:** Visual bar chart showing candidate-job fit distribution.

---



## **Installation**

1. Clone the repository:

```bash
git clone https://github.com/YourUsername/resume-screener.git
cd resume-screener
```

2. Install dependencies:

```bash
pip install streamlit openai pandas python-docx PyPDF2 plotly
```

3. Add your **Gemini API key**:

```python
client = OpenAI(api_key="YOUR_GEMINI_API_KEY")
```

---

## **Usage**

1. Run the Streamlit app:

```bash
streamlit run resume_screener_full.py
```

2. Enter the **job description** in the text area.
3. **Upload candidate resumes** (`.pdf`, `.docx`, or `.txt`).
4. Click **“Evaluate Resumes”**.
5. View the **ranked resumes**, **highlighted skills**, and **download results** as CSV.
6. Explore the **interactive score chart**.

---

## **How It Works**

1. **Resume Parsing:** Extracts text from uploaded PDFs, DOCX, or TXT files.
2. **Keyword Extraction:** Identifies important words from the job description.
3. **Semantic Matching:** Uses Gemini API to compute similarity between resumes and the job description.
4. **Ranking & Highlighting:** Resumes are scored, sorted, and key skills are highlighted.
5. **Visualization & Export:** Scores are visualized in a chart and results can be downloaded as CSV.

---

## **Tech Stack**

| Layer         | Technology          |
| ------------- | ------------------- |
| Frontend      | Streamlit           |
| Backend/AI    | Gemini API, Python  |
| File Handling | PyPDF2, python-docx |
| Data Handling | Pandas              |
| Visualization | Plotly              |

---

## **Future Enhancements**

* Database integration to save resumes and job postings.
* Multi-job support for evaluating candidates across multiple roles.
* Email notifications for shortlisted candidates.
* Authentication & admin dashboard for recruiters.
* Scalable system to handle large volumes of resumes.

---

## **License**

This project is **open-source** and available for personal and educational use.

---



