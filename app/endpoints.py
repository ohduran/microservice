#!environment/bin/python3
from flask import request, jsonify
from flask_restful import Resource, abort, reqparse
from flask_login import current_user, login_user
from app import app, api, auth

users = {
    'alvaro': 'duran',
    'admin': 'sudo',
}
tasks = {
     1: {
        'task_id': 1,
        'title': u'Build an API',
        'description': "",
        'done': False,
        },
     2: {
        'task_id': 2,
        'title': u'Meeting with friends',
        'description': "Pub around the corner",
        'done': False,
        },
}


class UserAPI(Resource):
    """User endpoint."""

    def __init__(self):
        """Constructor: Handle Arguments."""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('username', type=str,  required=True,
                                   help='No username provided',
                                   location='json')
        self.reqparse.add_argument('password', type=str,  required=True,
                                   help='No password provided',
                                   location='json')
        super(UserAPI, self).__init__()

    @auth.get_password
    def get(self,):
        """Get method."""
        args = self.reqparse.parse_args()
        username = args['username']
        if username in users:
            return users.get(username)
        return None

    def put(self, id):
        """Authenticate."""
        pass

    def post(self, id):
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
        self.reqparse.add_argument('title', type=str,  required=True,
                                   help='No task title provided',
                                   location='json')
        self.reqparse.add_argument('description', location='json',
                                   type=str, default="")
        self.reqparse.add_argument('done', type=bool, default=False,
                                   location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        """Get ALL tasks method."""
        return jsonify(tasks)

    def post(self):
        """Post a new task method."""
        args = self.reqparse.parse_args()
        task_id = int(max(tasks.keys())) + 1
        task = {key: args[key] for key in args.keys()}
        tasks[task_id] = task
        return jsonify({'task': tasks[task_id]})


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
        task = tasks[task_id]
        return jsonify({'task': task})

    def put(self, task_id):
        """Update a task by task_id method."""
        task = tasks[task_id]
        args = self.reqparse.parse_args()
        for key in args.keys():
            if args[key] is not None:
                task[key] = args[key]
        tasks[task_id] = task
        return jsonify({'task': task})

    def delete(self, task_id):
        """Delete a task with task_id method."""
        del tasks[task_id]
        return jsonify("")


api.add_resource(UserAPI, '/users', endpoint='user')
api.add_resource(TaskListAPI, '/tasks', endpoint='all_tasks')
api.add_resource(TaskAPI, '/tasks/<int:task_id>', endpoint='task')


if __name__ == '__main__':
    app.run(debug=True)
