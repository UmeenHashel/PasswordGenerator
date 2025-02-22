from flask import Flask, jsonify, request
import secrets
import string

app = Flask(__name__)

@app.route('/')
def server():
    return "Server is running!"

@app.route('/generate-password')
def generatePassword():
    length = request.args.get('length')
    numbers = request.args.get('numbers')
    symbols = request.args.get('symbols')

    length = int(length)
    numbers = numbers.lower() == 'true'
    symbols = symbols.lower() == 'true'

    alpahabet = string.ascii_letters
    if numbers == True:
        alpahabet += string.digits
    if symbols == True:
        alpahabet += string.punctuation

    password = "".join(secrets.choice(alpahabet)for i in range(length))
    return jsonify({"Password": password})

if __name__ == "__main__":
    app.run(debug=True)