from flask_restful import Resource

import job

class JobsList(Resource):

    def get(self):
        return {"jobs": job.jobs}, 200