import csv
from functools import lru_cache
from typing import List, Dict


@lru_cache
def read(path: str) -> List[Dict]:
    with open(file=path, mode='r', newline="", encoding="utf-8") as file:
        content = csv.reader(file, delimiter=",", quotechar='"')
        header, *data = content

        response = []
        newDict = {}

        for line in data:
            for i, key in enumerate(header):
                newDict[key] = line[i]
            response.append(newDict)
            newDict = {}
    return response


def get_unique_job_types(path: str) -> List[str]:
    response = set()

    jobs = read(path)

    for job in jobs:
        response.add(job["job_type"])

    return response


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    return [job for job in jobs if (job["job_type"] == job_type)]
