import argparse

params = argparse.ArgumentParser()

params.add_argument('a', nargs='*', default=['no args'])

args = params.parse_args()
for elem in args.a:
    print(elem)