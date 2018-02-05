from flask_restful import Resource


class UserApi(Resource):
    def get(self, user_id=None):
        if user_id:
            return {"user_id": user_id}
        else:
            return {"user_list": "all user"}

    def post(self):
        return "create user"

    def delete(self, user_id):
        return {"user_id": user_id, "is_delete": 1}
