from flask import Flask, request
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
    specialSymbols = request.args.get('specialSymbols')

    length = int(length)
    numbers = bool(numbers)
    specialSymbols = bool(specialSymbols)

    alpahabet = string.ascii_letters
    if numbers == True:
        alpahabet += string.digits
    if specialSymbols == True:
        alpahabet += string.punctuation
    password = "".join(secrets.choice(alpahabet)for i in range(length))
    return password

if __name__ == "__main__":
    app.run(debug=True)