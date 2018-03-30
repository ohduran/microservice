#!environment/bin/python3
from requests import put, get, post, delete
import unittest

class TestSuite(unittest.TestCase):
    """Set up and Tear Down the database methods."""

    def setUp(self):
        """Set up."""
        pass

    def tearDown(self):
        """Tear Down."""
        pass


class UserAPITests(TestSuite):
    """Test for the User API."""

    pass


class TaskListAPITest(TestSuite):
    """Test for the Task List API."""

    def get_tasks(self):
        """GET tasks tests."""
        response = get('http://127.0.0.1:5000/tasks').json()
        expected_response = ""
        self.assertEqual(response, expected_response)


class TaskAPITest(TestSuite):
    """Test for the Task API."""

    pass


""" GET tasks"""
start_get = get('http://127.0.0.1:5000/tasks').json()
print(start_get)

"""POST task"""
print(post('http://127.0.0.1:5000/tasks', data={'title': 'New task'}).json())

"""GET task/task_id"""
print(get('http://127.0.0.1:5000/tasks/2').json())

"""PUT task/task_id"""
print(put('http://127.0.0.1:5000/tasks/2',
          data={'title': 'New new task'}).json())

""" GET tasks"""
print(get('http://127.0.0.1:5000/tasks').json())

# DELETE tasks
print(delete('http://127.0.0.1:5000/tasks/3').json())

""" GET tasks"""
print(get('http://127.0.0.1:5000/tasks').json())

"""PUT task/task_id"""
print(put('http://127.0.0.1:5000/tasks/2',
          data={'title': 'Meeting with friends'}).json())

""" GET tasks"""
end_get = get('http://127.0.0.1:5000/tasks').json()
print(end_get)

if start_get == end_get:
    print("Get at start matches Get at end")
else:
    print("Check initial and final state.")
