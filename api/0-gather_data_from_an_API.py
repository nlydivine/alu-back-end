#!/usr/bin/python3
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]

    # Fetch user
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
    user = requests.get(user_url).json()

    # Fetch todos
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)
    todos = requests.get(todos_url).json()

    employee_name = user.get("name")

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title")))

