#!/usr/bin/python3
""" Module to test rectangle class """
import sys
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """ Class for test cases for the rectangle class """

    def test_area(self):
        """ Test for the area """
        r = Rectangle(4, 8)
        self.assertEqual(r.area(), 32)

    def test_id(self):
        """ Test for the id """
        a = Rectangle(10, 2)
        a2 = Rectangle (2, 10)
        a3 = Rectangle (2, 10)
        self.assertEqual(a2.id + 1, a3.id)

    def test_str(self):
        """ Test for the str """
        r = Rectangle(3, 3, 2, 2, 10)
        self.assertEqual("[Rectangle] (10) 2/2 - 3/3", str(r))
        r = Rectangle(5, 5, 1)
        self.assertEqual("[Rectangle] ({}) 1/0 - 5/5".format(r.id), str(r))

    def test_dictionary(self):
        """ Test for dictionary """
        r = Rectangle(5, 6, 7, 8, 30)
        r_dict = r.to_dictionary()
        self.assertEqual(r_dict['id'], 30)
        self.assertEqual(r_dict['width'], 5)
        self.assertEqual(r_dict['height'], 6)
        self.assertEqual(r_dict['x'], 7)
        self.assertEqual(r_dict['y'], 8)

    def test_values(self):
        """ Test for input values"""
        with self.assertRaises(ValueError):
            n = Rectangle(0, 0)
        with self.assertRaises(ValueError):
            n = Rectangle(1, 1, -5, -2)
    

