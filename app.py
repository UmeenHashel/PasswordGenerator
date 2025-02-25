from flask import Flask, jsonify, request
from flask_cors import CORS
import secrets
import string

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to the Password Generator Backend!"

@app.route('/generate-password')
def generatePassword():
    length = int(request.args.get('length', 8))
    numbers = request.args.get('numbers', 'false').lower() == 'true'
    symbols = request.args.get('symbols', 'false').lower() == 'true'
    uppercase = request.args.get('uppercase', 'true').lower() == 'true'
    lowercase = request.args.get('lowercase', 'true').lower() == 'true'
    similar = request.args.get('similar', 'false').lower() == 'true'

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation

    alpahabet = ''
    if lowercase:
        alpahabet += string.ascii_lowercase
    if uppercase:
        alpahabet += string.ascii_uppercase
    if numbers:
        alpahabet += string.digits
    if symbols:
        alpahabet += string.punctuation

    if similar:
        similar_characters = 'il1Lo0O'
        alphabet = ''.join([char for char in alphabet if char not in similar_characters])

    if not alpahabet:
        return jsonify({"error": "You must select at least one character type"}) , 400

    password = "".join(secrets.choice(alpahabet)for i in range(length))
    return jsonify({"Password": password})

if __name__ == "__main__":
    app.run(debug=True)