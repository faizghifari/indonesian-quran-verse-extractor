import flask
import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for
from app.lib.word_similarity import WordSimilarityClassifier
from app.lib.preprocess import IndoTextCleaner, StopWordsEliminator
from app.lib.dict import load_dict

app = Flask(__name__)

target_dict, quran_dict = load_dict()

vectorizer = pickle.load(open('pkl/vectorizer.pkl', 'rb'))
svm = pickle.load(open('pkl/svm.pkl', 'rb'))
wordsim = pickle.load(open('pkl/wordsim.pkl', 'rb'))

id_quran = pd.read_csv('../quran/Indonesian.csv')
ar_quran = pd.read_csv('../quran/Arabic.csv')
en_quran = pd.read_csv('../quran/English.csv')

text_cleaner = IndoTextCleaner()
sw_elim = StopWordsEliminator()

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

        input_text = input_text.apply(lambda x: text_cleaner.transform(x))
        input_text = input_text.apply(lambda x: sw_elim.transform(x))

        results = np.array(svm.predict(vectorizer.transform(input_text)))

        answers = []
        verse_results = []

        for result in results:
            idx = 0
            for label in result:
                if label == 1:
                    for name, key in target_dict.items():
                        if key == idx:
                            answers.append(name)
                idx = idx + 1

        for answer in answers:
            temp = quran_dict[answer]
            verse_results.append(temp)
        
        id_results = []
        ar_results = []
        en_results = []
        count_ayah = []

        for i in range(0,len(verse_results)):
            id_temp = []
            ar_temp = []
            en_temp = []
            for verse in verse_results[i]:
                count_ayah.append(len(verse_results[i]))
                surah = verse.split('|')[0]
                ayah = verse.split('|')[1]
                for id_text in id_quran['surah|ayah|text']:
                    if id_text.find(verse) != -1:
                        txt_temp = id_text.split('|')[-1]
                        id_temp.append(txt_temp)
                        break
                for ar_text in ar_quran['surah|ayah|text']:
                    if ar_text.find(verse) != -1:
                        txt_temp = ar_text.split('|')[-1]
                        ar_temp.append(txt_temp)
                        break
                for en_text in en_quran[['Surah','Ayah','Text']].values:
                    if ((en_text[0] == int(surah)) and (en_text[1] == int(ayah))):
                        en_temp.append(en_text[2])
                        break
            id_results.append(id_temp)
            ar_results.append(ar_temp)
            en_results.append(en_temp)

        ans_length = len(answers)

        return render_template('results.html', input_text=input_text, answers=answers,
                                verse_results=verse_results, id_results=results, 
                                ar_results=ar_results, en_results=en_results, 
                                count_ayah=count_ayah, len=ans_length)
    else:
        return redirect(url_for('error'))

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(port=5000, debug=True)

