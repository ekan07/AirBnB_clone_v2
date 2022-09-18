#!/usr/bin/python3
""" Test the City Class """
import pep8
import unittest
import inspect
from tests.test_models.test_base_model import test_basemodel
from models.city import City
from models import city


class test_City(test_basemodel):
    """ Test for class City """

    def __init__(self, *args, **kwargs):
        """ Initialize the class and set up relevant resources """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test state_id attribute to be an empty string """
        new = self.value()
        self.assertTrue(hasattr(new, "state_id"))
        self.assertEqual(new.state_id, None)

    def test_name(self):
        """ Test name attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "name"))
        self.assertEqual(new.name, None)

    def test_to_dict(self):
        """Tests that the to_dict method returns a dictionary"""
        city_dict = self.value().to_dict()
        self.assertEqual(type(city_dict), dict)

    def test_to_dict_assert_values(self):
        """Test that the values in to_dict() are correct"""
        city = self.value()
        city_dict = city.to_dict()
        self.assertNotIn("_sa_instance_state", city_dict.keys())
        self.assertEqual(city_dict["__class__"], "City")
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(city_dict["created_at"],
                         city.created_at.strftime(t_format))
        self.assertEqual(city_dict["updated_at"],
                         city.updated_at.strftime(t_format))

    def test_str(self):
        """Test that the str method has the correct output"""
        city = self.value()
        string = "[City] ({}) {}".format(city.id, city.to_dict())
        self.assertEqual(string, str(city))


class TestCityDocs(unittest.TestCase):
    """Tests to check the documentation and style of City class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.city_f = inspect.getmembers(City, inspect.isfunction)

    def test_pep8_conformance_city(self):
        """Test that models/city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """Test that tests/test_models/test_city.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_city.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_city_module_docstring(self):
        """Test for the city.py module docstring"""
        self.assertIsNot(city.__doc__, None,
                         "city.py needs a docstring")
        self.assertTrue(len(city.__doc__) >= 1,
                        "city.py needs a docstring")

    def test_city_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(City.__doc__, None,
                         "City class needs a docstring")
        self.assertTrue(len(City.__doc__) >= 1,
                        "City class needs a docstring")

    def test_city_func_docstrings(self):
        """Test for the presence of docstrings in City methods"""
        for func in self.city_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
