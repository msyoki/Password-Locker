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


def user_log_in(name, password):
    '''
    Function that allows a user to log into their credential account
    Args:
        name : the name the user used to create their user account
        password : the password the user used to create their user account
    '''
    log_in = User.log_in(name, password)
    if log_in != False:
        return User.log_in(name, password)


def create_credentail(user_password, name, password):
    '''
    Function to create a credential 
    Args:
        user_password : the password for Password Locker
        name : the name of the account 
        password : the password for the account
    '''

    new_credentail = Credential(user_password,name,password)

    return new_credentail