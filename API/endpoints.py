""""
This is the file containing all of the endpoints for our flask app.
The endpoint called `endpoints` will return all available endpoints.
"""

from http import HTTPStatus
from flask import Flask
from flask_restx import Resource, Api
import werkzeug.exceptions as wz

import db.data as db

app = Flask(__name__)
api = Api(app)


@api.route('/hello')
class HelloWorld(Resource):
    """
    The purpose of the HelloWorld class is to have a simple test to see if the
    app is working at all.
    """
    def get(self):
        """
        A trivial endpoint to see if the server is running.
        It just answers with "hello world."
        """
        return {'hello': 'world'}


@api.route('/endpoints')
class Endpoints(Resource):
    """
    This class will serve as live, fetchable documentation of what endpoints
    are available in the system.
    """
    def get(self):
        """
        The `get()` method will return a list of available endpoints.
        """
        endpoints = sorted(rule.rule for rule in api.app.url_map.iter_rules())
        return {"Available endpoints": endpoints}


@api.route('/soup')
class OSoup(Resource):
    """
    This class supports fetching a list of all outbound soup.
    """
    def get(self):
        """
        This method returns all outbound soup.
        """
        return db.get_soup()


@api.route('/add_soup/<soupname>')
class AddSoup(Resource): # Supports adding soup 
    def post(self, soupname): # Add soup to soup database
        ret = db.add_soup(soupname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("Soup db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("Soup already added"))
        else:
            return (f"{soupname} added")
            # return db.get_soup
            

@api.route('/delete_soup/<soupname>')
class DeleteSoup(Resource):
    def post(self, soupname):
        # This method deletes a soup from the soup db.
        ret = db.del_soup(soupname)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Soup {soupname} not found."))
        else:
            return f"{soupname} deleted."


            
@api.route('/add_user/<username>')
class AddUser(Resource): # Supports adding soup
    def post(self, username): # Add soup to soup database
        ret = db.add_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound("user db not found."))
        elif ret == db.DUPLICATE:
            raise (wz.NotAcceptable("User already added"))
            

@api.route('/delete_user/<username>')
class DeleteUser(Resource):
    def post(self, username):
        # This method deletes a room from the room db.
        ret = db.del_user(username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"User {username} not found."))
        else:
            return f"{username} deleted."


@api.route('/change_username/<username>')
class ChangeUserName(Resource):
    def post(self, username, new_username):
        
        ret = db.change_user_username(username, new_username)
        if ret == db.NOT_FOUND:
            raise (wz.NotFound(f"Soup {soupname} not found."))
        else:
            return f"{soupname} deleted."
