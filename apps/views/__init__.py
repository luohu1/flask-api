from flask_restful import Api

from apps.views.users import UserApi
from apps.views.tokens import TokenApi

api = Api()

api.add_resource(
    UserApi,
    '/users',
    '/users/<string:user_id>'
)
api.add_resource(TokenApi, '/tokens')
