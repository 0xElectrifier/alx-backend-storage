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


def nginx_req_stat():
    """Prints some stats about Nginx stored in MongoDB"""
    print('{} logs'.format(log_count))
    print('Methods:')
    print('    method GET: {}'.format(get_method_count))
    print('    method POST: {}'.format(post_method_count))
    print('    method PUT: {}'.format(put_method_count))
    print('    method PATCH: {}'.format(patch_method_count))
    print('    method DELETE: {}'.format(delete_method_count))
    print('{} status check'.format(get_root_count))


def nginx_ip_stat():
    """Prints some stats about Nginx stored in MongoDB"""
    ips = nginx.aggregate([
        {
            '$group':
            {
                '_id': '$ip',
                'count': { '$sum': 1 }
            }
        },
        {
            '$sort': { 'ip': -1 }
        }
    ])
    print('IPs:')
    for ip in ips:
        print('{}: {}'.format(ip.get('ip'), ip.get('count')))


if __name__ == '__main__':
    nginx_req_stat()
    nginx_ip_stat()
