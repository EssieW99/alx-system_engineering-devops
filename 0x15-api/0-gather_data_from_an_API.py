#!/usr/bin/python3
"""
uses a REAST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys


if __name__ == "__main__":
    employee_id = sys.argv[1]
    todos_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    users_endpoint = 'https://jsonplaceholder.typicode.com/users'

    user_specs = {"id": employee_id}
    todos_specs = {"userId": employee_id}

    user_info = requests.get(users_endpoint, params=user_specs).json()
    employee_name = user_info[0].get('name')

    todos_info = requests.get(todos_endpoint, params=todos_specs).json()

    len_comp_tasks = 0
    comp_tasks = []
    for t in todos_info:
        if t.get('completed') is True:
            comp_tasks.append(t.get('title'))
            len_comp_tasks += 1

    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, len_comp_tasks, len(todos_info)))
    for title in comp_tasks:
        print(f"\t {title}")
