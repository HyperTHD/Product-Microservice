db = db.getSiblingDB("Product");
db.products.drop();

db.products.insertMany([
    { 
        "id": 1,
        "name": "Bananas",
        "quantity": 10
    }
]);