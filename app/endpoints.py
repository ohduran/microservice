from flask import request
from flask_restful import Resource
from flask.ext.restful import reqparse

from app import app, api

tasks = {}


class UserAPI(Resource):
    """User endpoint."""

    def get(self, id):
        """Get method."""
        pass

    def put(self, id):
        """Put method."""
        pass

    def delete(self, id):
        """Delete method."""
        pass


class TaskListAPI(Resource):
    """All tasks endpoint."""

    def __init__(self):
        """Constructor: Handle Arguments."""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description',
                                   type=str, default="", location='json')
        super(TaskListAPI, self).__init__()

    def get_tasks(self):
        """Get ALL tasks method."""
        pass


class TaskAPI(Resource):
    """Particular task endpoint."""

    def __init__(self):
        """Constructor: Handle Arguments."""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, task_id):
        """Get task by task_id method."""
        task = [t for t in tasks if t['task_id'] == task_id]
        return {'task': task}

    def put(self, task_id):
        """Update a task by task_id method."""
        task = filter(lambda t: t['task_id' == task_id], tasks)
        args = self.reqparse.parse_args(strict=True)
        for key, value in args.iteritems():
            if value is not None:
                task[key] = value
        return {'task': task}


api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api.add_resource(TaskListAPI, '/tasks', endpoint='all_tasks')
api.add_resource(TaskAPI, '/tasks/<int:task_id>', endpoint='task')


if __name__ == '__main__':
    app.run(debug=True)
