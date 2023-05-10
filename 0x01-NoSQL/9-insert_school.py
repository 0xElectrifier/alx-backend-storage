#!/usr/bin/env python3
"""Module for Task_9. Defines a function 'insert_school'"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection based on kwargs
    Args:
        mongo_collection: pymongo collection object
        kwargs (dict): key-value pairs to be inserted as documents
                       to the collection
    Returns:
        the generated '_id'
    """
    inserted_object = mongo_collection.insert_one(kwargs)
    return inserted_object.inserted_id
