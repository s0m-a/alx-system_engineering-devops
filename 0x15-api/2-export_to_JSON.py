#!/usr/bin/python3
"""Module with a python script"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    empId = int(argv[1])
    emp = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}".format(
                empId)).json()
    empUsrname = emp["username"]
    todo = requests.get(
            "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                empId)).json()

    with open("{}.json".format(empId), "w", newline="") as jsonFile:
        empList = []
        for i in todo:
            empList.append(
                    {"task": i["title"],
                        "completed": i["completed"],
                        "username": empUsrname})
        empDict = {empId: empList}
        json.dump(empDict, jsonFile)
