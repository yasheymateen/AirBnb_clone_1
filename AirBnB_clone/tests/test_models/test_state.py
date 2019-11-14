#!/usr/bin/python3
""" This module contains the unittests for the user module """

import unittest
from models.base_model import BaseModel
from models.state import State


class TestState(unittest.TestCase):
    """ Test for class user and its methods """

    def setUp(self):
        """ Set up method for user instance """
        self.state1 = State()
        self.state2 = State()

    def tearDown(self):
        """ tearDown method """
        pass

    def test_type(self):
        self.assertEqual(type(self.state1), State)
        self.assertEqual(type(self.state2), State)

    def test_name(self):
        self.assertTrue(hasattr(self.state1, "name"))
        self.assertTrue(type(self.state1.name) is str)
        self.assertEqual(self.state1.name, "")
        State.name = "California"
        self.assertEqual(self.state1.name, "California")
        self.assertEqual(self.state1.name, self.state2.name)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.state1, BaseModel))
        self.assertFalse(type(self.state1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
