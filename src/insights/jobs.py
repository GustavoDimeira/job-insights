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
    reponse = set()

    jobs = read(path)

    for job in jobs:
        reponse.add(job["job_type"])

    print(reponse)


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
