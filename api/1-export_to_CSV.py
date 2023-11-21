#!/usr/bin/python3
'''
returns to do list info for specific employee
'''

import requests
import sys

def tasks_finished(id):
    '''
    displays employee finished todo
    '''

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id)
    user_response = requests.get(url)
    json_response = user_response.json()
    employee = json_response.get('name')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    todos = requests.get(url)
    json_todos = todos.json()
    num_tasks = len(json_todos)
    finished_task = 0
    task_list = ''
    for task in json_todos:
        if task.get('completed') is True:
            finished_task += 1
            task_list += '\t ' + task.get('title') + '\n'

    print('Employee {} is done with tasks({}/{}):'.format(
        employee, finished_task, num_tasks))
    print(task_list[:-1])

if __name__ == '__main__':
    tasks_finished(sys.argv[1])




