from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

from .resume_parser import extract_resume_text
from .matcher import calculate_match_score, get_match_level
from .skill_extractor import extract_skills, find_missing_skills


app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

UPLOAD_FOLDER = "../uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


def analyze_resume(resume_path, job_description):
    """
    Analyze a resume against a job description.
    """

    # Extract resume text
    resume_text = extract_resume_text(resume_path)

    # Calculate similarity score
    score = calculate_match_score(
        resume_text,
        job_description
    )

    # Get match level
    match_level = get_match_level(score)

    # Extract skills
    resume_skills = extract_skills(resume_text)
    job_skills = extract_skills(job_description)

    # Find missing skills
    missing_skills = find_missing_skills(
        resume_text,
        job_description
    )

    # Find matched skills
    matched_skills = sorted(
        set(resume_skills) & set(job_skills)
    )

    return {
        "score": score,
        "match_level": match_level,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "resume_skills": resume_skills,
        "job_skills": job_skills,
    }


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():

    # Check if resume was uploaded
    if "resume" not in request.files:
        return "No resume file uploaded."

    resume = request.files["resume"]

    # Check filename
    if resume.filename == "":
        return "Please select a resume file."

    # Get job description
    job_description = request.form.get("job_description", "").strip()

    if not job_description:
        return "Please enter a job description."

    # Secure filename
    filename = secure_filename(resume.filename)

    # Create upload directory if it doesn't exist
    os.makedirs(
        os.path.join(os.path.dirname(__file__), UPLOAD_FOLDER),
        exist_ok=True
    )

    # Save uploaded resume
    resume_path = os.path.join(
        os.path.dirname(__file__),
        UPLOAD_FOLDER,
        filename
    )

    resume.save(resume_path)

    # Analyze resume
    result = analyze_resume(
        resume_path,
        job_description
    )

    return render_template(
        "results.html",
        result=result
    )


if __name__ == "__main__":
    app.run(debug=True)