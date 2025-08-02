"""
This module checks the validity of the login credentials.
"""

def valid_login(username, password):
    """
    Checks the validity of the login credentials.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        bool: returns the validity of the login
    """

    if (username == password) and username != "" and password != "":
        return True
    else:
        return False
