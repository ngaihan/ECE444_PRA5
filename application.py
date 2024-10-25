import requests
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

# @application.route("/", methods=["GET"])
# def index():
#     return "Your Flask App Works! V2.0"


@application.route("/", methods=["GET", "POST"])
def load_model():
    with open("basic_classifier.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    with open("count_vectorizer.pkl", "rb") as vectorizer_file:
        vectorizer = pickle.load(vectorizer_file)
    inputs = [
        "This is fake news",
        "Homeowners who regularly rent on Airbnb and other sites must pay 13% tax on property value when they sell, recent tax ruling finds",
        "More straight couples are calling each other partners. Here's why",
        "The 2020 election was not stolen. Anyone who claims it was is spreading THE BIG LIE",
    ]
    predictions = model.predict(vectorizer.transform(inputs))
    return jsonify({"predictions": predictions.tolist()})


if __name__ == "__main__":
    application.run()
