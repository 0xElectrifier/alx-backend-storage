#!/usr/bin/env python3
"""Module for Task_11, defines a function"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    schools = list(mongo_collection.find())
    filtered_schools = mongo_collection.find({ "topics": { '$in': [topic] } })
    """
    filtered_schools = []
    for school in schools:
        try:
            if topic in school['topics']:
                filtered_schools.append(school)
        except Exception as e:
            pass
    """

    return filtered_schools
