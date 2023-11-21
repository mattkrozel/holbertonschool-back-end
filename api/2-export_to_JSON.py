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

    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = get(url)
    user = user_response.json().get('username')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    todos = get(url)
    json_todos = todos.json()
    dictionary = {user_id: []}
    for task in json_todos:
        dictionary[user_id].append(
            {'task': task.get('title'),
             'completed': task.get('completed'),
             'username': user})
    with open('{}.json'.format(user_id), 'w') as file:
        dump(dictionary, file)
