from unittest import TestCase, skip 
 
import API.endpoints as ep
from flask_restx import Resource, Api
import random
 
import db.data as db
 
def new_entity_name(entity_type):
    int_name = random.randint(0,1000000000)
    return f"new {entity_type}" + str(int_name)
 
class EndpointTestCase(TestCase):
    def setUp(self):
        pass
 
    def tearDown(self):
        pass
 
    def test_hello(self):
        hello = ep.HelloWorld(Resource)
        ret = hello.get()
        self.assertIsInstance(ret, dict)
 
    def test_soup(self):
        """
        Post-condition 1: return is a dictionary.
        """
        lr = ep.OSoup(Resource)
        ret = lr.get()
        self.assertIsInstance(ret, dict)
 
    def test_add_soup(self):
        """
        Post-condition: we can create a soup
        """
        cs = ep.AddSoup(Resource)
        newSoup = new_entity_name("soup")
        #db.add_soup(newSoup)
        cs.post(newSoup)
        soups = db.get_soup()
        #self.assertIn("{soupName: Gumbo}", soups)
        self.assertIn(newSoup, soups)
 
    def test_add_user(self):
        """
        Post-condition: we can create a user
        """
        db.add_user("Bob")
        self.assertIn("Bob",db.get_users())
 
    def test_delete_user(self):
        """
        Post-condition: we can create and delete a user
        """
        db.add_user("Bob")
        ret = ep.DeleteUser(Resource)
        ret.post("Bob")
        self.assertNotIn("Bob", db.get_users())
 
    def test_delete_soup(self):
        """
        Post-condition: we can create and delete a soup
        """
        db.add_soup("Gumbo")
        ret = ep.DeleteSoup(Resource)
        ret.post("Gumbo")
        self.assertNotIn("Gumbo", db.get_soup())