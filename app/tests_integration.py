#!environment/bin/python3
from requests import put, get, post, delete


proxies = {"http": "http://alvaro:python"}

r = get('http://127.0.0.1:5000/tasks', proxies=proxies)
print(r.json())
# """ GET tasks"""
# start_get = get('http://127.0.0.1:5000/tasks', auth=('alvaro', 'python')).json()
# print("GET TASKS -", start_get)

# """POST task"""
# print('TASK 3 - ', post('http://127.0.0.1:5000/tasks', data=dict(title='New task')).json())
#
# """GET task/task_id"""
# print("GET task 2", get('http://127.0.0.1:5000/tasks/2').json())
#
# """PUT task/task_id"""
# print('PUT task 2', put('http://127.0.0.1:5000/tasks/2',
#                         data=dict(title='New new task')).json())
#
# """ GET tasks"""
# print(get('http://127.0.0.1:5000/tasks').json())
#
# # DELETE tasks
# print(delete('http://127.0.0.1:5000/tasks/3').json())
#
# """ GET tasks"""
# print(get('http://127.0.0.1:5000/tasks').json())
#
# """PUT task/task_id"""
# print(put('http://127.0.0.1:5000/tasks/2',
#           data=dict(title='Meeting with friends')).json())
#
# """ GET tasks"""
# end_get = get('http://127.0.0.1:5000/tasks').json()
# print(end_get)
#
# if start_get == end_get:
#     print("Get at start matches Get at end")
# else:
#     print("Check initial and final state.")
#
# """Mark task/task_id as DONE"""
# #print(put('http://127.0.0.1:5000/markasdone/2').json())
# print('Mark as done', put('http://127.0.0.1:5000/markasdone/2',
#           data=dict(done=True)).json())
