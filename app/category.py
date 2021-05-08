from flask import make_response, abort
from config import db
from models import Category
from serializer import CategorySchema

def read():
    category = Category.query.first()
    
    category_schema = CategorySchema()
    data = category_schema.dump(category)
    return data