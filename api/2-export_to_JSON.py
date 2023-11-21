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

    userId = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(userId)
    user_response = get(url)
    user = user_response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(userId)
    todos = get(url)
    json_todos = todos.json()
    dictionary = {userId: []}
    for task in json_todos:
        dictionary[userId].append(
            {'task': task.get('title'),
             'completed': task.get('completed'),
             'username': user}
        )
    with open('{}.json'.format(userId), 'w') as file:
        dump(dictionary, file)
