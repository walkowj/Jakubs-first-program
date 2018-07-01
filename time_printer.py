from datetime import datetime, timedelta
import pytz

eastern = pytz.timezone('Australia/Sydney')
loc_dt = eastern.localize(datetime.now() - timedelta(days=3472))

samoa = pytz.timezone('Pacific/Samoa')
samoa_dt = loc_dt.astimezone(samoa)

warsaw = pytz.timezone('Europe/Warsaw')
warsaw_dt = loc_dt.astimezone(warsaw)

phili = pytz.timezone('US/Eastern')
phili_dt = loc_dt.astimezone(phili)

format = '%Y-%m-%d %I:%M:%S %p %A'
print("Sydney time ziomeczki:")
print(loc_dt.strftime(format))
print("Warsaw time:")
print(warsaw_dt.strftime(format))
print("Phili time:")
print(phili_dt.strftime(format))
