import unittest # Importing the unittest module
from profile import Profile # Importing the profile class

class TestProfile(unittest.TestCase):

    '''
    Test class that defines test cases for the profile class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_profile = Profile("JohnDoe","JohnD2020#") # create profile object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_profile.profile_username,"JohnDoe")
        self.assertEqual(self.new_profile.profile_password,"JohnD2020#")
        
    def test_save_profile(self):
        """
        test_save_profile test case to test if profile object is saved into the profile_list
        """

        self.new_profile.save_profile() # saving the new profile
        self.assertEqual(len(Profile.profile_list),3)


    def test_find_account(self):
        '''
        Test case to test if the Profile module is importing from accounts module
        '''

        # Save the new profile
        self.new_profile.save_profile()

        test_profile = Profile("LizDoe","LizD2020#")

        test_profile.save_profile()

        found_account = Profile.find_account("Gmail")

        self.assertEqual( found_account, False )


if __name__ == '__main__':
    unittest.main()