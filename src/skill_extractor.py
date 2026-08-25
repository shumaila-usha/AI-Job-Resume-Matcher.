import re


SKILLS = [
    "Python",
    "Java",
    "C++",
    "JavaScript",
    "HTML",
    "CSS",
    "SQL",
    "MySQL",
    "PostgreSQL",
    "MongoDB",
    "Flask",
    "Django",
    "FastAPI",
    "Streamlit",
    "Pandas",
    "NumPy",
    "Scikit-learn",
    "TensorFlow",
    "PyTorch",
    "Machine Learning",
    "Deep Learning",
    "Natural Language Processing",
    "NLP",
    "Computer Vision",
    "OpenCV",
    "Generative AI",
    "Artificial Intelligence",
    "Data Science",
    "Data Analysis",
    "Git",
    "GitHub",
    "Docker",
    "AWS",
    "Azure",
    "Google Cloud",
    "Power BI",
    "Tableau",
    "Excel",
]


def extract_skills(text):
    """
    Extract known technical skills from text.
    """

    text_lower = text.lower()

    found_skills = []

    for skill in SKILLS:
        pattern = r"\b" + re.escape(skill.lower()) + r"\b"

        if re.search(pattern, text_lower):
            found_skills.append(skill)

    return sorted(found_skills)


def find_missing_skills(resume_text, job_description):
    """
    Find skills required by the job but missing from the resume.
    """

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    missing_skills = job_skills - resume_skills

    return sorted(missing_skills)