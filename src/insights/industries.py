from typing import List, Dict
from jobs import read


def get_unique_industries(path: str) -> List[str]:
    response = set()

    jobs = read(path)

    for job in jobs:
        if (job["industry"] != ""):
            response.add(job["industry"])

    return response
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
