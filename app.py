from flask import Flask, request, render_template
from pickle import load
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from  nltk.stem import SnowballStemmer
nltk.download('stopwords')

instance = load(open('instance3.pkl', 'rb'))

app = Flask(__name__, template_folder='templates')

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

def top_tweets(nb_top, text, df):
    clean_text = preprocess(text)
    similarities = instance[clean_text]

    rows, cols = (nb_top, 2)
    results = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(nb_top):
        results[i][0] = df.text[similarities[i][0]]
        results[i][1] = similarities[i][1]
    
    return results
        
def import_data(data):
    df = pd.read_csv(data, index_col=0)
    df = pd.DataFrame(df['text'])
    df = df.drop_duplicates()
    df = df.reset_index().drop(columns=['index'])
    return df

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')

    if request.method == 'POST':

        df = import_data('tweets.csv')

        text = request.form['text']

        results = top_tweets(20, text, df)

        return render_template('index.html', text = text, prediction = results)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
