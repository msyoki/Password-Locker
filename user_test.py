import unittest # Importing the unittest module
from user import User # Importing the user class
from credentials import Credential

class TestUser(unittest.TestCase):

    '''
    Test class that defines test cases for the user class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user= User("JohnDoe","JohnD2020#") # create user object

    
    
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        User.user_list = []



    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_user.user_name,"JohnDoe")
        self.assertEqual(self.new_user.user_password,"JohnD2020#")
        
    def test_save_user(self):
        """
        test_save_user test case to test if user object is saved into the user_list
        """

        self.new_user.save_user() # saving the new user
        self.assertEqual(len(User.user_list),1)


    def test_find_credential(self):
        '''
        Test case to test if the User module is importing from credentials module
        '''

        # Save the new user
        self.new_user.save_user()

        test_user= User("LizDoe","LizD2020#")

        test_user.save_user()

        found_credential = User.find_credential("Gmail")

        self.assertEqual( found_credential, False )


    def test_log_in(self):
        '''
        Test case to test if a user can log into their credential
        '''

        # Save the new user
        self.new_user.save_user()

        test_user= User("LizDoe","LizD2020#")

        test_user.save_user()

        found_credential = User.log_in("LizDoe", "LizD2020#")

        self.assertEqual( found_credential, Credential.credential_list )   

    
    def test_display_user(self):
        """
        Test case to test if a user can see a list of all the users saved
        """
        
        self.assertEqual( User.display_user() , User.user_list )

if __name__ == '__main__':
    unittest.main()