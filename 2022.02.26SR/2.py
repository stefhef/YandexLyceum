import csv
import json as js

import requests

with open('tropic.json') as inputfile:
    f = inputfile.read()
    data = js.loads(f)
    host = data['host']
    stage = int(data['stage'])
    stages = [stage + 1, stage, stage - 1]
    port = data['gate']

response = requests.get(f'http://{host}:{port}')
json = response.json()

# with open('tropic.json') as file:
#     f = file.read()
#     json = js.loads(f)
#     stage = 3
#     stages = [stage + 1, stage, stage - 1]


with open('stages.csv', 'w') as outscv:
    file_writer = csv.writer(outscv, delimiter="-")
    file_writer.writerow(['inhabitant', 'meal', 'stage'])
    for st in stages:
        lst = json.get(str(st), None)
        if lst:
            for elem in sorted(set(map(lambda x: (x['inhabitant'], x['meal'], str(st)), lst))):
                file_writer.writerow(elem)
