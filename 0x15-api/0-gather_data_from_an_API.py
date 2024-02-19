#!/usr/bin/python3
"""This is the 0-gather_data_from_an_API module"""
import requests
from sys import argv


def get_employee_task_done(employee_id):
    """Returns user TODO list data."""
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        total_tasks = len(todos_data)
        done_tasks = sum(1 for task in todos_data if task["completed"])

        print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                              done_tasks,
                                                              total_tasks
                                                              ))
        for task in todos_data:
            if task["completed"]:
                print(f"\t {task['title']}")

    except requests.RequestException as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    employee_id = argv[1]
    get_employee_task_done(employee_id)
