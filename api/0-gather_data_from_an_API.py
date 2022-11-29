#!/usr/bin/python3
import requests
from flask import Flask

from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)

url = "http://127.0.0.1:5000/"
response = requests.get(url=url)
print(response.text)

class Helloworld(Resource):

	def __init__(self):

		pass

def get(self):

		return {

			"Hello": "World"

		}

api.add_resource(Helloworld, '/')

if __name__ == '__main__':

	app.run(debug=True)