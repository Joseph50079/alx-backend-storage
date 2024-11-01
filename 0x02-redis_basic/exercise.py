#!/usr/bin/env python3

"""Caching"""

import redis
import typing
import uuid


class Cache:
    """
        Cache for redis OOP
    """

    def __init__(self):
        _redis = redis.Redis()
        _redis.flushdb()

    def store(self, data: typing.Union[float, str, bytes, int]) -> str:
        """ store() method for storing data

            Args:
                data: typing.Union[float, str, bytes, int] - data to be stored

            Return: key unique identifier
        """
        setd = {}
        key = str(uuid.uuid4())
        setd[key] = data
        redis.Redis().mset(setd)

        return key
