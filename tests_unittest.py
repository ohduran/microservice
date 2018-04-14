#!environment/bin/python3
import unittest
import os

from requests import put, get, post, delete
from config import basedir
from app import app, db
from app.models import User, Task


class UnitTestCase(unittest.TestCase):
    """
    Test the behaviour of the application and its relationship
    with the database.
    """

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

    def test_Get_Tasks(self):
        """Get tasks."""
        r = get('http://127.0.0.1:5000/tasks')

        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), dict)

    def test_post_task(self):
        """Post a new task."""
        new_task = {
                'title': 'New task',
                'description': 'Description of the task',
                'done': False,
        }
        r = post('http://127.0.0.1:5000/tasks', data=new_task)
        #print(r.json())
        task_result = r.json()['task']
        print(task_result)
        print(new_task)
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), dict)
        self.assertTrue(task_result == new_task)






if __name__ == '__main__':
    unittest.main()
