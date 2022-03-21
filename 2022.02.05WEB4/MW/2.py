import argparse

params = argparse.ArgumentParser()
params.add_argument('--per-day', default=[0], nargs=1, type=float)
params.add_argument('--per-week', default=[0], nargs=1, type=float)
params.add_argument('--per-month', default=[0], nargs=1, type=float)
params.add_argument('--per-year', default=[0], nargs=1, type=float)
params.add_argument('--get-by', default='day', choices=['day', 'month', 'year'])
arg = params.parse_args()

result = arg.per_day[0] + arg.per_week[0] / 7 + arg.per_month[0] / 30 + arg.per_year[0] / 360
if arg.get_by == 'day':
    print(int(result))
elif arg.get_by == 'month':
    print(int(result * 30))
else:
    print(int(result * 360))
