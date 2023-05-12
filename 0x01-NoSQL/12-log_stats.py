#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def print_nginx_stat():
    """Prints some stats about Nginx stored in MongoDB"""
    client = MongoClient()
    db = client.logs
    nginx = db.nginx

    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    print('{} logs'.format(nginx.count_documents({})))
    print('Methods:')

    for method in methods:
        method_count = nginx.count_documents({ 'method': method })
        print('    method {}: {}'.format(method, method_count))

    print('{} status check'.format(nginx.count_documents(
        {
            'method': 'GET',
            'path': '/status'
        }
    )))


if __name__ == '__main__':
    print_nginx_stat()
