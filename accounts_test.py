import unittest # Importing the unittest module
from accounts import Account # Importing the profile class

class TestProfile(unittest.TestCase):

    """
    Test class that defines test cases for the account class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_account = Account("Passlockjd2020#","Gmail","gmail20*") # create account object

    
    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Account.account_list = []


    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_account.profile_password,"Passlockjd2020#")
        self.assertEqual(self.new_account.account_name,"Gmail")
        self.assertEqual(self.new_account.account_password,"gmail20*")

    def test_save_account(self):
        """
        Test case to test if the account object is saved into the account_list
        """

        # Save the new account
        self.new_account.save_account()

        self.assertEqual( len(Account.account_list), 1 )
    

    def test_save_multiple_account(self):
        """
        test_save_multiple_accounts to check if we can save multiple account
        objects to our contact_list
        """
        self.new_account.save_account()
        test_account = Account("Passlockjd2020#","Gmail","gmail20*") 
        test_account.save_account()
        self.assertEqual(len(Account.account_list),2)


       
if __name__ == '__main__':
    unittest.main()    