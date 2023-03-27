from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)

    maxSalary = None

    for job in jobs:
        salary = job["max_salary"]
        if (salary and (not maxSalary or int(salary) > maxSalary)):
            maxSalary = int(salary)

    return maxSalary


def get_min_salary(path: str) -> int:
    jobs = read(path)

    minSalary = None

    for job in jobs:
        salary = job["min_salary"]
        if (salary and (not minSalary or int(salary) < minSalary)):
            minSalary = int(salary)

    return minSalary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    maxSalary = job["max_salary"]
    minSalary = job["min_salary"]
    if (not maxSalary or not minSalary or minSalary > maxSalary):
        raise ValueError

    return (maxSalary >= salary and minSalary >= salary)


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
