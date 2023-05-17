"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chi7sul269vf5qbbb64g-a.oregon-postgres.render.com",
        database="todo_pm43",
        user="root",
        password="pz2QayluWmM4jvaFlG0Zl2kLa4jeHIrQ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
