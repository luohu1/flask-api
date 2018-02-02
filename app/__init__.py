from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Task(Resource):
    def get(self):
        return "get tasks"

    def post(self):
        return "create one task"

    def put(self):
        return "update one task"

    def delete(self):
        return "delete one task"


api.add_resource(Task, '/tasks')
