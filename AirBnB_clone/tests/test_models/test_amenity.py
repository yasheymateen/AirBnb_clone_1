#!/usr/bin/python3
""" This module contains the unittests for the user module """

import unittest
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """ Test for class user and its methods """

    def setUp(self):
        """ Set up method for user instance """

        self.amenity1 = Amenity()
        self.amenity2 = Amenity()

    def tearDown(self):
        """ tearDown method """
        pass

    def test_type(self):
        self.assertEqual(type(self.amenity1), Amenity)
        self.assertEqual(type(self.amenity2), Amenity)

    def test_name(self):
        self.assertTrue(hasattr(self.amenity1, "name"))
        self.assertTrue(type(self.amenity1.name) is str)
        self.assertEqual(self.amenity1.name, "")
        Amenity.name = "AC"
        self.assertEqual(self.amenity1.name, "AC")
        self.assertEqual(self.amenity1.name, self.amenity2.name)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.amenity1, BaseModel))
        self.assertFalse(type(self.amenity1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
