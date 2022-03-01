import schedule
import datetime
from typing import Union


def q(word: str, time_n: Union[list[int, int], tuple[int, int]]):
    d = datetime.datetime.now()
    if time_n[0] <= d.hour <= time_n[1]:
        return
    i = d.hour % 12 if d.hour % 12 else 12
    print(word * i)


time_n = tuple(map(int, input().split('-')))
schedule.every().hour.at(":00").do(q(input(), time_n))

while True:
    schedule.run_pending()
