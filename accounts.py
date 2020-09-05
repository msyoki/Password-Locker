from random import choice
import string

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
     
    @classmethod   
    def generate_password(cls):
        """
        Method that generates a random alphanumeric password
        """

        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase
        #string.ascii_uppercase/lowercase (String constants) - These values are not locale-dependent and will not change.
         
        password = ''.join( choice(alphanum) for num in range(8) )
        # Create password
        
        return password

    @classmethod
    def display_account(cls,password):
        '''
        Method that returns the account list
        Args:
            password : the user password
        '''
        profile_account_list = []

        for account in cls.account_list:
            if account.profile_password == password:
                profile_account_list.append(account)

        return profile_account_list

        



