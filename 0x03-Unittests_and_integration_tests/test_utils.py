#!/usr/bin/env python3
"""Unit tests for utils.py"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test cases for access_nested_map"""

    @parameterized.expand([
        ("simple_map", {"a": 1}, ("a",), 1),
        ("nested_map", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("deep_nested", {"a": {"b": {"c": 3}}}, ("a", "b", "c"), 3),
    ])
    def test_access_nested_map(self, name, nested_map, path, expected):
        """Test successful access"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ("missing_key", {}, ("a",)),
        ("nested_missing", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, name, nested_map, path):
        """Test KeyError raised for missing keys"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Test cases for get_json"""

    @patch("utils.requests.get")
    def test_get_json(self, mock_get):
        """Test get_json returns expected result"""
        url = "http://example.com"
        expected = {"payload": True}
        mock_get.return_value = Mock(**{"json.return_value": expected})

        result = get_json(url)
        mock_get.assert_called_once_with(url)
        self.assertEqual(result, expected)


class TestMemoize(unittest.TestCase):
    """Test cases for memoize decorator"""

    def test_memoize(self):
        """Test that memoize caches method result"""

        class TestClass:
            call_count = 0

            @memoize
            def a_method(self):
                self.call_count += 1
                return 42

        obj = TestClass()
        self.assertEqual(obj.a_method, 42)
        self.assertEqual(obj.a_method, 42)
        self.assertEqual(obj.call_count, 1)  # should only be called once


if __name__ == '__main__':
    unittest.main()
