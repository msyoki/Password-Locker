from accounts import Account

class Profile:
    """
    Class that generates new instances of user profiles
    """

    #Empty list of user profiles 

    profile_list = []

    def __init__(self, profile_username, profile_password):
        """
        __init__ method to define the properties of a user profile object

        Args:
            username : username for a profile
            password : password for a profile
        """

        self.profile_username = profile_username
        self.profile_password = profile_password


    def save_profile(self):

        """
        save_profile method to save profile object into profile_list
        """

        Profile.profile_list.append(self)

    @classmethod
    def find_account(cls, name):
        '''
        Method that checks if accounts is imported correctly
        Args:
            name : name of the account
        Returns:
            Boolean : True / False if the credential exists or does not exist
        '''

        # Search for the account in the account_list
        for account in Account.account_list:
            if account.account_name == name:
                return True

        return False