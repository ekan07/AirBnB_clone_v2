#!/usr/bin/python3
"""
Unittest for the DBStorage class
"""

import unittest
import os
import MySQLdb
from io import StringIO
from unittest.mock import patch
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.amenity import Amenity
from models import storage
from console import HBNBCommand


classes = {"Amenity": Amenity, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}
if os.getenv("HBNB_TYPE_STORAGE") == 'db':
    my_db = MySQLdb.connect(host=os.getenv("HBNB_MYSQL_HOST"),
                            port=3306,
                            user=os.getenv("HBNB_MYSQL_USER"),
                            password=os.getenv("HBNB_MYSQL_PWD"),
                            db=os.getenv("HBNB_MYSQL_DB"))
    cursor = my_db.cursor()


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "Testing db storage")
class test_DBStorage(unittest.TestCase):
    """ Class to test the Database storage methods """

    def test_delete(self):
        """Test that deleting an instance deletes the entry in the database"""
        SQL = "SELECT COUNT(name) FROM states"
        state = State(name="Georgia")
        state.save()
        cursor.execute(SQL)
        count = int(cursor.fetchone()[0])
        my_db.commit()
        state.delete()
        storage.save()
        cursor.execute(SQL)
        new_count = int(cursor.fetchone()[0])
        self.assertEqual(count - 1, new_count)

    def test_save(self):
        """Test that creating a new objects creates an entry in the database"""
        SQL = "SELECT COUNT(name) FROM states"
        cursor.execute(SQL)
        count = int(cursor.fetchone()[0])
        my_db.commit()
        state = State(name="Kansas")
        state.save()
        cursor.execute(SQL)
        new_count = int(cursor.fetchone()[0])
        self.assertEqual(count + 1, new_count)

    def test_all(self):
        """Test that the all method returns all instances"""
        state = State(name="New York")
        state.save()
        amenity = Amenity(name="Garden")
        amenity.save()
        user = User(email="jj@menow.com", password="jjpwd")
        user.save()
        my_state = storage.all("State")
        self.assertIn(state, my_state.values())
        my_amenity = storage.all("Amenity")
        self.assertIn(amenity, my_amenity.values())
        my_user = storage.all("User")
        self.assertIn(user, my_user.values())
        all = storage.all()
        self.assertIn(state, all.values())
        self.assertIn(amenity, all.values())
        self.assertIn(user, all.values())


@unittest.skipIf(os.getenv("HBNB_TYPE_STORAGE") != 'db', "Testing db storage")
class test_DBStorage_Tables(unittest.TestCase):
    """ Test that the links between tables were created properly """

    def test_table_links(self):
        """ Test that the necessary table links and delete relationships
            have been set up
        """
        # Create States
        state = State(name="California")
        state.save()
        state_2 = State(name="New York")
        state_2.save()
        # Create Cities
        city = City(state_id=state.id, name="San Francisco")
        city.save()
        city_2 = City(state_id=state.id, name="Cali City")
        city_2.save()
        city_3 = City(state_id=state_2.id, name="New York")
        city_3.save()
        # Create Users
        user = User(email="jj@mm.com", password="jjpwd")
        user.save()
        user_2 = User(email="mm@jj.com", password="mmpwd")
        user_2.save()
        # Create Places
        place = Place(user_id=user.id, city_id=city.id, name="House 1")
        place.save()
        place_2 = Place(user_id=user_2.id, city_id=city_2.id, name="House 2")
        place_2.save()
        place_3 = Place(user_id=user_2.id, city_id=city_3.id, name="House 3")
        place_3.save()
        # Create Amenity
        amenity = Amenity(name="Wifi")
        amenity.save()
        amenity_2 = Amenity(name="Cable")
        amenity_2.save()
        amenity_3 = Amenity(name="Oven")
        amenity_3.save()
        # link place_1 with 2 amenities
        place.amenities.append(amenity)
        place.amenities.append(amenity_2)
        # link place_2 with 3 amenities
        place_2.amenities.append(amenity)
        place_2.amenities.append(amenity_2)
        place_2.amenities.append(amenity_3)
        # link place_3 with 1 amenity
        place_3.amenities.append(amenity)
        # Create Reviews
        review = Review(text="Nice view from the front balcony",
                        place_id=place.id, user_id=user.id)
        review.save()
        review_2 = Review(text="Nothing nice to say",
                          place_id=place_2.id, user_id=user.id)
        review_2.save()
        review_3 = Review(text="This place sucks",
                          place_id=place_3.id, user_id=user_2.id)
        review_3.save()

        # Deleting a State should delete all linked Cities
        # and places and review
        state_2_key = "State." + state_2.id
        city_3_key = "City." + city_3.id
        place_3_key = "Place." + place_3.id
        review_3_key = "Review." + review_3.id
        state_2.delete()
        storage.save()
        all = storage.all().keys()
        self.assertNotIn(state_2_key, all)
        self.assertNotIn(city_3_key, all)
        self.assertNotIn(place_3_key, all)
        self.assertNotIn(review_3_key, all)

        # Deleting a place should leave the amenities present
        amenity_key = "Amenity." + amenity.id
        self.assertIn(amenity_key, all)

        # Deleting a user should delete all linked reviews
        user_2_key = "User." + user_2.id
        user_2.delete()
        storage.save()
        all = storage.all().keys()
        self.assertNotIn(user_2_key, all)

        # Deleting a City should delete all linked Places and Reviews
        city_2_key = "City." + city_2.id
        place_2_key = "Place." + place_2.id
        review_2_key = "Review." + review_2.id
        city_2.delete()
        storage.save()
        all = storage.all().keys()
        self.assertNotIn(city_2_key, all)
        self.assertNotIn(place_2_key, all)
        self.assertNotIn(review_2_key, all)
