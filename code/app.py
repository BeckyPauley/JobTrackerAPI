from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

jobs = []

class Job(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument(
        'company',
        type=str,
        required=True,
        help="This field cannot be left blank"
        )
    parser.add_argument('salary')
    parser.add_argument('status')

    def post(self, title):

        if self.check_for_job(title) is not None:
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

    def check_for_job(self, title):
        for job in jobs:
            if job['title'] == title:
                return job
        return None

    def get(self, title):
        job = self.check_for_job(title)
        if job:
            return {'job': job}, 200
        else:
            return{"message": "Job does not exist"}, 404

    def put(self, title):

        data = Job.parser.parse_args()

        job = self.check_for_job(title)
        if job is None:
            job = {
                'title': title,
                'company': data['company'],
                'salary': data['salary'],
                'status': data['status']
                }
            jobs.append(job), 201
        else:
            job.update(data), 200
        return job

    def delete(self, title):
        if self.check_for_job(title) is None:
            return{'message': "A job with name '{}' does not exist".format(title)}, 400
        global jobs
        jobs = list([job for job in jobs if job['title'] != title])
        return {'message': 'Item deleted'}, 200


class JobsList(Resource):

    def get(self):
        return {"jobs": jobs}, 200

api.add_resource(Job, '/job/<string:title>')
api.add_resource(JobsList, '/jobs')

app.run(port=5000, debug=True)