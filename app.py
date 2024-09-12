from flask import Flask, render_template, jsonify, request
import random
import string

app = Flask(__name__)

# Password generator logic
def generate_password(length=12, include_special_chars=True):
    characters = string.ascii_letters + string.digits
    if include_special_chars:
        characters += string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-password')
def generate_password():
    length = int(request.args.get('length', 12))
    include_abc = request.args.get('abc', 'false').lower() == 'true'
    include_123 = request.args.get('123', 'false').lower() == 'true'
    include_special = request.args.get('special', 'false').lower() == 'true'

    # Character sets
    characters = ''
    if include_abc:
        characters += string.ascii_letters  # ABC includes uppercase and lowercase letters
    if include_123:
        characters += string.digits  # 123 includes digits
    if include_special:
        characters += '!@#%'  # Special characters

    if not characters:
        characters = string.ascii_letters  # Default to letters if no option is selected

    password = ''.join(random.choice(characters) for _ in range(length))

    return jsonify({'password': password})