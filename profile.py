class Profile:
    """
    Class that generates new instances of passwords
    """
    profile_list = []

    def __init__(self, username, password):
        """
        __init__ method to define the properties of a User object

        Args:
            username : name of a user
            password : password for a user
        """

        self.username = username
        self.password = password


    def save_profile(self):

        """
        save_profile method to save profile objects into profile_list
        """

        Profile.profile_list.append(self)
