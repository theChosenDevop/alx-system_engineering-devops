#!/usr/bin/python3
"""This is the 1-export_to_CSV module"""


import csv
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
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task['completed'])

        csv_filename = "{}.csv".format(employee_id)
        with open(csv_filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            for todo in todos_data:
                emp_id = '{}'.format(employee_id)
                username = '{}'.format(user_name)
                task_completed = '{}'.format(todo["completed"])
                task_title = '{}'.format(todo["title"])
                csv_writer.writerow(
                        [emp_id, username, task_completed, task_title]
                        )

    except requests.RequestException as e:
        print("Error fetching data: {e}")


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_todo_progress(employee_id)
