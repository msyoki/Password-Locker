class Profile:
    """
    Class that generates new instances of user profiles
    """
    profile_list = []

    def __init__(self, username, password):
        """
        __init__ method to define the properties of a user profile object

        Args:
            username : username for a profile
            password : password for a profile
        """

        self.username = username
        self.password = password


    def save_profile(self):

        """
        save_profile method to save profile object into profile_list
        """

        Profile.profile_list.append(self)
