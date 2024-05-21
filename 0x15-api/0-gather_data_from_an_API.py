#!/usr/bin/python3
"""
using jsonplaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

from sys import argv
import requests


def employee_username():
    """finding username of employee"""
    url = "https://jsonplaceholder.typicode.com/users/" + argv[1]
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if "name" in data:
            return data["name"]


def todos():
    """getting todos of employee"""
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    response = requests.get(url)
    complete = 0
    not_completed = 0
    emp_todos = []
    if response.status_code == 200:
        data = response.json()
        for todos in data:
            if todos["completed"] == True:
                complete += 1
                emp_todos.append(todos["title"])
            else:
                not_completed += 1
        name = employee_username()
        total = complete + not_completed
        print("Employee {} is done with tasks({}/{}):".format(name, complete,
                                                              total))
        for todo in emp_todos:
            print(todo)


if __name__ == "__main__":
    todos()
