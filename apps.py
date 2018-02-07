from flask import Flask, request, abort
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
        username = request.form['username']
        password = request.form['password']
        if username is None or password is None:
            abort(400)  # missing arguments
        if User.query.filter_by(username=username).first() is not None:
            abort(400)  # existing user
        user = User(username=username, password=password)
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
