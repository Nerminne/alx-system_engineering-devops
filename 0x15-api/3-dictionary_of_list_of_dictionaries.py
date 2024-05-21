#!/usr/bin/python3
"""
using jsonplaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


def employee_username(empID):
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
    ids = [1]
    task = []
    x = 0
    for todos in response.json():
        if todos["userId"] != ids[x]:
            x += 1
            ids.append(todos["userId"])
    for todo in response.json():
        task.append({"username": employee_username(todo["userId"]),
                     "task": todo["title"],
                     "completed": todo["completed"]})
        final = {}
    x = 0
    for inf in task:
        if x == (len(ids) - 1):
            final[ids[x]] = inf
            x += 1
    filename = "todo_all_employees.json"
    with open(filename, "w") as f:
        json.dump(final, f)


if __name__ == "__main__":
    all_todo()
