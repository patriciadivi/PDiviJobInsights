from src.jobs import read as readData


def get_unique_job_types(path):
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    result = readData(path)
    resultJobType = list()

    for each_line in result:
        if each_line["job_type"] != "":
            resultJobType.append(each_line["job_type"])
    JobTypeCorrect = list(set(resultJobType))
    return JobTypeCorrect


def filter_by_job_type(jobs, job_type):
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
    resultJobType = list(job for job in jobs if job["job_type"] == job_type)
    return resultJobType


def get_unique_industries(path):
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

    result = readData(path)
    listIndustry = list()
    # set = para tirar os valores repetidos
    listIndustryNotDuplicates = set()

    for each_line in result:
        if each_line['industry'] != "":
            listIndustry.append(each_line['industry'])

    for each_element in listIndustry:
        if each_element != "":
            listIndustryNotDuplicates.add(each_element)
    return listIndustryNotDuplicates


def filter_by_industry(jobs, industry):
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
    return []


def get_max_salary(path):
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    # Tentando
    result = readData(path)
    resultMaxSalary = list()

    for each_element in result:
        if each_element["max_salary"].isnumeric():
            resultMaxSalary.append(int(each_element["max_salary"]))

    sortedNumbers = sorted(resultMaxSalary)
    maxSalary = sortedNumbers[::-1][0]

    return maxSalary


def get_min_salary(path):
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    result = readData(path)
    resultMaxSalary = list()

    for each_element in result:
        if each_element["min_salary"].isnumeric():
            resultMaxSalary.append(int(each_element["min_salary"]))

    minSalary = sorted(resultMaxSalary)

    return minSalary[0]


def matches_salary_range(job, salary):
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    pass


def filter_by_salary_range(jobs, salary):
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
    return []
