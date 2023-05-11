#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


client = MongoClient()
db = client.logs
nginx = db.nginx

log_count = nginx.count_documents({})
get_method_count = nginx.count_documents({ 'method': 'GET' })
post_method_count = nginx.count_documents({ 'method': 'POST' })
put_method_count = nginx.count_documents({ 'method': 'PUT' })
patch_method_count = nginx.count_documents({ 'method': 'PATCH' })
delete_method_count = nginx.count_documents({ 'method': 'DELETE' })

get_root_count = nginx.count_documents({ 'method': 'GET', 'path': '/status' })


def print_nginx_stat():
    """Prints some stats about Nginx stored in MongoDB"""
    print('{} logs'.format(log_count))
    print('Methods:')
    print('    Method GET: {}'.format(get_method_count))
    print('    Method POST: {}'.format(post_method_count))
    print('    Method PUT: {}'.format(put_method_count))
    print('    Method PATCH: {}'.format(patch_method_count))
    print('    Method DELETE: {}'.format(delete_method_count))
    print('{} status check'.format(get_root_count))


if __name__ == '__main__':
    print_nginx_stat()
