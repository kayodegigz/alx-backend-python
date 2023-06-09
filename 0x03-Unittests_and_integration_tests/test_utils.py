#!/usr/bin/env python3
"""Test to parametrize a unit test
"""
import unittest
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """Test access_nested_map utils methods
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """
        Tests the access nested map to see that it returns the accurate thing
         """
        returned_result = access_nested_map(nested_map, path)
        self.assertEqual(returned_result, expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """
        Testing with specified params to assert
        that the right exceptions are raised
        """
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)

        self.assertEqual(
            f'KeyError({str(error.exception)})', repr(error.exception))


class TestGetJson(unittest.TestCase):
    """ This class tests the get_json
    function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """ Mocked HTTP response
        """
        with patch('requests.get') as mocked_req:
            mocked_req.return_value.json.return_value = test_payload
            self.assertEqual(get_json(url=test_url), test_payload)


class TestMemoize(unittest.TestCase):
    """ Testigng memoization """

    def test_memoize(self):
        """ Test memoize """
        class TestClass:
            """Memoize Test Class """

            def a_method(self):
                """ A method, returns 42 """
                return 42

            @memoize
            def a_property(self):
                """ Method called twice """
                return self.a_method()

        with patch.object(TestClass, 'a_method') as mock:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mock.assert_called_once()
