# import things that I can use html
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

app = Flask(__name__)

@app.get("/")

def home():
    return 'Hello, World!'

@app.get("/bye")
def bye():
    return 'Bye, World!'
