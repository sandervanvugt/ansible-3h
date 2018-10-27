#!/usr/bin/python

from subprocess import Popen,PIPE
import sys

try:
     import json
except ImportError:
     import simplejson as json



result = {}

result['all'] = {}



pipe = Popen(['getent', 'hosts'], stdout=PIPE, universal_newlines=True)


result['all']['hosts'] = []

for line in pipe.stdout.readlines():
    s = line.split()
    result['all']['hosts']=result['all']['hosts']+s


result['all']['vars'] = {}


if len(sys.argv) == 2 and sys.argv[1] == '--list':
    print(json.dumps(result))

elif len(sys.argv) == 3 and sys.argv[1] == '--host':
    print(json.dumps({}))

else:
    print("Requires an argument, please use --list or --host <host>")
