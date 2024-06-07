from flask import request, jsonify
from config import words_probability, app 


@app.route("/", methods=['GET'])
def home():
    return jsonify({
        "message": "Server is Running"
    }), 200

@app.route("/spell-check/<string:check_word>", methods=["GET"])
def spell_check(check_word):
    def delete(word):
        probable_words = []
        n = len(word)
        for i in range(0, n, 1):
            probable_words.append(word[0: i] + word[i+1:])
        return probable_words
    
    def swap(word):
        probable_words = []
        n = len(word)
        word = list(word)
        for i in range(1, n, 1):
            word[i], word[i-1] = word[i-1], word[i]
            probable_words.append("".join(word))
            word[i], word[i-1] = word[i-1], word[i]
        return probable_words
    
    def insert(word):
        probable_words = []
        n = len(word)
        word = list(word)
        for i in range(0, n+1, 1):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                probable_words.append("".join(word[0:i]) + ch + "".join(word[i:]))
        return probable_words
    
    def replace(word):
        probable_words = []
        n = len(word)
        word = list(word)
        for i in range(0, n, 1):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                probable_words.append("".join(word[0:i]) + ch + "".join(word[i+1:]))
        return probable_words
    
    def spell_check(word):
        probable_words = replace(word) + insert(word) + delete(word) + swap(word)
        output = []
        for word in probable_words:
            if word in words_probability.keys():
                output.append([word, words_probability[word]])
        output.sort(key=lambda x: x[1], reverse=True)
        return output
    
    output = spell_check(check_word)
    
    return jsonify({
        'success': True,
        'output': output
    }), 200

if __name__ == "__main__":
    app.run(debug = True)
    