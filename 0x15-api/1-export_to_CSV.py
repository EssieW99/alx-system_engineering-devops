#!/usr/bin/python3
"""
export data in the CSV format.
"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    todos_endpoint = 'https://jsonplaceholder.typicode.com/todos'
    users_endpoint = 'https://jsonplaceholder.typicode.com/users'

    user_specs = {"id": user_id}
    todos_specs = {"userId": user_id}

    user_info = requests.get(users_endpoint, params=user_specs).json()
    user_name = user_info[0].get('username')

    todos_info = requests.get(todos_endpoint, params=todos_specs).json()

    with open(f"{user_id}.csv", "w") as new_file:
        user = csv.writer(new_file, quoting=csv.QUOTE_ALL)

        for t in todos_info:
            user.writerow([user_id, user_name, t.get('completed'),
                           t.get('title')])
