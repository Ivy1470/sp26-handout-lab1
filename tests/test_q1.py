"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q1 import validate_password

class TestValidatePassword(unittest.TestCase):
    """Unit tests for the validate_password function."""
    
    def test_valid_password(self) -> None:
        """Test a password that meets all requirements."""
        self.assertTrue(validate_password("Password1!"))
    
    def test_password_too_short(self) -> None:
        """Test a password that is too short."""
        self.assertFalse(validate_password("Pass1!"))
    
    def test_missing_uppercase(self) -> None:
        """Test a password missing uppercase letter."""
        self.assertFalse(validate_password("password1!"))

    def test_missing_lowercase(self) -> None:
        """Test a password missing lowercase letter."""
        self.assertFalse(validate_password("PASSWORD1!"))