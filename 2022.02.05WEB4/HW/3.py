import argparse
import os


def main(args):
    if not args.file:
        return print("ERROR")
    if not os.path.exists(args.file[0]):
        return print("ERROR")

    with open(args.file[0]) as file:
        data = file.read().split("\n")

    if args.sort:
        data.sort()
    if args.num:
        data = list(map(lambda x: f"{x[0]} {x[1]}", enumerate(data)))

    print("\n".join(data))

    if args.count:
        print(f"rows count: {len(data)}")


params = argparse.ArgumentParser()
params.add_argument('file', default=None, nargs='*')
params.add_argument('--count', default=None, action="store_true")
params.add_argument('--num', default=None, action="store_true")
params.add_argument('--sort', default=None, action="store_true")

args = params.parse_args()

main(args)
