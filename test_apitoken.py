# test_apitoken.py
"""
Tests for ApiToken module.
"""

import unittest
from apitoken import ApiToken

class TestApiToken(unittest.TestCase):
    """Test cases for ApiToken class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ApiToken()
        self.assertIsInstance(instance, ApiToken)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ApiToken()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
