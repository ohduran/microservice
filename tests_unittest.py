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




if __name__ == '__main__':
    unittest.main()
