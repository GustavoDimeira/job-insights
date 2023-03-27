from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)

    maxSalary = None

    for job in jobs:
        if (job["max_salary"] and (not maxSalary or int(job["max_salary"]) > maxSalary)):
            maxSalary = int(job["max_salary"])

    return maxSalary


def get_min_salary(path: str) -> int:
    jobs = read(path)

    minSalary = None
    
    for job in jobs:
        if (job["min_salary"] and (not minSalary or int(job["min_salary"]) < minSalary)):
            minSalary = int(job["min_salary"])

    return minSalary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if (not job["max_salary"] or not job["min_salary"] or job["min_salary"] > job["max_salary"]):
        raise ValueError

    return (job["max_salary"] >= salary and job["min_salary"] >= salary)


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError

