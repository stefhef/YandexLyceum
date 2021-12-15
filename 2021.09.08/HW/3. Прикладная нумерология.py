def add_zero(st: str) -> str:
    return st.rjust(2, '0')


hours = sorted(list(map(add_zero, input().strip().split())))
minutes = sorted(list(map(add_zero, input().strip().split())))

for hour in hours:
    for minute in minutes:
        if sum(map(int, list(hour))) != sum(map(int, list(minute))):
            print(f'{hour}:{minute}')
