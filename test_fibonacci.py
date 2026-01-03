import pytest
from fibonacci import get_nth, FibonacciIterator

#!/usr/bin/env python3

"""Tests for the Fibonacci sequence generator."""



class TestGetNth:
    """Test cases for the get_nth function."""

    def test_get_nth_zero(self):
        """Test that the 0th Fibonacci number is 1."""
        assert get_nth(0) == 1

    def test_get_nth_first(self):
        """Test that the 1st Fibonacci number is 1."""
        assert get_nth(1) == 1

    def test_get_nth_second(self):
        """Test that the 2nd Fibonacci number is 2."""
        assert get_nth(2) == 2

    def test_get_nth_third(self):
        """Test that the 3rd Fibonacci number is 3."""
        assert get_nth(3) == 3

    def test_get_nth_fourth(self):
        """Test that the 4th Fibonacci number is 5."""
        assert get_nth(4) == 5

    def test_get_nth_tenth(self):
        """Test that the 10th Fibonacci number is 89."""
        assert get_nth(10) == 89

    def test_get_nth_large(self):
        """Test a larger Fibonacci number."""
        assert get_nth(20) == 10946

    def test_get_nth_sequence(self):
        """Test multiple Fibonacci numbers in sequence."""
        expected = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
        for i, expected_val in enumerate(expected):
            assert get_nth(i) == expected_val