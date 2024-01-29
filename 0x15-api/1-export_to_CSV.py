#!/usr/bin/python3
"""Module with a python script"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    empl_id = int(argv[1])
    empl = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                empl_id)).json()
    empl_username = empl["username"]
    todo = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                empl_id)).json()

    with open("{}.csv".format(empl_id), "w", newline="") as CFile:
        for i in todo:
            var = [empl_id, empl_username, i["completed"], i["title"]]
            csvW = csv.writer(
                    cFile, delimiter=',',
                    quote='"', quoting=csv.QUOTE_ALL)
            csvW.writerow(var)
