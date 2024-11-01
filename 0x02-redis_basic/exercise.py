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
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: typing.Union[str, bytes, int, float]) -> str:
        """ store() method for storing data

            Args:
                data: typing.Union[float, str, bytes, int] - data to be stored

            Return: key unique identifier
        """
        setd = {}
        key = str(uuid.uuid4())
        setd[key] = data
        self._redis.mset(setd)

        return key

    def get(self, key: str, fn: typing.Optional[typing.Callable] = None):
        """ get() gets the value of the <key> in fn mode/format

        Args:
            key: key to value
            fn: type format to convert value to
        Return: return in fn format type
        """
        data = self._redis.get(key)

        if data is None:
            return None
        return fn(data) if fn else data

    def get_int(self, key: str) -> int:
        """get_int() method get the value in integer
        Args:
            key: key to the value
        Return: return in integer
        """

        return int(key)

    def get_str(self, key: str) -> str:
        """get_str() method to return value in str format
        Args:
            key: key to that value
        Return: in strinf format
        """

        return str(key)
