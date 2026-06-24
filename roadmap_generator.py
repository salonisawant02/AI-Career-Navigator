def generate_roadmap(role, missing_skills):

    roadmap = []

    for skill in missing_skills:

        if skill == "python":
            roadmap.append(
                "Learn Python Fundamentals and Data Structures"
            )

        elif skill == "sql":
            roadmap.append(
                "Learn SQL Queries and Database Concepts"
            )

        elif skill == "excel":
            roadmap.append(
                "Learn Advanced Excel and Pivot Tables"
            )

        elif skill == "power bi":
            roadmap.append(
                "Learn Power BI Dashboard Development"
            )

        elif skill == "statistics":
            roadmap.append(
                "Learn Statistics for Data Science"
            )

        elif skill == "machine learning":
            roadmap.append(
                "Learn Machine Learning Algorithms"
            )

        elif skill == "deep learning":
            roadmap.append(
                "Learn Deep Learning and Neural Networks"
            )

        elif skill == "numpy":
            roadmap.append(
                "Learn NumPy for Numerical Computing"
            )

        elif skill == "pandas":
            roadmap.append(
                "Learn Pandas for Data Analysis"
            )

    return roadmap