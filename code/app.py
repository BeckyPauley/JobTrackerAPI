from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)

api = Api(app)

jobs = []

#Job
class Job(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('company', 
        type=str, 
        required=True, 
        help="This field cannot be left blank" 
        ) 
    parser.add_argument('salary')
    parser.add_argument('status')

    #Add job (Post)
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

#Get job (Get)

    #    return None

#Edit job (Put)
    #def put():
     #   return None

#Remove job (Delete)
    #def delete():
     #   return None

#JobsList
#class job_list(Resource)
#Get jobs (Get)

#Endpoints
api.add_resource(Job, '/job/<string:title>')

app.run(port=5000, debug=True)