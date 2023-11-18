#!/usr/bin/python3
'''
returns to do list info for specific employee
'''
from requests import get
from sys import argv

if __name__ == '__main__':
    id_user = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(id_user)
    reply = get(url)
    name = reply.json().get('name')

    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(id_user)
    reply = get(url)
    jobs = reply.json()
    done = 0
    done_jobs = []
    for job in jobs:
        if job.get('completed'):
            done_jobs.append(job)
            done += 1

    print('Employee {} is done with tasks({}/{}):'
          .format(name, done, len(jobs)))
    for job in done_jobs:
        print('\t {}'.format(job.get('title')))
