from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel


class SentimentPredictor:
    error_result = {'neutral': 1.0}

    def __init__(self):
        self._tokenizer = RegexTokenizer()
        self._model = FastTextSocialNetworkModel(tokenizer=self._tokenizer)

    def predict(self, text):
        try:
            result = self._model.predict([text], k=2)
            if len(result) > 0:
                return result[0]
            else:
                return self.error_result
        except:
            return self.error_result
