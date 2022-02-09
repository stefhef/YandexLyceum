import sys


if len(sys.argv) == 1:
    print('NO PARAMS')
else:
    try:
        numbers = list(map(int, sys.argv[1:]))
        print(sum(numbers[::2]) - sum(numbers[1::2]))
    except BaseException as e:
        print(e.__class__.__name__)
