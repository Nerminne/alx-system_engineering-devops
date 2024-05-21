#!/usr/bin/python3
"""
using jsonplaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import json
import requests
from sys import argv


def employee_username():
    """finding username of employee"""
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "name" in data:
            return data["username"]


def to_json():
    """convert to json"""
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    response = requests.get(url)
    if response.status_code == 200:
        task = []
        for todo in response.json():
            task.append({"task": todo["title"],
                         "completed": todo["completed"],
                         "username": employee_username()})
        filename = f"{argv[1]}.json"
        inf = {argv[1]: task}
        with open(filename, "w") as f:
            json.dump(inf, f)


if __name__ == "__main__":
    to_json()
