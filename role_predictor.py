def predict_role(skills):

    skills = [skill.lower() for skill in skills]

    # Data Scientist

    if (
        "python" in skills and
        "machine learning" in skills and
        "statistics" in skills
    ):
        return "Data Scientist"

    # Data Analyst

    elif (
        "python" in skills and
        "sql" in skills and
        "excel" in skills
    ):
        return "Data Analyst"

    # Business Analyst

    elif (
        "excel" in skills and
        "power bi" in skills
    ):
        return "Business Analyst"

    # ML Engineer

    elif (
        "python" in skills and
        "deep learning" in skills
    ):
        return "Machine Learning Engineer"

    else:
        return "General IT Professional"