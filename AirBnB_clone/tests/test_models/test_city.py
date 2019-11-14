#!/usr/bin/python3
""" This module contains the unittests for the user module """

import unittest
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """ Test for class user and its methods """

    def setUp(self):
        """ Set up method for user instance """

        self.city1 = City()
        self.city2 = City()

    def tearDown(self):
        """ tearDown method """
        pass

    def test_type(self):
        self.assertEqual(type(self.city1), City)
        self.assertEqual(type(self.city2), City)

    def test_state_id(self):
        self.assertTrue(hasattr(self.city1, "state_id"))
        self.assertTrue(type(self.city1.state_id) is str)
        self.assertEqual(self.city1.state_id, "")
        City.state_id = "MD"
        self.assertEqual(self.city1.state_id, "MD")
        self.assertEqual(self.city1.state_id, self.city1.state_id)

    def test_name(self):
        self.assertTrue(hasattr(self.city1, "name"))
        self.assertTrue(type(self.city1.name) is str)
        self.assertEqual(self.city1.name, "")
        City.name = "Baltimore"
        self.assertEqual(self.city1.name, "Baltimore")
        self.assertEqual(self.city1.name, self.city2.name)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.city1, BaseModel))
        self.assertFalse(type(self.city1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
