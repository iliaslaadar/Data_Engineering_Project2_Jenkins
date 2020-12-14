#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from  nltk.stem import SnowballStemmer
import gensim
from gensim.similarities import WmdSimilarity
import time


def import_data(data):
    df = pd.read_csv(data, index_col=0)
    df = pd.DataFrame(df['text'])
    df = df.drop_duplicates()
    df = df.reset_index().drop(columns=['index'])
    return df


data = "tweets.csv"
df = import_data(data)
df.head()


def preprocess(text, stem=False):
    TEXT_CLEANING_RE = "@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+"
    text = re.sub(TEXT_CLEANING_RE, ' ', str(text).lower()).strip()
    stop_words = stopwords.words("english")
    stemmer = SnowballStemmer("english")
    tokens = []
    for token in text.split():
        if token not in stop_words:
            if stem:
                tokens.append(stemmer.stem(token))
            else:
                tokens.append(token)
    return " ".join(tokens)


def split_doc(df_clean):
    documents = [text.split() for text in df_clean]
    return documents


def model(documents):
    w2v_model = gensim.models.word2vec.Word2Vec(size=300, window=7, min_count=10, workers=8)
    w2v_model.build_vocab(documents)
    w2v_model.train(documents, total_examples=len(documents), epochs=35)
    return w2v_model


def similarity(df_clean, w2v_model):
    instance = WmdSimilarity(df_clean, w2v_model, num_best=20)
    return instance


def top_tweets(nb_top, text):
    df_clean = df.text.apply(lambda x: preprocess(x))
    documents = split_doc(df_clean)
    w2v_model = model(documents)
    instance = similarity(df_clean, w2v_model)
    clean_text = preprocess(text)
    similarities = instance[clean_text]
    
    rows, cols = (nb_top, 2) 
    results = [[0 for i in range(cols)] for j in range(rows)]

    print('Your text:')
    print(text)
    for i in range(nb_top):
        print('\n\nsimilarities = %.4f' % similarities[i][1])
        print(df.text[similarities[i][0]])
        results[i][0] = df.text[similarities[i][0]]
        results[i][1] = similarities[i][1]
        
    return results
        
        