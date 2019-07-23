from flask_restful import Api

from apps.service.demo import DemoResource
from apps.service.user import UserResource

api_v1 = Api(prefix='/apis/v1')

api_v1.add_resource(DemoResource, '/demo')
api_v1.add_resource(UserResource, '/users')
