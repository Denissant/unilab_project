from flask import Flask, redirect
from flask_restful import Api
from flask_jwt import JWT
from security import authentication, identity
from resources.user import RegisterUser
from resources.freelancers import Item, ItemList


app = Flask(__name__)
app.secret_key = 'secret'

app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"


api = Api(app)
jwt = JWT(app, authentication, identity)


@app.route('/')
def home():
    return redirect('https://github.com/Denissant/unilab_project/tree/main'), 302

api.add_resource(ItemList, "/items/")
api.add_resource(Item, "/items/<string:link_id>")
api.add_resource(RegisterUser, "/registration")

if __name__ == '__main__':
    from db import db
    db.init_app(app)

    app.run(port=54321, debug=True)
