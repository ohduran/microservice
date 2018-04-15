#!environment/bin/python3
from flask import g
from flask_httpauth import HTTPBasicAuth


users = {'alvaro': 'duran'}
auth = HTTPBasicAuth()


@auth.verify_password
def verify_password(username, password):
    try:
        stored_password = users[username]
        if password == stored_password:
            g.user = username
            return True
        return False
    except KeyError:
        return False
