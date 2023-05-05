"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-chaagre7avj5o48t9lq0-a.oregon-postgres.render.com",
        database="todo_10ny",
        user="root",
        password="9Mr2PUc59lrBZvEFTalI8ND9z5m4cqs3")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
