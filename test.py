from src.main import analyze_resume


job_description = """
We are looking for a Machine Learning Engineer.

Required skills:
Python
Pandas
NumPy
Scikit-learn
Machine Learning
Flask
SQL
Docker
AWS
Git
GitHub
"""

import os

resume_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    "uploads",
    "test_resume.docx"
)

result = analyze_resume(
    resume_path,
    job_description
)


print("\n========== RESUME ANALYSIS ==========")

print(f"\nMatch Score: {result['score']}%")

print(f"Match Level: {result['match_level']}")

print("\nMatched Skills:")
for skill in result["matched_skills"]:
    print(f"  ✓ {skill}")

print("\nMissing Skills:")
for skill in result["missing_skills"]:
    print(f"  ✗ {skill}")

print("\n======================================")