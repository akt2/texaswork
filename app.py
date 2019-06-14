import os 
from flask import Flask,render_template,jsonify,request,redirect

app=Flask(__name__)

from flask_sqlalchemy import SQLAlchemy
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"
# db=SQLAlchemy(app)

# from .models import Pet

@app.route('/')
def home():
    return 'meow'

if __name__ == '__main__':
    app.run(debug=True)