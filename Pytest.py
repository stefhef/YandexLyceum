from datetime import datetime, timezone, timedelta

import pytz
dt = datetime.now(timezone(timedelta(hours=3)))
print(dt.strftime('%d.%m.%Y %H:%M:%S %A'))
pytz.timezone('Europe/Moscow')
