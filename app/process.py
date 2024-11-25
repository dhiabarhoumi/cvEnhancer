import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer

def preprocess_text(text):
    """
    Preprocesses text by converting to lowercase and removing special characters.
    
    Args:
        text (str): The input text to preprocess.
        
    Returns:
        str: Cleaned text.
    """
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)  # Remove special characters
    text = re.sub(r"\s+", " ", text).strip()  # Remove extra spaces
    return text


def extract_keywords(text, top_n=20):
    """
    Extracts top N keywords from the given text using TF-IDF.

    Args:
        text (str): The input text to analyze.
        top_n (int): The number of top keywords to extract.

    Returns:
        list: A list of keywords.
    """
    vectorizer = TfidfVectorizer(stop_words="english", max_features=top_n)
    tfidf_matrix = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out()


def compare_keywords(cv_text, job_text):
    """
    Compares keywords from the CV and the job description.

    Args:
        cv_text (str): Text extracted from the CV.
        job_text (str): Text extracted from the job description.

    Returns:
        dict: A dictionary containing:
            - `cv_keywords`: Keywords from the CV.
            - `job_keywords`: Keywords from the job description.
            - `missing_keywords`: Keywords in the job description but not in the CV.
    """
    # Preprocess both texts
    cv_text_clean = preprocess_text(cv_text)
    job_text_clean = preprocess_text(job_text)

    # Extract keywords
    cv_keywords = extract_keywords(cv_text_clean)
    job_keywords = extract_keywords(job_text_clean)

    # Find missing keywords
    missing_keywords = set(job_keywords) - set(cv_keywords)

    return {
        "cv_keywords": list(cv_keywords),
        "job_keywords": list(job_keywords),
        "missing_keywords": list(missing_keywords),
    }


def create_enhancement_suggestions(missing_keywords):
    """
    Creates enhancement suggestions based on missing keywords.

    Args:
        missing_keywords (list): List of missing keywords.

    Returns:
        str: Suggestions for improving the CV.
    """
    if not missing_keywords:
        return "Your CV is well-aligned with the job description. No major enhancements needed."

    suggestions = "Consider incorporating the following keywords into your CV:\n"
    for keyword in missing_keywords:
        suggestions += f"- {keyword}\n"
    return suggestions
