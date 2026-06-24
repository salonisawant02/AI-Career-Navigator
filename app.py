import streamlit as st
import pandas as pd
import plotly.express as px

from resume_parser import extract_text
from skill_extractor import extract_skills
from skill_gap_analyzer import analyze_skill_gap
from roadmap_generator import generate_roadmap
from report_generator import generate_report
from ml_role_predictor import predict_role_ml

from database import (
    create_database,
    save_analysis,
    get_analysis_history
)

# Create Database
create_database()

# Page Configuration
st.set_page_config(
    page_title="AI Career Navigator",
    page_icon="🚀",
    layout="wide"
)

# Title
st.title("🚀 AI Career Navigator & Resume Analyzer")

st.write(
    "Upload your resume and get career recommendations, skill analysis, resume score and learning roadmap."
)

# Temporary User
username = "guest"

# Upload Resume
uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:

    # Extract Resume Text
    resume_text = extract_text(uploaded_file)

    # Extract Skills
    skills = extract_skills(resume_text)

    # ML Role Prediction
    predicted_role = predict_role_ml(skills)

    # Skill Gap Analysis
    score, missing_skills = analyze_skill_gap(
        predicted_role,
        skills
    )

    # Learning Roadmap
    roadmap = generate_roadmap(
        predicted_role,
        missing_skills
    )

    # Save Analysis
    save_analysis(
        username,
        predicted_role,
        score,
        skills
    )

    # Resume Content
    st.subheader("📄 Resume Content")

    st.text_area(
        "Extracted Text",
        resume_text,
        height=250
    )

    # Skills
    st.subheader("🛠 Detected Skills")

    if skills:

        cols = st.columns(3)

        for index, skill in enumerate(skills):

            with cols[index % 3]:
                st.success(
                    skill.title()
                )

    else:

        st.warning(
            "No skills detected."
        )

    # Role Prediction
    st.subheader("🎯 Recommended Career Role")

    st.success(
        predicted_role
    )

    # Resume Score
    st.subheader("📊 Resume Score")

    st.metric(
        label="Score",
        value=f"{score}/100"
    )

    # Missing Skills
    st.subheader("⚠ Missing Skills")

    if missing_skills:

        for skill in missing_skills:

            st.error(
                skill.title()
            )

    else:

        st.success(
            "No missing skills found!"
        )

    # Dashboard
    st.subheader(
        "📈 Skills Analysis Dashboard"
    )

    matched_count = max(
        len(skills) - len(missing_skills),
        0
    )

    chart_data = pd.DataFrame({

        "Category": [
            "Matched Skills",
            "Missing Skills"
        ],

        "Count": [
            matched_count,
            len(missing_skills)
        ]
    })

    fig = px.pie(
        chart_data,
        values="Count",
        names="Category",
        title="Skill Match Analysis"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # Learning Roadmap
    st.subheader(
        "🗺 Learning Roadmap"
    )

    if roadmap:

        for month, step in enumerate(
            roadmap,
            start=1
        ):

            st.info(
                f"Month {month}: {step}"
            )

    else:

        st.success(
            "You already possess all required skills!"
        )

    # PDF Download
    st.subheader(
        "📄 Download Report"
    )

    pdf_file = generate_report(
        predicted_role,
        score,
        skills,
        missing_skills,
        roadmap
    )

    with open(
        pdf_file,
        "rb"
    ) as file:

        st.download_button(
            label="⬇ Download PDF Report",
            data=file,
            file_name="Career_Report.pdf",
            mime="application/pdf"
        )

# Analysis History

st.subheader(
    "🗄 Analysis History"
)

history = get_analysis_history(
    username
)

if history:

    history_df = pd.DataFrame(

        history,

        columns=[
            "ID",
            "Username",
            "Role",
            "Score",
            "Skills"
        ]
    )

    st.dataframe(
        history_df,
        use_container_width=True
    )

else:

    st.info(
        "No analysis history available."
    )