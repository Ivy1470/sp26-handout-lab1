"""Tests for Lab 1 Question 1"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q1 import validate_password

class TestValidatePassword(unittest.TestCase):
    """Unit tests for the validate_password function."""

    def test_valid_password(self) -> None:
        """Test a valid password returns True and prints nothing."""
        buf = StringIO()
        with redirect_stdout(buf):
            result = validate_password("Abcdef1!")
        output = buf.getvalue()

        self.assertTrue(result)
        self.assertEqual(output, "")

    def test_too_short(self) -> None:
        """Test password shorter than 8 characters fails Requirement 1."""
        buf = StringIO()
        with redirect_stdout(buf):
            result = validate_password("Ab1!")
        output = buf.getvalue()

        self.assertFalse(result)
        self.assertIn("Requirement 1 not met", output)

    def test_missing_uppercase(self) -> None:
        """Test missing uppercase letter fails Requirement 2."""
        buf = StringIO()
        with redirect_stdout(buf):
            result = validate_password("abcdef1!")
        output = buf.getvalue()

        self.assertFalse(result)
        self.assertIn("Requirement 2 not met", output)