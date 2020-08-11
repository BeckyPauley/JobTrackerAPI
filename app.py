from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)

api = Api(app)


#Job
class Job(Resource):
    #Add job (Post)
    def add_job():
        return None

#Get job (Get)
    def get_job_details():
        return None

#Edit job (Put)
    def update_job():
        return None

#Remove job (Delete)
    def delete_job():
        return None

#JobsList
#class job_list(Resource)
#Get jobs (Get)

#Endpoints
