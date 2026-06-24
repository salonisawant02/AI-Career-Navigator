skills_list = [
    "python",
    "sql",
    "excel",
    "power bi",
    "tableau",
    "machine learning",
    "deep learning",
    "statistics",
    "pandas",
    "numpy",
    "data analysis",
    "data science",
    "streamlit"
]

def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in skills_list:

        if skill in text:
            found_skills.append(skill)

    return found_skills