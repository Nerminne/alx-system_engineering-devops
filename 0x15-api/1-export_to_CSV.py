#!/usr/bin/python3
"""
using jsonplaceholder REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import csv
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


def csv_converter():
    """convert dictionary to csv file"""
    url = "https://jsonplaceholder.typicode.com/todos?userId=" + argv[1]
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        name = employee_username()
        formatted_inf = []
        for inf in data:
            formatted_inf.append([argv[1], name, inf["completed"],
                                  inf["title"]])
        filename = f"{argv[1]}.csv"
        with open(filename, "w") as f:
            write = csv.writer(f, quoting=csv.QUOTE_ALL)
            write.writerows(formatted_inf)


if __name__ == "__main__":
    csv_converter()
