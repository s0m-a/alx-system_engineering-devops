#!/usr/bin/python3
"""Module with a python script"""
import json
import requests

if __name__ == "__main__":
    employ = requests.get(
            "https://jsonplaceholder.typicode.com/users").json()

    with open("todo_all_employees.json", "w", newline="") as jsonFile:
        empDict = {}
        for i in employ:
            empId = i["id"]
            empUsrname = i["username"]
            url = "https://jsonplaceholder.typicode.com/users/{}/todos".format(
                            empId)
            todo = requests.get(url).json()

            empList = []
            for x in todo:
                empList.append(
                        {
                            "username": empUsrname,
                            "task": x["title"],
                            "completed": x["completed"]})
            empDict[empId] = empList
        json.dump(empDict, jsonFile)
