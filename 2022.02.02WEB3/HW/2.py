import sys

d = {}
sort = False
for arg in sys.argv[1:]:
    if '=' in arg:
        arg = arg.split('=')
        d[arg[0]] = arg[1]
    else:
        sort = True

d = sorted(d.items()) if sort else d.items()
for key, value in d:
    print(f"Key: {key} Value: {value}")
