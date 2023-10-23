#!/usr/bin/python3
"""
a Python script that, using this REST API, for a given 
employee ID, returns information about his/her TO DO list progress.
"""
import requests
import sys

employeeID = sys.argv[1]

base_url = 'https://jsonplaceholder.typicode.com/users'
url = base_url + '/' + employeeID
response = requests.get(url)
employeeName = response.json().get('name')

todo_url = url + '/todos'
response = requests.get(todo_url)
tasks = response.json()

done_tasks = []
num_of_done_tasks = 0

for task in tasks:
    if task.get('completed'):
        done_tasks.append(task)
        num_of_done_tasks += 1
print('Employee {} is done with tasks({}/{}):'.format(employeeName, num_of_done_tasks,len(tasks)))

for task in done_tasks:
    print('\t {}'.format(task.get('title')))
