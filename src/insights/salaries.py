from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)

    max_salary = None

    for job in jobs:
        salary = job["max_salary"]
        if (salary and (not max_salary or max_salary < int(salary))):
            try:
                max_salary = int(salary)
            except ValueError:
                print('a')

    return max_salary


def get_min_salary(path: str) -> int:
    jobs = read(path)

    min_salary = None

    for job in jobs:
        salary = job["min_salary"]
        if (salary and (not min_salary or min_salary > int(salary))):
            try:
                min_salary = int(salary)
            except ValueError:
                print('Invalid value')

    return min_salary


def str_to_int(input):
    if (type(input) == int or (type(input) == str and input.isnumeric())):
        return int(input)
    raise ValueError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if ("max_salary" not in job) or ("min_salary" not in job):
        raise ValueError

    maxSalary = str_to_int(job["max_salary"])
    minSalary = str_to_int(job["min_salary"])
    salary = str_to_int(salary)
    if (minSalary > maxSalary):
        raise ValueError

    return (maxSalary >= salary and minSalary <= salary)


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

