#!environment/bin/python3
from requests import put, get, post, delete

"""Authenticate first."""
start_get = get('http://127.0.0.1:5000/users', data=dict(username='alvaro')).json()
print(start_get)


""" GET tasks"""
start_get = get('http://127.0.0.1:5000/tasks').json()
print(start_get)

"""POST task"""
print(post('http://127.0.0.1:5000/tasks', data=dict(title='New task')).json())

"""GET task/task_id"""
print(get('http://127.0.0.1:5000/tasks/2').json())

"""PUT task/task_id"""
print(put('http://127.0.0.1:5000/tasks/2',
          data=dict(title='New new task')).json())

""" GET tasks"""
print(get('http://127.0.0.1:5000/tasks').json())

# DELETE tasks
print(delete('http://127.0.0.1:5000/tasks/3').json())

""" GET tasks"""
print(get('http://127.0.0.1:5000/tasks').json())

"""PUT task/task_id"""
print(put('http://127.0.0.1:5000/tasks/2',
          data=dict(title='Meeting with friends')).json())

""" GET tasks"""
end_get = get('http://127.0.0.1:5000/tasks').json()
print(end_get)

if start_get == end_get:
    print("Get at start matches Get at end")
else:
    print("Check initial and final state.")
