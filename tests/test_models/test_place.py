#!/usr/bin/python3
""" Test the Place class """
import pep8
import inspect
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
from models import place


class test_Place(test_basemodel):
    """ Tests for Place class """

    def __init__(self, *args, **kwargs):
        """ Initialize the class and set up some resources """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test city_id attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "city_id"))
        self.assertEqual(new.city_id, None)

    def test_user_id(self):
        """ Test user_id attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(new.user_id, None)

    def test_name(self):
        """ Test name attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, None)

    def test_description(self):
        """ Test description attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "description"))
        self.assertEqual(new.description, None)

    def test_number_rooms(self):
        """ Test number_rooms attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "number_rooms"))
        self.assertEqual(new.number_rooms, None)

    def test_number_bathrooms(self):
        """ Test number_bathrooms attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "number_bathrooms"))
        self.assertEqual(new.number_bathrooms, None)

    def test_max_guest(self):
        """ Test max_guest attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "max_guest"))
        self.assertEqual(new.max_guest, None)

    def test_price_by_night(self):
        """ Test price_by_night attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "price_by_night"))
        self.assertEqual(new.price_by_night, None)

    def test_latitude(self):
        """ Test latitude attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "latitude"))
        self.assertEqual(new.latitude, None)

    def test_longitude(self):
        """ Test longitude attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "longitude"))
        self.assertEqual(new.latitude, None)

    def test_amenity_ids(self):
        """ Test amenity_ids attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "amenity_ids"))
        self.assertEqual(type(new.amenity_ids), list)


class TestPlaceDocs(unittest.TestCase):
    """Tests to check the documentation and style of Place class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.place_f = inspect.getmembers(Place, inspect.isfunction)

    def test_pep8_conformance_place(self):
        """Test that models/place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """Test that tests/test_models/test_place.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_place.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_place_module_docstring(self):
        """Test for the place.py module docstring"""
        self.assertIsNot(place.__doc__, None,
                         "place.py needs a docstring")
        self.assertTrue(len(place.__doc__) >= 1,
                        "place.py needs a docstring")

    def test_place_class_docstring(self):
        """Test for the Place class docstring"""
        self.assertIsNot(Place.__doc__, None,
                         "Place class needs a docstring")
        self.assertTrue(len(Place.__doc__) >= 1,
                        "Place class needs a docstring")

    def test_place_func_docstrings(self):
        """Test for the presence of docstrings in Place methods"""
        for func in self.place_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
