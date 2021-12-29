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
 
    def test_add_soup1(self):
        """
        Post-condition: we can create a soup
        """
        cs = ep.AddSoup(Resource)
        newSoup = new_entity_name("soup")
        cs.post(newSoup)
        soups = db.get_soup()
        self.assertIn(newSoup, soups)
        
    def test_add_soup2(self):
        """
        Post-condition 2: we dont add duplicates
        """
        cs = ep.AddSoup(Resource)
        newSoup = new_entity_name("soup")
        cs.post(newSoup)
        try:
            cs.post(newSoup)
            self.assertTrue(False) # test fails if we add user twice
        except:
            self.assertTrue(True)
            
    def test_delete_soup1(self):
        """
        Post-condition: we can create and delete a soup
        """
        newSoup = new_entity_name("soup")
        ds = ep.DeleteSoup(Resource)
        db.add_soup(newSoup)
        ds.post(newSoup)
        soups = db.get_soup()
        self.assertNotIn(newSoup, soups)
           
    def test_delete_soup2(self):
        """
        Post-condition: we can't delete a non-existing soup
        """
        newSoup = new_entity_name("soup")
        ds = ep.DeleteSoup(Resource)
        try:
            ds.post(newSoup)
            self.assertTrue(False) #only fails if it deletes non-existing soup
        except:
            self.assertTrue(True)
            
    def test_add_user1(self):
        """
        Post-condition: we can create a user
        """
        cu = ep.AddUser(Resource)
        newUser = new_entity_name("user")
        cu.post(newUser)
        users = db.get_users()
        self.assertIn(newUser,users)
        
    def test_add_user2(self):
        """
        Post-condition: we can create a user
        """
        cu = ep.AddUser(Resource)
        newUser = new_entity_name("user")
        cu.post(newUser)
        try:
            cu.post(newUser)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
 
    def test_delete_user1(self):
        """
        Post-condition: we can create and delete a user
        """
        newUser = new_entity_name("user")
        du = ep.DeleteUser(Resource)
        db.add_user(newUser)
        du.post(newUser)
        users = db.get_users()
        self.assertNotIn(newUser, users)
        
    def test_delete_user2(self):
        """
        Post-condition: we cant delete a non-existing user
        """
        newUser = new_entity_name("user")
        du = ep.DeleteUser(Resource)
        try:
            du.post(newUser)
            self.assertTrue(False)
        except:
            self.assertTrue(True)
