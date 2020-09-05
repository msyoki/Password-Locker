class Account:
    """
    class that generates instances of users accounts
    """

    #Empty list of accounts
    account_list = []

    def __init__(self,profile_password, account_name, account_password):
        '''
        __init__ method to define the properties of a User object
        Args:
            profile_password : password of the user profile
            account_name : name of an account
            account_password : password for the account
        '''

        self.profile_password = profile_password
        self.account_name = account_name
        self.account_password = account_password

    def save_account(self):
        """
        save_account method to save account object into acount_list
        """

        Account.account_list.append(self)     

    def delete_account(self):
        """
        delete_contact method deletes a saved account from the account_list
        """

        Account.account_list.remove(self)
        