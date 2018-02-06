from flask_restful import Resource

from apps import db
from apps.models.user import User


class UserApi(Resource):
    def get(self, user_id=None):
        if user_id:
            return {"user_id": user_id}
        else:
            return {"user_list": "all user"}

    def post(self):
        user = User(username="admin", password="123456")
        db.session.add(user)
        db.session.commit()
        return {"username": user.username}

    def delete(self, user_id):
        return {"user_id": user_id, "is_delete": 1}
