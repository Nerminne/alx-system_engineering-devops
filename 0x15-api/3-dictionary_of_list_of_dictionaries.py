#!/usr/bin/python3
"""
using jsonplaceholder REST API, for a given employee ID
returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


def username(empID):
    """finding username of employee"""
    url = "https://jsonplaceholder.typicode.com/users/" + str(empID)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "name" in data:
            return data["username"]


def all_todo():
    """adding all users inf to json"""
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    final = {}
    for todo in response.json():
        if todo["userId"] not in final:
            final[todo["userId"]] = []
        final[todo["userId"]].append({"username": usrname(todo["userId"]),
                                      "task": todo["title"],
                                      "completed": todo["completed"]})
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(final, f)


if __name__ == "__main__":
    all_todo()
