from sklearn.feature_extraction.text import TfidfVectorizer

def apply_tfidf(text_data):

    vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=10000,
    ngram_range=(1,2),
    min_df=2,
    max_df=0.9
)

    X = vectorizer.fit_transform(text_data)

    return X, vectorizer