from flask_restful import Resource


class TokenApi(Resource):
    def get(self):
        return "token_id"
