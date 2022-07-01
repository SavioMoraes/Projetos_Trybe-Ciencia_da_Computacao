from functools import lru_cache
import csv


@lru_cache
def read(path):
    with open(path) as file:
        jobs = csv.DictReader(file)
        jobs_list = list(jobs)
    return jobs_list
    # recebi ajuda do @Felps no retorno da def para transformar em list!
