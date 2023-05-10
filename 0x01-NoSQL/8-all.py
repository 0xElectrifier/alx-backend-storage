#!/usr/bin/env python3
"""Defines a function `list_all`"""
from typing import List
import pymongo
from pymongo import MongoClient


def list_all(mongo_collection) -> List:
    """Lists all documents in @mongo_collection
    Args:
        mongo_collection: pymongo collection object caontainig objects to be listed
    Returns:
        the list of documents in @mongo_collection, otherwise []
        if no document is in @mongo_collection
    """
    collections: List = list(mongo_collection.find())
    return collections
