"""Tests for Lab 1 Question 2"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q2 import set_password
class TestSetPassword(unittest.TestCase):
    """Unit tests for the set_password function."""

    @patch("builtins.input", side_effect=["Abcdef1!"])
    @patch("src.q2.validate_password", return_value=True)
    def test_valid_first_try(self, mock_validate, mock_input) -> None:
        """Valid on first try: should call input once and stop."""
        set_password()
        self.assertEqual(mock_input.call_count, 1)
        self.assertEqual(mock_validate.call_count, 1)

    @patch("builtins.input", side_effect=["bad", "Abcdef1!"])
    def test_invalid_then_valid(self, mock_input) -> None:
        """Invalid then valid: should loop twice and print unmet requirements once."""
        def fake_validate(pw: str) -> bool:
            if pw == "bad":
                print("Requirement 1 not met: at least 8 characters long")
                return False
            return True

        buf = StringIO()
        with patch("src.q2.validate_password", side_effect=fake_validate):
            with redirect_stdout(buf):
                set_password()

        output = buf.getvalue()
        self.assertEqual(mock_input.call_count, 2)
        self.assertIn("Requirement 1 not met", output)

    @patch("builtins.input", side_effect=["bad", "alsoBad", "Abcdef1!"])
    def test_two_invalid_then_valid(self, mock_input) -> None:
        """Two invalid then valid: should loop three times and print twice."""
        def fake_validate(pw: str) -> bool:
            if pw != "Abcdef1!":
                print("Requirement X not met")
                return False
            return True

        buf = StringIO()
        with patch("src.q2.validate_password", side_effect=fake_validate):
            with redirect_stdout(buf):
                set_password()

        output = buf.getvalue()
        self.assertEqual(mock_input.call_count, 3)
        self.assertEqual(output.count("Requirement X not met"), 2)

