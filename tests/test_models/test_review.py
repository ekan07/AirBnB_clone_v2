#!/usr/bin/python3
""" Contains tests for class Review """
import inspect
import pep8
import unittest
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
from models import review


class test_review(test_basemodel):
    """ Tests for class Review """

    def __init__(self, *args, **kwargs):
        """ Initialize class for testing """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test place_id attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "place_id"))
        self.assertEqual(new.place_id, None)

    def test_user_id(self):
        """ Test user_id attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "user_id"))
        self.assertEqual(new.user_id, None)

    def test_text(self):
        """ Test text attribute to be an empty string"""
        new = self.value()
        self.assertTrue(hasattr(new, "text"))
        self.assertEqual(new.text, None)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary"""
        r = self.value()
        new_d = r.to_dict()
        self.assertEqual(type(new_d), dict)

    def test_to_dict_values(self):
        """test that values in dict returned from to_dict are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        r = self.value()
        new_d = r.to_dict()
        self.assertFalse("_sa_instance_state" in new_d)
        self.assertTrue("__class__" in new_d)
        self.assertEqual(new_d["__class__"], "Review")
        self.assertEqual(new_d["created_at"], r.created_at.strftime(t_format))
        self.assertEqual(new_d["updated_at"], r.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        review = self.value()
        string = "[Review] ({}) {}".format(review.id, review.to_dict())
        self.assertEqual(string, str(review))


class TestReviewDocs(unittest.TestCase):
    """Tests to check the documentation and style of Review class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.review_f = inspect.getmembers(Review, inspect.isfunction)

    def test_pep8_conformance_review(self):
        """Test that models/review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_review(self):
        """Test that tests/test_models/test_review.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_review.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_review_module_docstring(self):
        """Test for the review.py module docstring"""
        self.assertIsNot(review.__doc__, None,
                         "review.py needs a docstring")
        self.assertTrue(len(review.__doc__) >= 1,
                        "review.py needs a docstring")

    def test_review_class_docstring(self):
        """Test for the Review class docstring"""
        self.assertIsNot(Review.__doc__, None,
                         "Review class needs a docstring")
        self.assertTrue(len(Review.__doc__) >= 1,
                        "Review class needs a docstring")

    def test_review_func_docstrings(self):
        """Test for the presence of docstrings in Review methods"""
        for func in self.review_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))
