from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def extract_skill_words(text):
    text = text.lower()

    # keep words only
    words = re.findall(r"[a-zA-Z]+", text)

    # remove very short words
    words = [w for w in words if len(w) > 3]

    return " ".join(words)


def calculate_similarity_score(jd_text, resume_text):

    jd_keywords = extract_skill_words(jd_text)
    resume_keywords = extract_skill_words(resume_text)

    documents = [jd_keywords, resume_keywords]

    vectorizer = TfidfVectorizer(stop_words="english")

    tfidf_matrix = vectorizer.fit_transform(documents)

    score = cosine_similarity(
        tfidf_matrix[0:1],
        tfidf_matrix[1:2]
    )[0][0]

    return round(score * 100, 2)