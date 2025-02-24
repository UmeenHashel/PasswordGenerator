from flask import Flask, jsonify, request
from flask_cors import CORS
import secrets
import string

app = Flask(__name__)
CORS(app)

@app.route('/')
def server():
    return "Server is running!"

@app.route('/generate-password')
def generatePassword():
    length = int(request.args.get('length', 8))
    numbers = request.args.get('numbers', 'false').lower() == 'true'
    symbols = request.args.get('symbols', 'false').lower() == 'true'


    alpahabet = string.ascii_letters
    if numbers == True:
        alpahabet += string.digits
    if symbols == True:
        alpahabet += string.punctuation

    password = "".join(secrets.choice(alpahabet)for i in range(length))
    return jsonify({"Password": password})

if __name__ == "__main__":
    app.run(debug=True)