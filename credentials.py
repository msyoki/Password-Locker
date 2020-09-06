from random import choice
import string

class Credential:
    """
    class that generates instances of users credentials
    """

    #Empty list of credentials
    credential_list = []

    def __init__(self,user_password, credential_name, credential_password):
        '''
        __init__ method to define the properties of a User object
        Args:    
            user_password : password of the user user
            credential_name : name of an credential
           credential_password : password for the credential
        '''

        self.user_password = user_password
        self.credential_name = credential_name
        self.credential_password = credential_password

    def save_credential(self):
        """
        save_credential method to save credential object into acount_list
        """

        Credential.credential_list.append(self)     

    def delete_credential(self):
        """
        delete_contact method deletes a saved credential from the credential_list
        """

        Credential.credential_list.remove(self)
     
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
    def display_credential(cls,password):
        '''
        Method that returns the credential list
        Args:
            password : the user password
        '''
        user_credential_list = []

        for credential in cls.credential_list:
            if credential.user_password == password:
                user_credential_list.append(credential)

        return user_credential_list

        
    @classmethod
    def credential_exist(cls, name):
        
        '''
        Method that checks if a credential exists in the credential list
        
        Args:
            name: name of the credential to search
            
        Returns:
            Boolean: true/false depending if the contact exists
            
        '''
        
        for credential in cls.credential_list:
            if credential.credential_name == name:
                return True
            
        return False


