from credentials import Credential


class User:
    """
    Class that generates new instances of user
    """

    # Empty list of users

    user_list = []

    def __init__(self, user_name, user_password):
        """
        __init__ method to define the properties of a user object

        Args:
            name : name for a user
            password : password for a user
        """

        self.user_name = user_name
        self.user_password = user_password

    def save_user(self):

        """
        save_user method to save user object into profile_list
        """

        User.user_list.append(self)

    @classmethod
    def find_credential(cls, name):
        '''
        Method that checks if credentials is imported correctly
        Args:
            name : name of the credential
        Returns:
            Boolean : True / False if the credential exists or does not exist
        '''

        # Search for the credential in the credential_list
        for credential in Credential.credential_list:
            if credential.credential_name == name:
                return True

        return False

    @classmethod
    def log_in(cls, name, password):
        """
        Method that allows a user to log into their profile 

        Arg:
            name:name of the profile
            password:password of the profile

        Returns:
            credential list for the profile that matches the name and password
            False: if the name or password is incorrect
        """

        # Search for the user in the user list
        for user in cls.user_list:
            if user.user_name == name and user.user_password == password:
                return Credential.credential_list

        return False

    @classmethod
    def display_user(cls):
        """
        Method that returns the user list
        """

        return cls.user_list
