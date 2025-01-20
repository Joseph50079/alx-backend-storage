#!/usr/bin/env python3

"""Update all docment with match"""


def update_topics(mongo_collection, name, topics):
    """update_topics upates all document where name matches
    Args:
        mongo_collection: collection
        name: matching name
        topics: list of topics to update
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
