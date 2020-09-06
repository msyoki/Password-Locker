#!/usr/bin/env python3.8
"""
This is the file that runs the application
Import Profile Class from profile Module and Account Class from accounts Module
"""

from user import User
from credentials import Credential

def create_user(name, password):
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


def save_credentials(credential):
    '''
    Function to save a credential
    Args:
        credential : the credential to be saved
    '''

    credential.save_credential()

def delete_credentials(credential):
    """
    Function to deletes a credential
    Args:
        credential : the credential to be deleted
    """
    credential.delete_credential()

def check_existing_credentials(name):
    '''
    Function that checks if a user credential name already exists
    Args:
        name : the credential name
    '''

    return Credential.credential_exist(name)

def display_users():
    '''
    Function that returns all the saved users 
    '''

    return User.display_user()

def display_credentials(password):
    '''
    Function that returns all the saved credentials
    '''

    return Credential.display_credential(password)


def create_generated_password(name):
    '''
    Function that generates a password for the user 
    Args:
        name : the name of the account
    '''
    password = Credential.generate_password()

    return password

