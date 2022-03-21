import argparse


def main(numbers):
    if not numbers:
        print("NO PARAMS")
        return
    if len(numbers) == 1:
        print("TOO FEW PARAMS")
        return
    if len(numbers) > 2:
        print("TOO MANY PARAMS")
        return
    try:
        print(sum(map(int, numbers)))
    except BaseException as e:
        print(e.__class__.__name__)


params = argparse.ArgumentParser()
params.add_argument('numbers', default=None, nargs='*')

args = params.parse_args()

main(args.numbers)
