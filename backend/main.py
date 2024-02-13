from flask import Flask
from flask_peewee.db import SqliteDatabase
from flask_peewee.rest import RestAPI
import peewee

db = SqliteDatabase('app.db')

class Post(db.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField()
    content = peewee.CharField()

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'
if (__name__ == '__main__'):
    try:
        Post.create_table()
    except:
        pass

    api = RestAPI(app)
    api.register(Post)
    api.setup()

    app.run(debug=True)
