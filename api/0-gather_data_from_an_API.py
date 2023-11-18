#!/usr/bin/python3
'''
returns to do list info for specific employee
'''
import json
import requests
from sys import argv

if __name__ == '__main__':
    numdone, numtasks = 0, 0
    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    user_response = requests.get(url)
    url = 'https://jsonplaceholder.typicode.com/todos/?userId={}'\
        .format(userId)
    todo_response = requests.get(url)
    userInfo = json.loads(user_response.text)
    todoInfo = json.loads(todo_response.text)
    employeeName = userInfo['name']
    for task in todoInfo:
        numtasks += 1
        if task['completed']:
            numdone += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(employeeName, numdone, numtasks))
    for task in todoInfo:
        if task['completed']:
            print('\t {}'.format(task['title']))
