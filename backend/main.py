from flask import Flask
from flask_peewee.db import SqliteDatabase
from flask_peewee.rest import RestAPI
from flask_admin import Admin
from flask_cors import CORS
from flask_admin.contrib.peewee import ModelView
import peewee

db = SqliteDatabase('app.db')

class Post(db.Model):
    id = peewee.PrimaryKeyField()
    title = peewee.CharField()
    content = peewee.CharField()

class PostAdminView(ModelView):
    pass

app = Flask(__name__)
app.config['SECRET_KEY'] = '123'

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

if (__name__ == '__main__'):
    try:
        Post.create_table()
    except:
        pass

    admin = Admin(app)
    admin.add_view(PostAdminView(Post))

    api = RestAPI(app)
    api.register(Post)
    api.setup()

    app.run(debug=True)
