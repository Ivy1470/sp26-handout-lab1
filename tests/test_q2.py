"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q2 import set_password
class TestSetPassword(unittest.TestCase):
    
    @patch('builtins.input', return_value='ValidPass1!')
    @patch('src.q1.validate_password', return_value=True)
    def test_valid_password_first_try(self, mock_validate: Mock, mock_input: Mock) -> None:
        """"Test that function accepts a valid password on first attempt."""
        set_password()
        mock_input.assert_called_once()
        mock_validate.assert_called_once_with('ValidPass1!')
    
    @patch('builtins.input', side_effect=['bad', 'wrong', 'nope', 'GoodPass1!'])
    @patch('src.q1.validate_password', side_effect=[False, False, False, True])
    def test_multiple_invalid_attempts(self, mock_validate: Mock, mock_input: Mock) -> None:
        """"Test that function handles multiple invalid password attempts."""
        set_password()
        self.assertEqual(mock_input.call_count, 4)
        self.assertEqual(mock_validate.call_count, 4)
    
    @patch('builtins.input', return_value='')
    @patch('src.q1.validate_password', side_effect=[False, False, True])
    def test_empty_password_then_valid(self, mock_validate: Mock, mock_input: Mock) -> None:
        """"Test handling of empty password followed by valid password."""
        mock_input.side_effect = ['', '', 'ValidPass1!']
        set_password()
        self.assertEqual(mock_input.call_count, 3)
    
    @patch('builtins.input', return_value='ValidPass1!')
    @patch('src.q1.validate_password', return_value=True)
    def test_prompt_message(self, mock_validate: Mock, mock_input: Mock) -> None:
        """"Test that the correct prompt message is displayed."""
        set_password()
        mock_input.assert_called_with("Enter a password: ")


if __name__ == '__main__':
    unittest.main()