"""
Please implement this stub function to match the documentation.
Make sure to implement tests in the tests directory.
"""

import sys
sys.path.append('.')
from src.q1 import validate_password

def set_password() -> None:
    """
    1. Ask the user to input a password
    2. If it is not valid, print the 
       requirements which are not met and go back to step 1.
       (Keep repeating until password is valid)
    """
    # This function will require calling validate_password from q1
while True:
        password = input("Enter a password: ")
        if validate_password(password):
            break
