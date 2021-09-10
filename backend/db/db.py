import os
from flask_mongoengine import MongoEngine
from mongoengine import connect
from dotenv import load_dotenv

db = MongoEngine()

def initialize_db(app):
    db.init_app(app)
    
    load_dotenv('../', '.env')

    connect(host=os.environ.get('MONGO_URI'))
