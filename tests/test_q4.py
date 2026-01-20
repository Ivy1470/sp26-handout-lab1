"""Tests for Lab 1 Question 4"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q4 import most_common_letter

class TestMostCommonLetterFunction(unittest.TestCase):
    """Unit tests for the most_common_letter function."""
    
    def test_simple_case(self) -> None:
        """Test with a simple string."""
        self.assertEqual(most_common_letter("hello"), "l")
        self.assertEqual(most_common_letter("aaa"), "a")
    
    def test_ignore_case(self) -> None:
        """Test that case is ignored."""
        self.assertEqual(most_common_letter("AAAaaa"), "a")
        self.assertEqual(most_common_letter("HeLLo"), "l")
    
    def test_tie_alphabetical(self) -> None:
        """Test that ties are broken alphabetically."""
        self.assertEqual(most_common_letter("aabb"), "a")
        self.assertEqual(most_common_letter("zzaa"), "a")
        self.assertEqual(most_common_letter("abcabc"), "a")
    
    def test_ignore_non_letters(self) -> None:
        """Test that non-letter characters are ignored."""
        self.assertEqual(most_common_letter("a1b2c3a4"), "a")
        self.assertEqual(most_common_letter("hello!!!"), "l")
        self.assertEqual(most_common_letter("123 abc 456 abc"), "a")
    
    def test_no_letters(self) -> None:
        """Test that None is returned when there are no letters."""
        self.assertIsNone(most_common_letter("123456"))
        self.assertIsNone(most_common_letter("!@#$%^"))
        self.assertIsNone(most_common_letter(""))