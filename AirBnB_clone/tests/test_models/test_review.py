#!/usr/bin/python3
""" This module contains the unittests for the user module """

import unittest
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """ Test for class user and its methods """

    def setUp(self):
        """ Set up method for user instance """

        self.review1 = Review()
        self.review2 = Review()

    def tearDown(self):
        """ tearDown method """
        pass

    def test_type(self):
        self.assertEqual(type(self.review1), Review)
        self.assertEqual(type(self.review2), Review)

    def test_place_id(self):
        self.assertTrue(hasattr(self.review1, "place_id"))
        self.assertTrue(type(self.review1.place_id) is str)
        self.assertEqual(self.review1.place_id, "")
        Review.place_id = "ID of Place"
        self.assertEqual(self.review1.place_id, "ID of Place")
        self.assertEqual(self.review1.place_id, self.review2.place_id)

    def test_user_id(self):
        self.assertTrue(hasattr(self.review1, "user_id"))
        self.assertTrue(type(self.review1.user_id) is str)
        self.assertEqual(self.review1.user_id, "")
        Review.user_id = "ALA"
        self.assertEqual(self.review1.user_id, "ALA")
        self.assertEqual(self.review1.user_id, self.review2.user_id)

    def test_text(self):
        self.assertTrue(hasattr(self.review1, "text"))
        self.assertTrue(type(self.review1.text) is str)
        self.assertEqual(self.review1.text, "")
        Review.text = "Awesome"
        self.assertEqual(self.review1.text, "Awesome")
        self.assertEqual(self.review1.text, self.review2.text)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.review1, BaseModel))
        self.assertFalse(type(self.review1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
