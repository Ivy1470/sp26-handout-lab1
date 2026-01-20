"""
Please implement this stub function to match the documentation.
As always, make sure to implement tests in the tests directory.
"""

from typing import Optional


def most_common_letter(s: str) -> Optional[str]:
    """Finds the most common letter in a given string.
    
    Parameters
    ----------
    s : str
        The input string
    
    Returns
    -------
    Optional[str]
        The most common letter in the string. If there is a tie, return the 
        letter that comes first alphabetically.
        Ignore case -- 'a' is equal to 'A'. Non-letter characters should be ignored.
        If there are no letters in the string, return None.
    """
    letter_counts: dict[str, int] = {}

    
    for char in s:
        if char.isalpha():
            lower_char = char.lower()
            if lower_char in letter_counts:
                letter_counts[lower_char] += 1
            else:
                letter_counts[lower_char] = 1
    
    if len(letter_counts) == 0:
        return None
    

    max_count = 0
    most_common = None
    

    for letter in sorted(letter_counts.keys()):
        if letter_counts[letter] > max_count:
            max_count = letter_counts[letter]
            most_common = letter
    
    return most_common
