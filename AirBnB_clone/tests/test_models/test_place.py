#!/usr/bin/python3
""" This module contains the unittests for the place  module """

import unittest
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """ Test for class place  and its methods """

    def setUp(self):
        """ Set up method for place instance """

        self.place1 = Place()
        self.place2 = Place()

    def tearDown(self):
        """ tearDown method """
        pass

    def test_type(self):
        self.assertEqual(type(self.place1), Place)
        self.assertEqual(type(self.place2), Place)

    def test_city_id(self):
        self.assertTrue(hasattr(self.place1, "city_id"))
        self.assertTrue(type(self.place1.city_id) is str)
        self.assertEqual(self.place1.city_id, "")
        Place.city_id = "SF"
        self.assertEqual(self.place1.city_id, "SF")
        self.assertEqual(self.place1.city_id, self.place2.city_id)

    def test_user_id(self):
        self.assertTrue(hasattr(self.place1, "user_id"))
        self.assertTrue(type(self.place1.user_id) is str)
        self.assertEqual(self.place1.user_id, "")
        Place.user_id = "ALA"
        self.assertEqual(self.place1.user_id, "ALA")
        self.assertEqual(self.place1.user_id, self.place2.user_id)

    def test_name(self):
        self.assertTrue(hasattr(self.place1, "name"))
        self.assertTrue(type(self.place1.name) is str)
        self.assertEqual(self.place1.name, "")
        Place.name = "Great Falls"
        self.assertEqual(self.place1.name, "Great Falls")
        self.assertEqual(self.place1.name, self.place2.name)

    def test_description(self):
        self.assertTrue(hasattr(self.place1, "description"))
        self.assertTrue(type(self.place1.description) is str)
        self.assertEqual(self.place1.description, "")
        Place.description = "Nice House"
        self.assertEqual(self.place1.description, "Nice House")
        self.assertEqual(self.place1.description, self.place2.description)

    def test_number_rooms(self):
        self.assertTrue(hasattr(self.place1, "number_rooms"))
        self.assertTrue(type(self.place1.number_rooms) is int)
        self.assertEqual(self.place1.number_rooms, 0)
        Place.number_rooms = 4
        self.assertEqual(self.place1.number_rooms, 4)
        self.assertEqual(self.place1.number_rooms, self.place2.number_rooms)

    def test_number_bathrooms(self):
        self.assertTrue(hasattr(self.place1, "number_bathrooms"))
        self.assertTrue(type(self.place1.number_bathrooms) is int)
        self.assertEqual(self.place1.number_rooms, 0)
        Place.number_bathrooms = 10
        self.assertEqual(self.place1.number_bathrooms, 10)
        self.assertEqual(self.place1.number_bathrooms,
                         self.place2.number_bathrooms)

    def test_max_guest(self):
        self.assertTrue(hasattr(self.place1, "max_guest"))
        self.assertTrue(type(self.place1.max_guest) is int)
        self.assertEqual(self.place1.max_guest, 0)
        Place.max_guest = 15
        self.assertEqual(self.place1.max_guest, 15)
        self.assertEqual(self.place1.max_guest, self.place2.max_guest)

    def test_price_by_night(self):
        self.assertTrue(hasattr(self.place1, "price_by_night"))
        self.assertTrue(type(self.place1.price_by_night) is int)
        self.assertEqual(self.place1.price_by_night, 0)
        Place.price_by_night = 1000
        self.assertEqual(self.place1.price_by_night, 1000)
        self.assertEqual(self.place1.price_by_night,
                         self.place2.price_by_night)

    def test_latitude(self):
        self.assertTrue(hasattr(self.place1, "latitude"))
        self.assertTrue(type(self.place1.latitude) is float)
        self.assertEqual(self.place1.latitude, 0.0)
        Place.latitude = 36.0
        self.assertEqual(self.place1.latitude, 36.0)
        self.assertEqual(self.place1.latitude, self.place2.latitude)

    def test_longitude(self):
        self.assertTrue(hasattr(self.place1, "longitude"))
        self.assertTrue(type(self.place1.longitude) is float)
        self.assertEqual(self.place1.longitude, 0.0)
        Place.longitude = 40.0
        self.assertEqual(self.place1.longitude, 40.0)
        self.assertEqual(self.place1.longitude, self.place2.longitude)

    def test_amenity_ids(self):
        self.assertTrue(hasattr(self.place1, "amenity_ids"))
        self.assertTrue(type(self.place1.amenity_ids) is list)
        self.assertEqual(self.place1.amenity_ids, [])
        Place.amenity_ids = ["id1", "id2"]
        self.assertEqual(self.place1.amenity_ids, ["id1", "id2"])
        self.assertEqual(self.place1.amenity_ids, self.place2.amenity_ids)

    def test_isinstance(self):
        self.assertTrue(isinstance(self.place1, BaseModel))
        self.assertFalse(type(self.place1) is BaseModel)

if __name__ == '__main__':
    unittest.main()
