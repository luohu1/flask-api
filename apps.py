from flask import Flask
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
    SQLALCHEMY_DATABASE_URI='sqlite:///data/sqlite.db'
)
db = SQLAlchemy(app)
api = Api(app)


# models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))

    def __repr__(self):
        return '<User %r>' % self.username


# views
class UserApi(Resource):
    def get(self, user_id=None):
        pass

    def post(self):
        user = User(username="admin", password="123456")
        db.session.add(user)
        db.session.commit()
        return {"username": user.username}

    def delete(self, user_id):
        pass


api.add_resource(
    UserApi,
    '/users',
    '/users/<string:user_id>'
)

if __name__ == '__main__':
    app.run()
