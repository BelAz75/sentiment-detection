from prediction import SentimentPredictor


sentiment = SentimentPredictor()

test_sentences = [
    'привет', 'красавчик!', 'ну и говнище', 'отлично сказано!', 'вам самим не смешно?'
]

print(test_sentences)

for comment in test_sentences:
    print('{} : {}'.format(comment, sentiment.predict(comment)))
