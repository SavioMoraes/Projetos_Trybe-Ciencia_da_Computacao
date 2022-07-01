from src.jobs import read


def get_unique_job_types(path):
    data = read(path)
    job_types = set()
    for job_type in data:
        if job_type["job_type"] != "":
            job_types.add(job_type["job_type"])
    return list(job_types)


def filter_by_job_type(jobs, job_type):
    jobs_type_list = []
    for job in jobs:
        if job["job_type"] == job_type:
            jobs_type_list.append(job)
    return jobs_type_list


# problema com retorno na quantidade de indústrias resolvido na mentoria
# com ajuda do @Carlos


def get_unique_industries(path):
    data = read(path)
    industries = set()
    for industry in data:
        if industry["industry"] != "":
            industries.add(industry["industry"])
    return list(industries)


def filter_by_industry(jobs, industry):
    jobs_industry_list = []
    for job in jobs:
        if job["industry"] == industry:
            jobs_industry_list.append(job)
    return jobs_industry_list


def get_max_salary(path):
    data = read(path)
    max_salary = set()
    for salary in data:
        if salary["max_salary"].isdigit():
            max_salary.add(int(salary["max_salary"]))
    return max(max_salary)


def get_min_salary(path):
    data = read(path)
    min_salary = set()
    for salary in data:
        if salary["min_salary"].isdigit():
            min_salary.add(int(salary["min_salary"]))
    return min(min_salary)


def test_salary(salary):
    if type(salary) != int:
        raise ValueError("ValueError")


def test_min_and_max_salary(job):
    if "min_salary" not in job or "max_salary" not in job:
        raise ValueError("ValueError")
    if type(job["min_salary"]) != int or type(job["max_salary"]) != int:
        raise ValueError("ValueError")
    if job["min_salary"] > job["max_salary"]:
        raise ValueError("ValueError")


# recebi ajuda do @Carlos para entender a lógica do 'lançar um ValueError


def matches_salary_range(job, salary):
    test_min_and_max_salary(job)
    test_salary(salary)
    return salary in range(job["min_salary"], job["max_salary"])


def filter_by_salary_range(jobs, salary):
    jobs_salary_list = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                jobs_salary_list.append(job)
        except ValueError:
            pass
    return jobs_salary_list
