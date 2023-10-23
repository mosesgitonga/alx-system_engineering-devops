#!/usr/bin/env python3
"""
a Python script that, using this REST API, for a given 
employee ID, returns information about his/her TO DO list progress.
"""
import requests
response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
data = response.json()
print(data)