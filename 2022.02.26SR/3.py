import sys
import requests
import json as js
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("ip", nargs=1)
parser.add_argument("port", nargs=1)
parser.add_argument("colors", nargs='*')
parser.add_argument("--length", type=int, nargs=1, default=[1])
parser.add_argument("--size", type=int, nargs=1, default=[20])
args = parser.parse_args()


# json = ''
data = dict()
length = args.length[0]
size = args.size[0]
colors = args.colors

response = requests.get(f'http://{args.ip[0]}:{args.port[0]}')
json = response.json()

for d in json:
    color = d['color']
    if color not in colors and int(d['size']) <= size and len(d['name']) >= length:
        if color not in data:
            data[color] = [d['name']]
        else:
            data[color].append(d['name'])
            data[color].sort()

with open('hummingbirds.json', 'w') as outfile:
    js.dump(data, outfile, indent=4)
