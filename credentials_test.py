import unittest  # Importing the unittest module
from credentials import Credential  # Importing the profile class


class TestProfile(unittest.TestCase):
    """
    Test class that defines test cases for the credential class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
    """

    def setUp(self):
        """
        Set up method to run before each test cases.
        """
        self.new_credential = Credential("JohnD2020#", "Gmail", "gmail20*")  # create credential object

    def tearDown(self):
        """
        tearDown method that does clean up after each test case has run.
        """
        Credential.credential_list = []

    def test_init(self):
        """
        test_init test case to test if the object is initialized properly
        """

        self.assertEqual(self.new_credential.user_password, "JohnD2020#")
        self.assertEqual(self.new_credential.credential_name, "Gmail")
        self.assertEqual(self.new_credential.credential_password, "gmail20*")

    def test_save_credential(self):
        """
        Test case to test if the credential object is saved into the credential_list
        """

        # Save the new credential
        self.new_credential.save_credential()

        self.assertEqual(len(Credential.credential_list), 1)

    def test_save_multiple_credential(self):
        """
        test_save_multiple_credentials to check if we can save multiple credential
        objects to our credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credential("JohnD2020#", "Gmail", "gmail20*")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

    def test_delete_credential(self):
        """
        test_delete_credential to test if we can remove an credential from our credential_list
        """
        self.new_credential.save_credential()
        test_credential = Credential("JohnD2020#", "Twitter", "Twitter20*")
        test_credential.save_credential()

        self.new_credential.delete_credential()  # Deleting an credential object
        self.assertEqual(len(Credential.credential_list), 1)

    def test_generate_password(self):
        """
        Test case to test if a user can log into their
        """

        generated_password = self.new_credential.generate_password()

        self.assertEqual(len(generated_password), 8)

    def test_display_credential(self):
        """
        test case to test if user can access a list of all the credentials saved 
        """

        # save new credentials
        self.new_credential.save_credential()

        test_credential = Credential("JohnD2020#", "Instagram", "Instajd20*")
        test_credential.save_credential()

        test_credential = Credential("JohnD2020#", "Linkedin", "Linkjd20*")
        test_credential.save_credential()

        self.assertEqual(len(Credential.display_credential("JohnD2020#")), 3)

    def test_credential_exist(self):
        """
        Test to check if we can return a boolean if we can't find the credential
        """

        # Save the new credential
        self.new_credential.save_credential()

        test_credential = Credential("JohnD2020#", "Gmail", "gmail20*")

        test_credential.save_credential()

        # use contact exist method
        credential_exist = Credential.credential_exist("Gmail")

        self.assertTrue(credential_exist)


if __name__ == '__main__':
    unittest.main()
