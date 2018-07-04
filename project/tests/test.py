# project/test.py
 
 
import unittest
 
from project import app
 
 
class ProjectTests(unittest.TestCase):
 
    ############################
    #### setup and teardown ####
    ############################
 
    # executed prior to each test
    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        self.app = app.test_client()
 
        self.assertEquals(app.debug, False)
 
    # executed after each test
    def tearDown(self):
        pass
 
 
    ########################
    #### helper methods ####
    ########################
 
 
 
    ###############
    #### tests ####
    ###############
 
    def test_main_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertIn(b'Welcome to Heart and Hand Admin', response.data)
        self.assertIn(b'This site is used for all of Heart and Hands Administration', response.data)
        self.assertIn(b'Adding Customers', response.data)
        self.assertIn(b'Adding Children', response.data)
        self.assertIn(b'Adding Classes', response.data)
        self.assertIn(b'Adding payments and expenses', response.data)
 
 
if __name__ == "__main__":
    unittest.main()