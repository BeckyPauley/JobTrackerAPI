from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

jobs = []


class Job(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('company', 
        type=str, 
        required=True, 
        help="This field cannot be left blank" 
        ) 
    parser.add_argument('salary')
    parser.add_argument('status')

    def post(self, title):

        if next(filter(lambda x: x['title'] == title, jobs), None) is not None:
            return{'message': "A job with name '{}' already exists".format(title)}, 400 
        data = Job.parser.parse_args() 

        job = {
                'title': title, 
                'company': data['company'], 
                'salary': data['salary'], 
                'status': data['status']
                }
        jobs.append(job)

        return job, 201

    def get(self, title):
        job  = next(filter(lambda x: x['title'] == title, jobs), None) # Returns a filter object, returns None if can;t find object
        return {'job': job}, 200 if job else 404

    def put(self, title):

        data = Job.parser.parse_args()

        job = next(filter(lambda x: x['title'] == title, jobs), None)
        if job is None:
            job = {
                'title': title, 
                'company': data['company'], 
                'salary': data['salary'], 
                'status': data['status']
                }
            jobs.append(job)
        else:
            job.update(data)
        return job

#Remove job (Delete)
    #def delete():
     #   return None

#JobsList
#class job_list(Resource)
#Get jobs (Get)

#Endpoints
api.add_resource(Job, '/job/<string:title>')

app.run(port=5000, debug=True)