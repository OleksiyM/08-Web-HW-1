from bson import json_util
from mongoengine import connect, Document, StringField, ListField, ReferenceField, CASCADE

import os

from dotenv import load_dotenv

load_dotenv()

DB_USER = os.getenv('DB_USER')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_HOST = os.getenv('DB_HOST')


URI = f'mongodb+srv://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/?retryWrites=true&w=majority'


# uri = "mongodb+srv://<username>:<password>@cluster0.vhirvg8.mongodb.net/?retryWrites=true&w=majority"

connect(db='Web-HW-8-1', host=URI)


class Author(Document):
    fullname = StringField(required=True, unique=True)
    born_date = StringField()
    born_location = StringField()
    description = StringField()
    meta = {"collection": "authors"}


class Quote(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    quote = StringField(required=True)
    tags = ListField(StringField(max_length=35))
    meta = {"collection": "quotes"}

