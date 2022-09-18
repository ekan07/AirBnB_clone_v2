#!/usr/bin/python3
""" Contains tests for class User """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
from models import user
import pep8
import inspect
import unittest


class test_User(test_basemodel):
    """ Tests for class User """

    def __init__(self, *args, **kwargs):
        """ Initialize class and set up resources """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test first_name attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "first_name"))
        self.assertEqual(new.first_name, None)

    def test_last_name(self):
        """ Test last_name attribute is empty"""
        new = self.value()
        self.assertTrue(hasattr(new, "last_name"))
        self.assertEqual(new.last_name, None)

    def test_email(self):
        """ Test email attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "email"))
        self.assertEqual(new.email, None)

    def test_password(self):
        """ Test password attribute is empty """
        new = self.value()
        self.assertTrue(hasattr(new, "password"))
        self.assertEqual(new.password, None)


class TestUserDocs(unittest.TestCase):
    """Tests to check the documentation and style of User class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.user_f = inspect.getmembers(User, inspect.isfunction)

    def test_pep8_conformance_user(self):
        """Test that models/user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """Test that tests/test_models/test_user.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_user.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_user_module_docstring(self):
        """Test for the user.py module docstring"""
        self.assertIsNot(user.__doc__, None,
                         "user.py needs a docstring")
        self.assertTrue(len(user.__doc__) >= 1,
                        "user.py needs a docstring")

    def test_user_class_docstring(self):
        """Test for the City class docstring"""
        self.assertIsNot(User.__doc__, None,
                         "User class needs a docstring")
        self.assertTrue(len(User.__doc__) >= 1,
                        "User class needs a docstring")

    def test_user_func_docstrings(self):
        """Test for the presence of docstrings in User methods"""
        for func in self.user_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
