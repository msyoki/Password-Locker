#!/usr/bin/env python3.8
"""
This is the file that runs the application
Import Profile Class from profile Module and Account Class from accounts Module
"""

from user import User
from credentials import Credential

def create_profile(name, password):
    """
    Function to create a user account
    Args:
        name : the name the user wants for the profile
        password : the password the user want for the profile
    """

    new_user= User(name,password)

    return new_user

def save_users(user):
    """
    Function to save a user account
    Args:
        user : the user account to be saved
    """

    user.save_user()

@classmethod
def find_credential(cls, name):
    """
    Method that checks if Credentials is imported correctly
    Args:
        name : name of the credential
    Returns:
        Boolean : True / False if the credential exists or does not exist
    """

    # Search for the user in the user list
    for credential in Credential.credential_list:
        if credential.credential_name == name:
            return True

    return False
