# import re
# import nltk
# from nltk.corpus import stopwords

# nltk.download("stopwords")

# stop_words = set(stopwords.words("english"))

# def clean_text(text):
#     text = str(text).lower()
#     text = re.sub(r'[^a-z\s]', ' ', text)
#     words = text.split()
#     words = [word for word in words if word not in stop_words]
#     return " ".join(words)

import re
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words("english"))

def clean_text(text):

    text = text.lower()

    # remove emails
    text = re.sub(r'\S+@\S+', ' ', text)

    # remove phone numbers
    text = re.sub(r'\b\d{10}\b', ' ', text)

    # remove punctuation
    text = re.sub(r'[^a-zA-Z\s]', ' ', text)

    # remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    words = text.split()

    words = [w for w in words if w not in stop_words and len(w) > 2]

    return " ".join(words)