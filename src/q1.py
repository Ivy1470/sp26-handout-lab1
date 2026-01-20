"""
Please implement these stub functions to match the documentation.
Make sure to implement tests in the tests directory.
"""


def validate_password(password: str) -> bool:
    """Determines whether a password meets the requirements. If any requirements
    are not met, prints which requirements were not met.

    Requirements:
    1. Password must be at least 8 characters long
    2. Password must contain at least one uppercase letter
    3. Password must contain at least one lowercase letter
    4. Password must contain at least one digit
    5. Password must contain at least one special character (!@#$%^&*)

    
    Parameters
    ----------
    password : str
        The password to validate
    
    Returns
    -------
    bool
        True if the password is valid, and false otherwise
    """
    unmet = []

    if len(password) < 8:
        unmet.append("Requirement 1 not met: at least 8 characters long")

    if not any(ch.isupper() for ch in password):
        unmet.append("Requirement 2 not met: at least one uppercase letter")

    if not any(ch.islower() for ch in password):
        unmet.append("Requirement 3 not met: at least one lowercase letter")

    if not any(ch.isdigit() for ch in password):
        unmet.append("Requirement 4 not met: at least one digit")

    special = set("!@#$%^&*")
    if not any(ch in special for ch in password):
        unmet.append("Requirement 5 not met: at least one special character (!@#$%^&*)")

    if unmet:
        for msg in unmet:
            print(msg)
        return False

    return True