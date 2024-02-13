from flask import Flask
from flask_peewee.db import SqliteDatabase
import peewee

db = SqliteDatabase('app.db')

class Post(db.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField()
    content = peewee.CharField()

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
if (__name__ == '__main__'):

    app.run(debug=True)
