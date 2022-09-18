#!/usr/bin/python3
"""Contains tests for the BaseModel Class """
from models.base_model import BaseModel
from models import base_model
import unittest
import datetime
from uuid import UUID
import json
import os
import inspect
import pep8 as pycodestyle


class test_basemodel(unittest.TestCase):
    """ Tests for the BaseModel Class"""

    def __init__(self, *args, **kwargs):
        """ Initialize the class"""
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Set up resources required for the class.
            Empty function
        """
        pass

    def tearDown(self):
        """Tear down resources that have been set up"""
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Test type of created instance"""
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test creation from keyword arguments """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    @unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") == 'db',
                     "Unsupported for db storage")
    def test_save(self):
        """ Testing save """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Test return value of str method """
        i = self.value()
        self.assertEqual(str(i), '[{}] ({}) {}'.format(self.name, i.id,
                                                       i.to_dict()))

    def test_todict(self):
        """ Test to_dict method returns required value """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test error raised when kwargs is None """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_id(self):
        """ Test data type of id attribute """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test data type of created_at attribute """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test data type of updated_at attribute """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)

    def test_kwargs_int(self):
        """ Test error raised when kwargs contains ints """
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)


class TestBaseModelDocs(unittest.TestCase):
    """Tests to check the documentation and style of BaseModel class"""

    @classmethod
    def setUpClass(self):
        """Set up for docstring tests"""
        self.base_funcs = inspect.getmembers(BaseModel, inspect.isfunction)

    def test_pep8_conformance(self):
        """Test that models/base_model.py conforms to PEP8."""
        for path in ['models/base_model.py',
                     'tests/test_models/test_base_model.py']:
            with self.subTest(path=path):
                errors = pycodestyle.Checker(path).check_all()
                self.assertEqual(errors, 0)

    def test_module_docstring(self):
        """Test for the existence of module docstring"""
        self.assertIsNot(base_model.__doc__, None,
                         "base_model.py needs a docstring")
        self.assertTrue(len(base_model.__doc__) > 1,
                        "base_model.py needs a docstring")

    def test_class_docstring(self):
        """Test for the BaseModel class docstring"""
        self.assertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.assertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel class needs a docstring")

    def test_func_docstrings(self):
        """Test for the presence of docstrings in BaseModel methods"""
        for func in self.base_funcs:
            with self.subTest(function=func):
                self.assertIsNot(func[1].__doc__, None,
                                 "{:s} method needs docstring".format(func[0]))
                self.assertTrue(len(func[1].__doc__) > 1,
                                "{:s} method needs docstring".format(func[0]))
