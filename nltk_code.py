

import nltk
#nltk.download('punkt')
from nltk.stem.snowball import SnowballStemmer
import numpy as np
import spacy

stemmer = SnowballStemmer("french")
nlp = spacy.load('fr_core_news_sm')

def tokenize(phrase):

    return  nltk.word_tokenize(phrase.lower(), language='french')

def stem(mot):
    # return stemmer.stem(mot.lower())
    #installer fr_core_news_sm : python -m spacy download fr_core_news_sm
    #lemmatisation
    doc = nlp(mot)
    mot_lemmatiser = [token.lemma_ for token in doc]
    return mot_lemmatiser[0] if mot_lemmatiser else mot.lower()

def sac_de_mot(phrase_token,tous_mot):

    mot_phrase = [stem(mot) for mot in phrase_token]

    sac = np.zeros(len(tous_mot), dtype=np.float32)

    for idx, w in enumerate(tous_mot):
        if w in mot_phrase: 
            sac[idx] = 1

    return sac
