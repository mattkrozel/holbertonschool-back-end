#!/usr/bin/python3
'''
returns to do list info for specific employee
'''

from json import dump
from requests import get
from sys import argv


if __name__ == '__main__':
    '''
    displays employee finished todo
    '''

    url = 'https://jsonplaceholder.typicode.com/users/'
    user_response = get(url)
    users = user_response.json()

    dictionary = {}
    for user in users:
        userId = user.get('id')
        userName = user.get('username')
        url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
        url = url + '/todos/'
        reply = get(url)
        jobs = reply.json()
        dictionary[userId] = []
        for task in tasks:
            dictionary[userId].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': userName
            })
    with open('todo_all_employees.json', 'w') as file:
        dump(dictionary, file)
