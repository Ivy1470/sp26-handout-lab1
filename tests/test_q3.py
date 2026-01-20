"""Tests for Lab 1 Question 3"""

import sys
sys.path.append(".")
import unittest
from unittest.mock import patch, Mock
from src.q3 import (
    income_tax_fed,
    income_tax_ca,
    income_tax_ma,
    income_tax_ny,
    calculate_income_tax
)

def test_income_tax_ma() -> None:
    """Test Massachusetts flat tax rate"""
    assert income_tax_ma(50000) == 2500.0
    assert income_tax_ma(100000) == 5000.0
    assert income_tax_ma(0) == 0.0

def test_income_tax_fed() -> None:
    """Test federal progressive tax"""
    # Test income in first bracket
    assert income_tax_fed(10000) == 1000.0
    # Test income in second bracket
    assert abs(income_tax_fed(50000) - 6633.0) < 1.0
    # Test higher income
    assert abs(income_tax_fed(100000) - 17400.5) < 1.0

def test_income_tax_ca() -> None:
    """Test California progressive tax"""
    # Test income in first bracket
    assert abs(income_tax_ca(10000) - 100.0) < 1.0
    # Test income in multiple brackets
    assert abs(income_tax_ca(50000) - 1814.64) < 10.0

def test_income_tax_ny() -> None:
    """Test New York progressive tax"""
    # Test income in first bracket
    assert abs(income_tax_ny(8000) - 320.0) < 1.0
    # Test income in multiple brackets
    assert abs(income_tax_ny(50000) - 2436.5) < 10.0

def test_zero_income() -> None:
    """Test that zero income results in zero tax"""
    assert income_tax_fed(0) == 0.0
    assert income_tax_ca(0) == 0.0
    assert income_tax_ma(0) == 0.0
    assert income_tax_ny(0) == 0.0