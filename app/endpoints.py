from app import app
from flask import jsonify, abort, make_response, request

tasks = [
    {
        'id': 1,
        'title': u'Buy train tickets',
        'description': u'From London to Oxford tomorrow at 10am.',
        'done': False,
    },
    {
        'id': 2,
        'title': u'Buy a present for my partner',
        'description': u'Maybe a book on programming?',
        'done': False,
    },
    ]


@app.errorhandler(404)
def not_found(error):
    """404 Error Handling."""
    return make_response(jsonify({'error': 'Not found'}), 404)


# @app.route('/login')
# def login():
#     """Login endpoint."""
#     form = LoginForm()
#     return form


@app.route('/tasks', methods=['GET'])
def get_tasks():
    """Get all tasks for the user."""
    return jsonify(
        {'tasks': tasks}
    )


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_a_task(task_id):
    """Get a task by task id."""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
        return jsonify(
            {'task': task[0]}
        )


@app.route('/tasks', method=['POST'])
def post_task():
    """Post a task for the user."""
    if not request.json or 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False,
    }

    tasks.append(task)
    return jsonify({'task': task}), 201


def mark_as_complete(task_id):
    """Mark a task with id = task_id as done."""
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if not request.json:
        abort(400)
    task[0]['done'] = True
    return jsonify({'task': task[0]})
