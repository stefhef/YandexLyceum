import argparse


params = argparse.ArgumentParser()
params.add_argument('--upper', default=None, action="store_true")
params.add_argument('--lines', type=int, default=None)
params.add_argument('source', nargs=1, type=str)
params.add_argument('destination', nargs=1, type=str)

args = params.parse_args()
with open(args.source[0], 'r', encoding='utf-8') as file:
    data = file.read().split('\n')
    if args.lines:
        data = data[:args.lines]
    if args.upper:
        data = tuple(map(str.upper, data))

with open(args.destination[0], 'w', encoding='utf-8') as file:
    file.write('\n'.join(data))
    print('ok')
