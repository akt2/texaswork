import MySQLdb

print('Connecting to database using MySQLdb')

dbconn=MySQLdb.connect(host='us-cdbr-iron-east-02.cleardb.net',
                        db='heroku_6e5a2e6badc386d',
                        user='bb0b038b59569a',
                        passwd='33c9d7ce')

print('Successfully connected')
dbconn.close()