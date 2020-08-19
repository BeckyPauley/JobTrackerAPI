from flask_restful import Resource, reqparse

jobs = {}

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

        if jobs.get(title):
           return{'message': f"A job with name '{title}' already exists"}, 400

        data = Job.parser.parse_args()

        jobs.update(
            {title : {
                'company': data['company'],
                'salary': data['salary'],
                'status': data['status']
                }
            }
        )
        return jobs[title], 201

    def get(self, title):
        if jobs.get(title):
            return jobs[title], 200
        else:
            return{"message": f"A job with neme {title} does not exist"}, 404

    def put(self, title):

        data = Job.parser.parse_args()

        if jobs.get(title):
            jobs[title].update(data), 200
            return jobs[title]
        else:
            return self.post(title)

    def delete(self, title):
        if jobs.get(title) == None:
            return {'message': f"A job with name '{title}' does not exist"}, 400
        jobs.pop(title)
        return {'message' : f"{title} deleted"}, 200
