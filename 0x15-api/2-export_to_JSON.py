#!/usr/bin/python3
"""This is the 2-export_to_JSON  module"""


import json
import requests
from sys import argv


def get_employee_todo_progress(employee_id):
    """ Returns users todolist data """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = "{}/users/{}".format(base_url, employee_id)
    todos_url = "{}/todos?userId={}".format(base_url, employee_id)

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data['name']
        user_name = user_data['username']

        todo_list = []
        for todo in todos_data:
            todo_list.append({
                "task": todo["title"],
                "completed": todo["completed"],
                "username": user_name
                })

        employee_data = {str(employee_id): todo_list}

        json_filename = "{}.json".format(employee_id)
        with open(json_filename, "w") as json_file:
            json.dump(employee_data, json_file, indent=4)
    
    except requests.RequestException as e:
        print("Error fetching data: {e}")


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_todo_progress(employee_id)
