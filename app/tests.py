#!environment/bin/python3
from requests import put, get, post

""" GET tasks"""
print(get('http://127.0.0.1:5000/tasks').json())

"""POST task"""
print(post('http://127.0.0.1:5000/tasks', data={'title': 'New task'}).json())

"""GET task/task_id"""
print(get('http://127.0.0.1:5000/tasks/2').json())

"""PUT task/task_id"""
print(put('http://127.0.0.1:5000/tasks/2', data={'title': 'New new task'}).json())

""" GET tasks"""
print(get('http://127.0.0.1:5000/tasks').json())
