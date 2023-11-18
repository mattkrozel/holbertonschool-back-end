#!/usr/bin/python3
'''
returns to do list info for specific employee
'''
import csv
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
    tasks = []
    usersname = userInfo['username']
    for task in todoInfo:
        task_dict = {}
        task_dict['USER_ID'] = userId
        task_dict['USERNAME'] = usersname
        task_dict['TASK_COMPLETED_STATUS'] = task['completed']
        task_dict['TASK_TITLE'] = task['title']
        tasks.append(task_dict)

    names = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    with open('./{}.csv'.format(userId), 'w', encoding='UTF8',
              newline='') as f:
        writer = csv.Dictwriter(f, names=names,
                                quoting=csv.QUOTE_ALL, quotechar='"')
        writer.writerows(tasks)