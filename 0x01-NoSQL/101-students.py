#!/usr/bin/env python3

"""101-studenets"""

def top_students(mongo_collection):
    """return studenst that meet higher than average score
    Args:
        mongo_collection: collection
    Return: students sorted by average score
    """

    students = mongo_collection.find()
    for student in students:
        topics = student.get('topics', [])
        if topics:
            total_score = sum(topic['score'] for topic in topics)
            average = total_score / len(topics)
        else:
            average = 0
        mongo_collection.update_one({"_id": student["_id"]}, {"$set": {"averageScore": average}})
    all_student = mongo_collection.find({}).sort({"averageScore": -1})
    if all_student:
        return all_student
    return []
