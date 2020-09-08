#!/usr/bin/env python3.8
"""
This is the file that runs the application
Import Profile Class from profile Module and Account Class from accounts Module
"""

from user import User
from credentials import Credential
from termcolor import colored, cprint

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


def create_credential(user_password, name, password):
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

def delete_credential(credential):
    """
    delete_credential method deletes a saved credential from the credential_list
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

def main():
    '''
    Function running the Password Locker app
    '''
    print('\n')
    print('-'*50)
    cprint('WELCOME TO PASSWORD LOCKER APP','yellow',attrs=['bold'])
    print('-'*50)
    cprint('Use these short codes to navigate','cyan')
    print('.'*50)

    while True:
        '''
        Loop that is running the entire application
        '''

        print('''Short codes:\n
            cu - create a Password Locker app account \n
            du - display names of current Password Locker app users \n
            lg - log into your Password Locker app account \n
            ex - exit the Password Locker app account''')

        # Get short codes from the user
        short_code = input().lower()

        if short_code == 'cu':
            '''
            Creating a Password Locker app account
            '''

            print('-'*50)
            cprint("Create New Account",'green')
            print("-"*10)

            print("User name : ")
            user_name = input()

            print("Password : ")
            user_password = input()

            # Create and save new user
            save_users( create_user( user_name, user_password) )

            print('-'*50)
            cprint(f"Account created successfully !!! ",'green')
            print('-'*50)
            cprint("Please log-in",'cyan')
            print('-'*10)

        elif short_code == 'du':
            '''
            Display the names of the current users 
            '''

            if display_users():
                print('-'*50)
                cprint("Current Password Locker app Users:",'white',attrs=['bold'])
                print("-"*10)

                for user in display_users():
                    print(f"{user.user_name}")
                    print("-"*10)
            else:
                print('-'*50)
                print("Password Locker app  has no current user.\n let's sign you up")
                print("\n")

        elif short_code == 'lg':
            '''
            Logs in the user into their Password Locker app account
            '''
            print('-'*50)
            cprint("Log into Password Locker app Account",'green')
            print("-"*10)
            print("Enter the user name")
            user_name = input()
            print("Enter the password: ")
            user_password = input()
            print('\n')

            if user_log_in(user_name,user_password) == None:
                print('-'*50)
                cprint("Please try again or create an account",'red')
                print("\n")

            else:

                user_log_in(user_name,user_password)
                print('-'*50)
                cprint(f'Welcome to your account: {user_name}','green')
                print('-'*50)
                cprint('Navigate below; ','cyan')
                print('-'*10)

                while True:
                    '''
                    Loop to run functions after logging in,while loop lops till condition is met
                    '''
                    print('''  Short codes:
                    cc - add a credential \n
                    dc - display credentials \n
                    cg - create a credential with a generate password \n 
                    del - delete credential \n
                    ex - exit Credentials''')

                    # Get short code from the user
                    short_code = input().lower()

                    if short_code == 'cc':
                        '''
                        Creating a Credential
                        '''

                        print('-'*50)
                        cprint("New Credential",'yellow')
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        print("Password of the credential ...")
                        credential_password = input()

                        # Create and save new user
                        save_credentials( create_credential( user_password, credential_name, credential_password) )

                        print("\n")
                        cprint(f"Credentials for {credential_name} have been created and saved",'green')
                        print("\n")

                    elif short_code == 'dc':
                        '''
                        Displaying credential name and password
                        '''

                        if display_credentials(user_password):
                            print('-'*50)
                            print(f"{user_name}\'s credentials",'yellow',attrs=['bold'])
                            print("-"*10)

                            for credential in display_credentials(user_password):
                                cprint(f"Account ..... {credential.credential_name}",'yellow',attrs=['bold'])
                                cprint(f"Password .... {credential.credential_password}",'yellow',attrs=['bold'])
                                print("-"*10)

                        else:
                            print('-'*50)
                            cprint("You have no credentials",'red')
                            print("\n")

                    elif short_code == 'cg':
                        '''
                        Creating a credential with a generated password
                        '''

                        print('-'*50)
                        cprint("New Credential",'yellow')
                        print("-"*10)

                        print("Name of the credential ...")
                        credential_name = input()

                        # Save new credential with its generated password
                        save_credentials( Credential(user_password, credential_name, (create_generated_password(credential_name)) ) )
                        print("\n")
                        cprint(f"Credential '{credential_name}' has been created and saved",'yellow')
                        print("\n")

                        #Delete credential

                    elif short_code == 'del':
                        print('-'*50)
                        cprint("Enter credential name: ",'green')
                        print('-'*50)
                        credential_name = input()
                        print('-'*10)
                        """
                        check if credential exits then delete
                        """
                        if check_existing_credentials(credential_name) == True:
                            cprint(f"credential '{credential_name}' has been deleted",'green')
                            print('-'*10)
                        else:
                            cprint("no cerdential with this name",'red') 
                            print('-'*10) 

                        #exit credentials

                    elif short_code == 'ex':
                        print('-'*10)
                        cprint(f"See you later {user_name}",'yellow')
                        print('-'*50)
                        print("\n")
                        break

                    else:
                        print('-'*50)
                        cprint(f'''{short_code} does not compute.
                        Please use the short codes''','red')
                        print("\n")
            
            #exit user
        elif short_code == 'ex':
            '''
            Exit Password Locker app
            '''
            print('-'*50)
            cprint("Bye .....",'yellow')
            print('-'*10)

            break

        else:
            print('-'*50)
            cprint(f'''Come again, what's {short_code}?
             Please use the short codes''','cyan')
            print("\n")

if __name__ == '__main__':
    main()
