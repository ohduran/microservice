#!environment/bin/python3
import unittest
from random import choices
from string import ascii_uppercase

from requests import put, get, post, delete
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("alvaro", "python")


class UnitTestCase(unittest.TestCase):
    """
    Test the behaviour of the application and its relationship
    with the database.
    """

    def setUp(self):
        """Set up."""
        pass

    def tearDown(self):
        """Tear Down."""
        pass

    def test_Get_Tasks(self):
        """Get tasks."""
        r = get('http://127.0.0.1:5000/tasks', auth=auth)

        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), dict)

    def test_post_task(self):
        """Post a new task."""
        new_task = {
                'title': 'newest task',
                'description': 'Description of the task',
        }
        r = post('http://127.0.0.1:5000/tasks', data=new_task, auth=auth)
        task_result = r.json()['task']
        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(r.json(), dict)
        for key in new_task.keys():
                self.assertTrue(new_task[key] == task_result[key])

    def test_get_a_task(self):
        """Get a task by task_id."""
        r_all = get('http://127.0.0.1:5000/tasks', auth=auth).json()
        expected_task = r_all['1']

        r = get('http://127.0.0.1:5000/tasks/1', auth=auth)
        task_result = r.json()['task']

        self.assertEqual(r.status_code, 200)
        self.assertIsInstance(task_result, dict)

        self.assertEqual(task_result, expected_task)

        for key in expected_task.keys():
                self.assertTrue(expected_task[key] == task_result[key])

    def test_put_a_task(self):
            """Update a task by task_id."""
            r_task = get('http://127.0.0.1:5000/tasks/1', auth=auth)
            before_task = r_task.json()['task']

            after_task = {
                    'title':  ''.join(choices(ascii_uppercase, k=10)),
                    'description': ''.join(choices(ascii_uppercase, k=10)),
            }

            r = put('http://127.0.0.1:5000/tasks/1', data=after_task, auth=auth)
            task_result = r.json()['task']

            self.assertEqual(r.status_code, 200)
            self.assertIsInstance(task_result, dict)

            for key in after_task.keys():
                    self.assertNotEqual(before_task[key], task_result[key])
                    self.assertEqual(after_task[key], task_result[key])

    def test_delete_a_task(self):
            """Delete a task by task_id."""
            r_all_before = get('http://127.0.0.1:5000/tasks', auth=auth).json()
            keys_before = sorted([int(key) for key in r_all_before])

            r = delete('http://127.0.0.1:5000/tasks/' + str(keys_before[-1]), auth=auth)

            self.assertEqual(r.status_code, 200)
            self.assertEqual(r.json(), "")

            r_all_after = get('http://127.0.0.1:5000/tasks', auth=auth).json()
            keys_after = sorted([int(key) for key in r_all_after])

            self.assertEqual(len(keys_after), len(keys_before) - 1)

            keys_after.append(keys_before[-1])
            self.assertListEqual(keys_after, keys_before)

    def test_mark_a_task_as_done(self):
            """Mark a task by task_id as done."""
            r_get_before = get('http://127.0.0.1:5000/tasks/1', auth=auth)
            task_result_before = r_get_before.json()['task']

            self.assertFalse(task_result_before['done'])

            r = put('http://127.0.0.1:5000/markasdone/1',
                    data=dict(done=True), auth=auth)
            self.assertEqual(r.status_code, 200)
            self.assertIsInstance(r.json(), dict)

            r_get_after = get('http://127.0.0.1:5000/tasks/1', auth=auth)
            task_result_after = r_get_after.json()['task']

            self.assertTrue(task_result_after['done'])



if __name__ == '__main__':
    unittest.main()
