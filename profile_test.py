import unittest # Importing the unittest module
from profile import Profile # Importing the contact class

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
        self.new_profile = Profile("JohnDoe","Passlockjd2020#") # create profile object


    def test_init(self):
        '''
        test_init test case to test if the object is initialized properly
        '''

        self.assertEqual(self.new_profile.username,"JohnDoe")
        self.assertEqual(self.new_profile.password,"Passlockjd2020#")
        
    def test_save_profile(self):
        """
        test_save_profile test case to test if profile object is saved into the profile_list
        """

        self.new_profile.save_profile() # saving the new profile
        self.assertEqual(len(Profile.profile_list),1)


if __name__ == '__main__':
    unittest.main()