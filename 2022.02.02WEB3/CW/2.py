import sys

if len(sys.argv) == 3:
    try:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(a + b)
    except ValueError:
        print(0)
else:
    print(0)

