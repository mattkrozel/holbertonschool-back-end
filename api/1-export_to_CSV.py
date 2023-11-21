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
    employee = json_response('name')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id)
    todos = requests.get(url)
    json_todos = todos.json()
    num_tasks = len(json_todos)
    finished_task = 0
    task_list = ''
    fileName = '{}.csv'.format(id)
    with open(fileName, 'a') as fd:
        for todo in json_todos:
            finished = todo.get('completed')
            title = todo.get('title')
            csv = '\'{}\',\'{}\',\'{}\',\'{}\'\n'.format(
                id, employee, finished, title)
            fd.write(csv)

if __name__ == '__main__':
    tasks_finished(sys.argv[1])
