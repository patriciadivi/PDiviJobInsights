from functools import lru_cache
import csv

@lru_cache
def read(pathParams):
    with open(pathParams, encoding="utf-8") as fileParamns:
        readData = csv.DictReader(fileParamns, delimiter=",", quotechar='"')
        data = list(readData)
    return data

# print(read("src/jobs.csv")[5])
