class Profile:
    """
    Class that generates new instances of passwords
    """
    Profile_list = []

    def __init__(self, username, password):
        """
        __init__ method to define the properties of a User object
        
        Args:
            username : name of a user
            password : password for a user
        """

        self.username = username
        self.password = password
