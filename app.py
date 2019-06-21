import os 
from flask import Flask,render_template,jsonify,request,redirect
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

for x in bob:
    print(x)

df = pandas.read_sql('SELECT * FROM may', engine)
print(df)

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/data')
def data():
    return jsonify(df.to_json(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)