import datetime
from .db import db

class Product(db.Document):
    name = db.StringField(required=True, unique=True)
    quantity = db.IntField(required=True, unique=True, default=0)
    price = db.FloatField(required=True, unique=True, default=0.0)
    date = db.DateTimeField(default=datetime.datetime.utcnow)
