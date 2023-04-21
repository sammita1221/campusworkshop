"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch13b7jh4hstbhh8r62g-a.oregon-postgres.render.com",
        database="todo_kee1",
        user="todo_kee1_user",
        password="IiPeH9rBnZ5r97NClXCApD8asUwonFEx")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
