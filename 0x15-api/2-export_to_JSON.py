#!/usr/bin/python3
"""
export employee data in the JSON format.
"""
import json
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

    """ create empty list"""
    todo = []
    """ create a dictionary"""
    for t in todos_info:
        dict = {}
        dict["task"] = t.get('title')
        dict["completed"] = t.get('completed')
        dict["username"] = user_name
        todo.append(dict)

    """
    create a new dict with the user id as the key
    and the list of dicts as the value
    """
    new_dict = {f"{user_id}": todo}

    """ write the data to a JSON file in JSON format"""
    with open(f"{user_id}.json", mode='w') as new_file:
        json.dump(new_dict, new_file)
