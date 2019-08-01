import os 
from flask import Flask,render_template,jsonify,request,redirect,send_file
import pymysql
import sqlalchemy
import flask_sqlalchemy
import pandas

# Thank you, Cam! source for the following code up to app=Flask(_name_): https://github.com/CamKirk/nanda/blob/master/app.py

if not os.environ.get('DYNO'):
    import config
    # print(config.name)

if os.environ.get('CLEARDB_DATABASE_URL'):
    dburl = os.environ['CLEARDB_DATABASE_URL']
else:
    dburl = config.dburl



engine = sqlalchemy.create_engine(dburl)
bob=engine.execute('SELECT * FROM may LIMIT 5')

# for x in bob:
#     print(x)

df = pandas.read_sql('SELECT * FROM may', engine)
print(df)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/tableau')
def tableau():
    return render_template('tableau.html')

@app.route('/models')
def models():
    return render_template('models.html')

# @app.route('/data')
# def data():
#     return render_template('data.html')
    # jsonify(df.to_json(orient='records'))

# @app.route('/csv')
# def upload_file():
#    return send_file('DataSet/bob.csv')

# @app.route('/stat')
# def stat():
#     return render_template('stat.html')

if __name__ == '__main__':
    app.run(debug=True)