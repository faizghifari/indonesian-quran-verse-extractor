import flask
import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from app.lib.word_similarity import WordSimilarityClassifier
from app.lib.preprocess import IndoTextCleaner, StopWordsEliminator
from app.lib.dict import load_dict

app = Flask(__name__)

target_dict, quran_dict, surah_dict = load_dict()

vectorizer = pickle.load(open('pkl/vectorizer.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open('pkl/tfidf_vectorizer.pkl', 'rb'))
tfidf_verse_matrix = pickle.load(open('pkl/tfidf_verse_matrix.pkl', 'rb'))

tree = pickle.load(open('pkl/tree.pkl', 'rb'))
wordsim = pickle.load(open('pkl/wordsim.pkl', 'rb'))

id_quran = pd.read_csv('../quran/Indonesian_clean.csv')
ar_quran = pd.read_csv('../quran/Arabic.csv')
en_quran = pd.read_csv('../quran/English.csv')

text_cleaner = IndoTextCleaner()
sw_elim = StopWordsEliminator()
stemmer = StemmerFactory().create_stemmer()

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        form = request.form
        input_text = pd.Series([form['input-text']])
        amount_ayah = int(form['amount-ayah'])
        method = form['optradio']

        input_text = input_text.apply(lambda x: text_cleaner.transform(x))
        input_text = input_text.apply(lambda x: sw_elim.transform(x))
        input_text = input_text.apply(lambda x: stemmer.stem(x))

        # print(input_text)
        # print(method)

        answers = []
        answers_txt = ''

        if (method == 'multilabel'):
            results = np.array(tree.predict(vectorizer.transform(input_text)))

            for result in results:
                idx = 0
                for label in result:
                    if label == 1:
                        for name, key in target_dict.items():
                            if key == idx:
                                answers.append(name)
                    idx = idx + 1

            # for answer in answers:
            #     temp = quran_dict[answer]
            #     verse_results.append(temp)

            answers_txt = ' '.join(answers)

            answers = pd.Series([answers_txt])
        else:
            answers_txt = str(input_text)

            answers = pd.Series([answers_txt])
        
        answers = answers.apply(lambda x: text_cleaner.transform(x))
        answers = answers.apply(lambda x: sw_elim.transform(x))
        answers = answers.apply(lambda x: stemmer.stem(x))

        answers_vector = tfidf_vectorizer.transform(answers)

        res_unsorted = cosine_similarity(answers_vector, tfidf_verse_matrix)

        res_sorted = sorted(range(len(res_unsorted[0])), key=lambda k: res_unsorted[0][k], reverse = True)

        # print(res_unsorted[0][3876])

        similarity_score = []
        verse_results = []

        for i in range(0, amount_ayah):
            ar_txt = ar_quran.loc[ res_sorted[i], : ]['surah|ayah|text'].split('|')[-1]
            en_txt = en_quran.loc[ res_sorted[i], : ]['Text']
            id_txt = id_quran.loc[ res_sorted[i] , : ]['text']

            surah_idx = id_quran.loc[ res_sorted[i] , : ]['surah']
            surah_name = surah_dict.get(str(surah_idx))

            ayah_idx = id_quran.loc[ res_sorted[i] , : ]['ayah']

            similarity_score.append(res_unsorted[0][res_sorted[i]])

            verse_results.append([surah_idx, surah_name, ayah_idx, ar_txt, en_txt, id_txt])
        
        # count_ayah = []

        # for i in range(0,len(verse_results)):
        #     id_temp = []
        #     ar_temp = []
        #     en_temp = []
        #     count_ayah.append(len(verse_results[i]))
        #     for verse in verse_results[i]:
        #         surah = verse.split('|')[0]
        #         ayah = verse.split('|')[1]
        #         for id_text in id_quran['surah|ayah|text']:
        #             if id_text.find(verse) != -1:
        #                 txt_temp = id_text.split('|')[-1]
        #                 id_temp.append(txt_temp)
        #                 break
        #         for ar_text in ar_quran['surah|ayah|text']:
        #             if ar_text.find(verse) != -1:
        #                 txt_temp = ar_text.split('|')[-1]
        #                 ar_temp.append(txt_temp)
        #                 break
        #         for en_text in en_quran[['Surah','Ayah','Text']].values:
        #             if ((en_text[0] == int(surah)) and (en_text[1] == int(ayah))):
        #                 en_temp.append(en_text[2])
        #                 break
        #     id_results.append(id_temp)
        #     ar_results.append(ar_temp)
        #     en_results.append(en_temp)

        # ans_length = len(answers)

        return render_template('results.html', input_text=input_text, answers=answers, answers_txt=answers_txt, method=method,
                                               amount_ayah=amount_ayah, verse_results=verse_results, similarity_score=similarity_score)
    else:
        return redirect(url_for('error'))

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

