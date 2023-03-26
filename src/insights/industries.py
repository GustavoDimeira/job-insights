from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    response = set()

    for job in read(path):
        if (job["industry"] != ""):
            response.add(job["industry"])

    return response


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    return [job for job in jobs if (job["industry"] == industry)]
