from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def calculate_match_score(resume_text, job_description):
    """
    Calculate the similarity between a resume and a job description.
    """

    if not resume_text.strip() or not job_description.strip():
        return 0.0

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer(
        stop_words="english",
        lowercase=True
    )

    tfidf_matrix = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    score = similarity * 100

    return round(score, 2)


def get_match_level(score):
    """Return a simple interpretation of the match score."""

    if score >= 80:
        return "Excellent Match"
    elif score >= 65:
        return "Good Match"
    elif score >= 50:
        return "Moderate Match"
    else:
        return "Low Match"