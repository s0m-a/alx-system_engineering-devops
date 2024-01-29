#!/usr/bin/python3
"""Module with a python script"""
import requests
from sys import argv

if __name__ == "__main__":
    employer_id = int(argv[1])
    empl_name = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                employer_id)).json()["name"]
    todo = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                employer_id)).json()

    tasks = len(todo)
    done = 0

    for i in todo:
        if i["completed"] is True:
            done += 1

    print("Employee {} is done with tasks({}/{}):".format(
        empl_name, done, tasks))
    for i in todo:
        if i["completed"] is True:
            print("\t {}".format(i["title"]))
