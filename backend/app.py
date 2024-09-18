from flask import Flask, request, jsonify
from flask_cors import CORS
import price_tracker
import db

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return 'Welcome to the Ticket Notifier API'

@app.route('/register', methods=['POST'])
def register():
    data = request.json
    email = data['email']
    artist = data['artist']
    db.register_user(email, artist)
    return jsonify({'message': 'User registered successfully'})

@app.route('/check-prices', methods=['GET'])
def check_prices():
    price_tracker.check_prices()
    return jsonify({'message': 'Price check completed'})

if __name__ == '__main__':
    app.run(debug=True)
