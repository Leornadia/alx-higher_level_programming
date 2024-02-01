#!/usr/bin/python3
"""Unittest for max_integer([..]) 
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_normal_list(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_one_element_list(self):
        self.assertEqual(max_integer([5]), 5)

    def test_floats(self):
        self.assertEqual(max_integer([1.5, 4.5, 3.0]), 4.5) 

    def test_ints_and_floats(self):
        self.assertEqual(max_integer([1, 4, 5.5]), 5.5)

    def test_ints_and_floats_negative(self):
        self.assertEqual(max_integer([-4, -1, -5.2]), -1)
    
    def test_only_negatives(self):
        self.assertEqual(max_integer([-7, -12, -15]), -7)

    def test_identical_values(self):
        self.assertEqual(max_integer([5, 5, 5]), 5)

    def test_string(self):
        self.assertEqual(max_integer("hello"), 'o')

    def test_list_of_strings(self):
        self.assertEqual(max_integer(["bob", "alex"]), "bob")

if __name__ == '__main__':
    unittest.main()
