from flask_restful import Api

from apps.service.demo import DemoResource

api_v1 = Api(prefix='/apis/v1')

api_v1.add_resource(DemoResource, '/demo')
