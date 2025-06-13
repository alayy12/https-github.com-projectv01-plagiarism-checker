
from flask import Flask, request, jsonify
from difflib import SequenceMatcher

app = Flask(__name__)

def calculate_similarity(text1, text2):
    return round(SequenceMatcher(None, text1, text2).ratio() * 100, 2)

@app.route("/check", methods=["POST"])
def check_plagiarism():
    data = request.get_json()
    text1 = data.get("text1", "")
    text2 = data.get("text2", "")
    similarity = calculate_similarity(text1, text2)
    return jsonify({"similarity_percent": similarity})

if __name__ == "__main__":
    app.run(debug=True)
        