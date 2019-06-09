#!flask/bin/python
from flask import Flask, jsonify, request, abort, render_template
from translate import translate_word

app = Flask(__name__)

@app.route('/api/v1/translate', methods=['POST'])
def translater():
    if not request.json or not 'word' in request.json:
        abort(400)
    word = request.json.get('word')
    translated = " ".join(translate_word(word) for word in word.split())
    return jsonify({'word': translated}), 201

@app.route('/')
def index():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
