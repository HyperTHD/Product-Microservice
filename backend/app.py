import os
from flask import Flask, jsonify, request, Response
from db.db import initialize_db
from db.models import Product
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv('../', '.env')

app.config['MONGODB_URI'] = os.getenv('MONGO_URI')

initialize_db(app)

@app.route('/', methods=['GET'])
def getProducts():
    return "This route should work if MongoDB connects"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')