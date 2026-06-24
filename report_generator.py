from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    role,
    score,
    skills,
    missing_skills,
    roadmap
):

    pdf_file = "career_report.pdf"

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "AI Career Navigator Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"<b>Recommended Role:</b> {role}",
            styles["BodyText"]
        )
    )

    content.append(
        Paragraph(
            f"<b>Resume Score:</b> {score}/100",
            styles["BodyText"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Detected Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Missing Skills</b>",
            styles["Heading2"]
        )
    )

    for skill in missing_skills:

        content.append(
            Paragraph(
                f"• {skill}",
                styles["BodyText"]
            )
        )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            "<b>Learning Roadmap</b>",
            styles["Heading2"]
        )
    )

    for i, step in enumerate(
        roadmap,
        start=1
    ):

        content.append(
            Paragraph(
                f"Month {i}: {step}",
                styles["BodyText"]
            )
        )

    doc.build(content)

    return pdf_file