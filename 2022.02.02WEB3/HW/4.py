import schedule
import datetime


def q():
    d = datetime.datetime.now()
    i = d.hour % 12 if d.hour % 12 else 12
    print('Ку' * i)


schedule.every().hour.at(":00").do(q)

while True:
    schedule.run_pending()
