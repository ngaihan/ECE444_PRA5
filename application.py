import requests
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import pickle

application = Flask(__name__)

@application.route("/")
def index():
    return "Your Flask App Works! V1.0"

def load_model():
    with open('basic_classifier.pkl', 'rb') as fid:
        loaded_model = pickle.load(fid)
    with open('count_vectorizer.pkl', 'rb') as vd:
        vectorizer = pickle.load(vd)
    return loaded_model, vectorizer

# model, vectorizer = load_model()

def fetch_article_content(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text
    else:
        return None

# @application.route("/predict", methods=["POST"])
# def predict():
#     data = request.get_json()
#     if 'url' not in data:
#         return jsonify({"error": "No URL provided"}), 400
    
#     url = data['url']
#     article_content = fetch_article_content(url)
#     if article_content is None:
#         return jsonify({"error": "Unable to fetch article content"}), 400
    
#     prediction = model.predict(vectorizer.transform([article_content]))[0]
#     return jsonify({"prediction": prediction})

if __name__ == "__main__":
    application.run(port=5000, debug=True)