from flask import Flask, send_from_directory
from flask_restful import Resource, Api
import os
app = Flask(__name__)

api = Api(app)

@app.route('/')
def hello():
	return "Hello World! Mk2"

class Listing(Resource):
    def get(self):
        return {"endpoints":[]}
api.add_resource(Listing, '/listing')

@app.route('/demo_site/<path:path>')
def send_bootstrap(path):
    return send_from_directory('bootstrap', path)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)