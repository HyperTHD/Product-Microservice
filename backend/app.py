from flask import Flask, jsonify, request, Response, redirect, url_for
from pymongo import MongoClient

app = Flask(__name__)


def get_db():
    client = MongoClient(
        host='test_mongodb',
        port=27017,
        username='root',
        password='pass',
        authSource="admin"
    )
    db = client["Product"]
    return db


@app.route('/')
def ping_server():
    return "This route should work if MongoDB connects"


@app.route('/products')
def get_products():
    db = get_db()
    _products = db.Product.find()
    products = [{"id": product["id"], "name": product["name"]}
                for product in _products]
    return jsonify({"products": products})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
