import argparse

params = argparse.ArgumentParser()
params.add_argument('--sort', default=None, action="store_true")
params.add_argument('params', nargs="+")

args = params.parse_args()

data = {}

for elem in args.params:
    k_v = elem.split("=")
    data[k_v[0]] = k_v[1]
# data = list(map(lambda x: x.split("="), args.params))

data = sorted(data.items(), key=lambda x: x[0]) if args.sort else data.items()

for key, value in data:
    print(f"Key: {key}  Value: {value}")
