# Lluís P
# 3CD1
# Sesión 5 Laboratorio LNR

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import gensim.downloader as api
import nltk

nltk.download('punkt')
corpus_df = pd.read_csv('Consp-vs-Critical.csv', delimiter='\t')
stop_words = set(stopwords.words('english'))
w2v_model = api.load("word2vec-google-news-300")
fasttext_model = api.load("fasttext-wiki-news-subwords-300")
glove_model = api.load("glove-wiki-gigaword-300")

def get_avg_vector(text, model):
    tokens = word_tokenize(text.lower())
    tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    vector = np.zeros_like(model.get_vector("word"))
    count = 0
    for token in tokens:
        try:
            vector += model.get_vector(token)
            count += 1
        except KeyError:
            pass  
    if count != 0:
        vector /= count  
    return vector

for class_label in ['CONSPIRACY', 'CRITICAL']:
    class_documents = corpus_df[corpus_df['label'] == class_label]['text']
    for i, document in enumerate(class_documents):
        w2v_vector = get_avg_vector(document, w2v_model)
        fasttext_vector = get_avg_vector(document, fasttext_model)
        glove_vector = get_avg_vector(document, glove_model)
        similarity_w2v = []
        similarity_fasttext = []
        similarity_glove = []
        for j, other_document in enumerate(class_documents):
            if i != j:  
                similarity_w2v.append((j, cosine_similarity([w2v_vector], 
                            [get_avg_vector(other_document, w2v_model)])[0][0]))
                similarity_fasttext.append((j, cosine_similarity([fasttext_vector],
                             [get_avg_vector(other_document, fasttext_model)])[0][0]))
                similarity_glove.append((j, cosine_similarity([glove_vector],
                          [get_avg_vector(other_document, glove_model)])[0][0]))
        most_similar_w2v = max(similarity_w2v, key=lambda x: x[1])
        most_similar_fasttext = max(similarity_fasttext, key=lambda x: x[1])
        most_similar_glove = max(similarity_glove, key=lambda x: x[1])

        print(f"Document {i+1}, class {class_label}:")
        print("Most similar document using Word2Vec:", most_similar_w2v)
        print("Most similar document using FastText:", most_similar_fasttext)
        print("Most similar document using GloVe:", most_similar_glove)
