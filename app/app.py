import flask
import pickle
import numpy as np
import pandas as pd

from flask import Flask, render_template, request, redirect, url_for, session
from sklearn.metrics.pairwise import cosine_similarity
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from app.lib.word_similarity import WordSimilarityClassifier
from app.lib.preprocess import IndoTextCleaner, StopWordsEliminator
from app.lib.dict import load_dict

app = Flask(__name__)
app.secret_key = "quran-search"
target_dict, old_dict, surah_dict = load_dict()

# vectorizer = pickle.load(open('pkl/vectorizer.pkl', 'rb'))
# old_vectorizer = pickle.load(open('pkl/old_vectorizer.pkl', 'rb'))
tfidf_vectorizer = pickle.load(open("pkl/tfidf_vectorizer.pkl", "rb"))
tfidf_verse_matrix = pickle.load(open("pkl/tfidf_verse_matrix.pkl", "rb"))

# tree = pickle.load(open('pkl/tree.pkl', 'rb'))
# old_tree = pickle.load(open('pkl/old_tree.pkl', 'rb'))

id_quran = pd.read_csv("../quran/Indonesian_clean.csv")
ar_quran = pd.read_csv("../quran/Arabic.csv")
en_quran = pd.read_csv("../quran/English.csv")

text_cleaner = IndoTextCleaner()
sw_elim = StopWordsEliminator()
stemmer = StemmerFactory().create_stemmer()


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/main", methods=["POST", "GET"])
def main():
    if request.method == "POST":
        form = request.form
        session["username"] = form["username"]

    return render_template("main.html")


@app.route("/results", methods=["POST", "GET"])
def results():
    if request.method == "POST":
        form = request.form
        input_text = pd.Series([form["input-text"]])
        amount_ayah = int(form["amount-ayah"])
        # method = form['optradio']
        method = "doc-ir"
        threshold = 0.1

        input_text = input_text.apply(lambda x: text_cleaner.transform(x))
        input_text = input_text.apply(lambda x: sw_elim.transform(x))
        input_text = input_text.apply(lambda x: stemmer.stem(x))

        raw_answers = []
        answers = []
        answers_txt = ""
        # if (method == 'multilabel-new'):
        #     results = np.array(tree.predict(vectorizer.transform(input_text)))

        #     for result in results:
        #         idx = 0
        #         for label in result:
        #             if label == 1:
        #                 for name, key in target_dict.items():
        #                     if key == idx:
        #                         answers.append(name)
        #             idx = idx + 1

        #     answers_txt = ' '.join(answers)
        #     raw_answers = answers
        #     answers = pd.Series([answers_txt])
        # elif (method == 'multilabel-old'):
        #     results = np.array(old_tree.predict(old_vectorizer.transform(input_text)))

        #     for result in results:
        #         idx = 0
        #         for label in result:
        #             if label == 1:
        #                 for name, key in old_dict.items():
        #                     if key == idx:
        #                         answers.append(name)
        #             idx = idx + 1

        #     answers_txt = ' '.join(answers)
        #     raw_answers = answers
        #     answers = pd.Series([answers_txt])
        # else:

        answers_txt = input_text.values[0]
        answers = pd.Series([answers_txt])

        answers = answers.apply(lambda x: text_cleaner.transform(x))
        answers = answers.apply(lambda x: sw_elim.transform(x))
        answers = answers.apply(lambda x: stemmer.stem(x))

        answers_vector = tfidf_vectorizer.transform(answers)

        res_unsorted = cosine_similarity(answers_vector, tfidf_verse_matrix)

        res_sorted = sorted(
            range(len(res_unsorted[0])), key=lambda k: res_unsorted[0][k], reverse=True
        )

        similarity_score = []
        verse_results = []

        session["method"] = method
        session["input_text"] = input_text.values[0]
        session["raw_answers"] = raw_answers
        session["amount_ayah"] = amount_ayah

        for i in range(0, amount_ayah):
            ar_txt = ar_quran.loc[res_sorted[i], :]["surah|ayah|text"].split("|")[-1]
            en_txt = en_quran.loc[res_sorted[i], :]["Text"]
            id_txt = id_quran.loc[res_sorted[i], :]["text"]

            surah_idx = id_quran.loc[res_sorted[i], :]["surah"]
            surah_name = surah_dict.get(str(surah_idx))

            ayah_idx = id_quran.loc[res_sorted[i], :]["ayah"]

            if res_unsorted[0][res_sorted[i]] > threshold:
                similarity_score.append(res_unsorted[0][res_sorted[i]])
                verse_results.append(
                    [surah_idx, surah_name, ayah_idx, ar_txt, en_txt, id_txt]
                )

        amount_ayah = len(verse_results)
        return render_template(
            "results.html",
            input_text=input_text,
            answers=answers,
            answers_txt=answers_txt,
            method=method,
            amount_ayah=amount_ayah,
            verse_results=verse_results,
            similarity_score=similarity_score,
            raw_answers=raw_answers,
            answers_len=len(raw_answers),
        )
    else:
        return redirect(url_for("error"))


@app.route("/error")
def error():
    return render_template("error.html")


if __name__ == "__main__":
    app.run(port=5000, debug=True)
