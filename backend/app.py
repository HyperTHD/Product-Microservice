import json
from bson.objectid import ObjectId
from flask import Flask, Response, request
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


@app.route('/products', methods=['GET'])
def get_products():
    db = get_db()
    _products = list(db.Product.find())
    for product in _products:
        product["_id"] = str(product["_id"])
    return Response(
        response=json.dumps(
            _products
        ),
        status=200,
        mimetype='application/json'
    )


@app.route('/products/<id>', methods=['GET'])
def get_products(id):
    db = get_db()
    product = db.Product.find_one({"_id": ObjectId(id)})
    return Response(
        response=json.dumps(
            product
        ),
        status=200,
        mimetype='application/json'
    )


@app.route('/products', methods=['POST'])
def create_product():
    db = get_db()
    product = {
        'name': request.form['name'],
        'quantity': request.form['quantity'],
        'price': request.form['price'],
    }
    response = db.Product.insert_one(product)
    print(response.inserted_id)
    return Response(
        response=json.dumps(
            {"Message": "Product created successfully",
             "id": f"{response.inserted_id}"}
        ),
        status=201,
        mimetype="application/json"
    )


@app.route('/products/<id>', methods=['DELETE'])
def delete_product(id):
    db = get_db()
    response = db.Product.delete_one({"_id": ObjectId(id)})
    return Response(
        response=json.dumps(
            {"Message": "Product deleted successfully", "id": f"{id}"}),
        status=204,
        mimetype="application/json"
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
