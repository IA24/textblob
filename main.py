from flask import Flask, render_template, request
from textblob import TextBlob

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        blob = TextBlob(text)
        sentiment = blob.sentiment
        return render_template('./index.html', text=text, sentiment=sentiment)
    return render_template('./index.html')

if __name__ == '__main__':
    app.run(debug=True)
