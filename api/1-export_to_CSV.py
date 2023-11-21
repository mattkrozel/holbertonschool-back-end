#!/usr/bin/python3
'''
returns to do list info for specific employee
'''

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
    with open('{}.csv'.format(userId), 'w') as file:
        for task in json_todos:
            file.write('"{}","{}","{}","{}"\n'.format(userId, user, task.get('completed'),
                                                      task.get('title')))
