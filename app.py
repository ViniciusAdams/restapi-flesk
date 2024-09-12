from flask import Flask
from flask_restful import Resource, Api
from flask_mongoengine import MongoEngine

app = Flask(__name__)
api = Api(app)
db = MongoEngine(app)

class Users(Resource):
    def get(self):
        return {"message": "user 1"}


class User(Resource):
    def post(self):
        return {"message": "teste"}

    def get(self, cpf):
        return {"message": f"CPF: {cpf}"}


# Corrected route for User resource
api.add_resource(User, '/user', '/user/<string:cpf>')
api.add_resource(Users, '/users')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
