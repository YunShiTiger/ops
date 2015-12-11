import sys
import re

def get_upstream():
    file_object = open('hosts.conf')
    try:
        ng_conf = file_object.read()
    finally:
        file_object.close()

    data = ng_conf.split("\n")
    objs = []
    obj = None
    xs = []
    for line in data:
        line = line.strip()
        if ('d_platform' in line):
            if (obj is not None):
                objs.append(obj)
                obj is None
            obj = {}
            continue

        if (obj is None):
            continue

        kv = line.split(':')

        if (len(kv) is not 2 ):
            break

        x = {}
        x['ip'] = kv[0].split(' ')[1]
        x['port'] = kv[1].split(' ')[0]

        xs.append(x)


    if (obj is not None):
        objs.append(obj)
        obj is None

    return xs

for i in  get_upstream():
    print i['ip'] + ":" + i['port']
