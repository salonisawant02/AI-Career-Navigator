role_requirements = {

    "Data Analyst": [
        "python",
        "sql",
        "excel",
        "power bi",
        "statistics"
    ],

    "Data Scientist": [
        "python",
        "machine learning",
        "statistics",
        "sql",
        "pandas"
    ],

    "Business Analyst": [
        "excel",
        "power bi",
        "sql"
    ],

    "Machine Learning Engineer": [
        "python",
        "machine learning",
        "deep learning",
        "numpy"
    ]
}

def analyze_skill_gap(role, skills):

    required_skills = role_requirements.get(role, [])

    missing_skills = []

    matched_skills = []

    for skill in required_skills:

        if skill in skills:
            matched_skills.append(skill)
        else:
            missing_skills.append(skill)

    if len(required_skills) > 0:
        score = int(
            (len(matched_skills) / len(required_skills)) * 100
        )
    else:
        score = 0

    return score, missing_skills