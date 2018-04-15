#!environment/bin/python3
from flask import jsonify
from flask_restful import Resource, reqparse

from app import app, api, auth

users = {'alvaro': 'python'}

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


@auth.verify_password
def verify_password(username, password):
        """Password verification for HTTP Basic Auth protocol."""
        try:
                stored_password = users[username]
                if password == stored_password:
                                return True
                return False
        except KeyError:
                return False


class TaskListAPI(Resource):
    """All tasks endpoint."""

    def __init__(self):
        """Constructor: Handle Arguments."""
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('title', type=str,  required=True,
                                   help='No task title provided')
        self.reqparse.add_argument('description',
                                   type=str, default="")
        self.reqparse.add_argument('done', type=bool, default=False)
        super(TaskListAPI, self).__init__()

    @auth.login_required
    def get(self):
        """Get ALL tasks method."""
        return jsonify(tasks)

    @auth.login_required
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
        self.reqparse.add_argument('title', type=str)
        self.reqparse.add_argument('description', type=str)
        self.reqparse.add_argument('done', type=bool, default=False)
        super(TaskAPI, self).__init__()

    @auth.login_required
    def get(self, task_id):
        """Get task by task_id method."""
        task = tasks[task_id]
        return jsonify({'task': task})

    @auth.login_required
    def put(self, task_id):
        """Update a task by task_id method."""
        task = tasks[task_id]
        args = self.reqparse.parse_args()
        for key in args.keys():
            if args[key] is not None:
                task[key] = args[key]
        tasks[task_id] = task
        return jsonify({'task': task})

    @auth.login_required
    def delete(self, task_id):
        """Delete a task with task_id method."""
        del tasks[task_id]
        return jsonify("")


class MarkTaskAsDoneAPI(TaskAPI):
        """Mark a task as Done endpoint."""

        def __init__(self):
                """Constructor: Handle Arguments."""
                self.reqparse = reqparse.RequestParser()
                self.reqparse.add_argument('done', type=bool)
                super(MarkTaskAsDoneAPI, self).__init__()


api.add_resource(TaskListAPI, '/tasks', endpoint='all_tasks')
api.add_resource(TaskAPI, '/tasks/<int:task_id>', endpoint='task')
api.add_resource(TaskAPI, '/markasdone/<int:task_id>', endpoint='markasdone')


if __name__ == '__main__':
    app.run(debug=False)
