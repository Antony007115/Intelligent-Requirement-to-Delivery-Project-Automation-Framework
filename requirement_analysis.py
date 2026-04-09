import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def extract_features(text):

    tokens = word_tokenize(text.lower())
    stop_words = set(stopwords.words('english'))

    keywords = [word for word in tokens if word.isalpha() and word not in stop_words]

    return keywords