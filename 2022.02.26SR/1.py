import json
import sys

data = {'forest': {},
        'water': {}}

for line in sys.stdin:
    line = line.strip().split('*')
    if line[0] == '2':
        if line[2] not in data['water']:
            data['water'][line[2]] = [line[1]]
        else:
            data['water'][line[2]].append(line[1])
            data['water'][line[2]].sort()

    else:
        if line[2] not in data['forest']:
            data['forest'][line[2]] = [line[1]]
        else:
            data['forest'][line[2]].append(line[1])
            data['forest'][line[2]].sort()

with open('tropical_plants.json', 'w') as outfile:
    json.dump(data, outfile, indent=4)
