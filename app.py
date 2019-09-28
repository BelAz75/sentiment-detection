from flask import Flask, request
from prediction import SentimentPredictor

app = Flask(__name__)
sentiment_predictor = SentimentPredictor()


@app.route('/text_sentiment', methods=['GET', 'POST'])
def get_sentiment():
    if request.is_json:
        request_dict = request.get_json()
        sentiment = sentiment_predictor.predict(request_dict['text'])
        return sentiment
    else:
        return 'Request doesn\'t contain json with field "text"', 400


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)