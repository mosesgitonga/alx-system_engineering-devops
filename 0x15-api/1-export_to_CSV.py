#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given
employee ID, returns information about his/her TO DO list progress.
"""
if __name__ == '__main__':
    import requests
    import sys

    employeeID = sys.argv[1]

    base_url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(base_url)
    url = base_url + '/' + employeeID
    response = requests.get(url)
    username = response.json().get('username')
    employeeName = response.json().get('name')

    todo_url = url + '/todos'
    response = requests.get(todo_url)
    tasks = response.json()

    done_tasks = []
    num_of_done_tasks = 0
    with open('{}.csv'.format(employeeID), 'w') as file:
        for task in tasks:
            file.write('"{}","{}","{}","{}"\n'.format(
                employeeID,
                username,
                task.get('completed'),
                task.get('title')))
