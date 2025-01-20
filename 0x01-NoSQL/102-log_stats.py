#!/usr/bin/env python3

"""12-logs_stats"""

from pymongo import MongoClient
from collections import Counter


if __name__ == "__main__":
    """returns the logs of nginx stats stored in mongodb
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    collection = client.logs.nginx
    print("{} logs".format(collection.count_documents({})))
    print("Methods:")
    for i in method:
        result = collection.count_documents({ "method" : i })
        print("    method {}: {}".format(i, result))
    stats = collection.count_documents({"method" : "GET", "path" : "/status"})
    print("{} status check".format(stats))
    print("IPs:")
    ips = collection.find({"ip": {"$exists": True}}, { "ip": 1, "_id": 0 })
    ip_list = [doc["ip"] for doc in ips]
    ip_counts = Counter(ip_list)
    for key, value in ip_counts.most_common(10):
        print("    {}: {}".format(key, value))

