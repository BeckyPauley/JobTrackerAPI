from flask import Flask
from flask_restful import Api

from job import Job 
from jobslist import JobsList

app = Flask(__name__)

api = Api(app)

api.add_resource(Job, '/job/<string:title>')
api.add_resource(JobsList, '/jobs')

app.run(port=5000, debug=True)