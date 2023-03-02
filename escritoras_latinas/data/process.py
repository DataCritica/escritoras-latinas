"""
Natural Language Processing
"""
# NLTK
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
# Gensim
import gensim
from gensim.utils import simple_preprocess


# Define stopwords in Spanish
stopwords = stopwords.words('spanish')
stopwords.append(['sido', 'mujer', 'mujeres'])

# Function to tokenize into words, lowercase and de-accent
def sent_to_words(sentences):
    for sentence in sentences:
        yield(gensim.utils.simple_preprocess(str(sentence), deacc=False))

# Fuction to remove defined stop words
def remove_stopwords(texts):
    return [[word for word in simple_preprocess(str(doc))
         if word not in stopwords] for doc in texts]
