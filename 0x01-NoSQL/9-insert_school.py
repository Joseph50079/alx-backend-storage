#!/usr/bin/env python3

"""Insert into collection"""


def insert_school(mongo_collection, **kwargs):
    """insert_school inserts school documents in school collection

    Args:
        mongo_collection: collection
        kwargs: dictionary documents to be inserted into collection [school]
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
