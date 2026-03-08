from sklearn.feature_extraction.text import TfidfVectorizer

def apply_tfidf(text_data):

    vectorizer = TfidfVectorizer(
        stop_words="english",
        max_features=12000,
        ngram_range=(1,2),
        min_df=3,
        max_df=0.85,
        sublinear_tf=True
    )

    X = vectorizer.fit_transform(text_data)

    return X, vectorizer