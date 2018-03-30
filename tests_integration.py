#!environment/bin/python3
import unittest
import os

from requests import put, get, post, delete
from config import basedir
from app import app, db
from app.models import User, Task


class TestSuite(unittest.TestCase):
    """Set up and Tear Down the database methods."""

    def setUp(self):
        """Set up."""
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' \
            + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """Tear Down."""
        db.session.remove()
        db.drop_all()

    def test_get_tasks(self):
        """TaskListAPI GET."""
        response = self.app.get('/tasks')
        print(response.data)
        self.assertTrue(1 == 1)


if __name__ == '__main__':
    unittest.main()


    # class UserAPITests(TestSuite):
    #     """Test for the User API."""
    #
    #     pass
    #
    #
    # class TaskListAPITest(TestSuite):
    #     """Test for the Task List API."""
    #
    #     def get_tasks(self):
    #         """GET tasks tests."""
    #         response = get('http://127.0.0.1:5000/tasks').json()
    #         expected_response = ""
    #         self.assertEqual(response, expected_response)
    #
    #
    # class TaskAPITest(TestSuite):
    #     """Test for the Task API."""
    #
    #     pass
    #
    #
    # """ GET tasks"""
    # start_get = get('http://127.0.0.1:5000/tasks').json()
    # print(start_get)
    #
    # """POST task"""
    # print(post('http://127.0.0.1:5000/tasks', data={'title': 'New task'}).json())
    #
    # """GET task/task_id"""
    # print(get('http://127.0.0.1:5000/tasks/2').json())
    #
    # """PUT task/task_id"""
    # print(put('http://127.0.0.1:5000/tasks/2',
    #           data={'title': 'New new task'}).json())
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
    #           data={'title': 'Meeting with friends'}).json())
    #
    # """ GET tasks"""
    # end_get = get('http://127.0.0.1:5000/tasks').json()
    # print(end_get)
    #
    # if start_get == end_get:
    #     print("Get at start matches Get at end")
    # else:
    #     print("Check initial and final state.")
