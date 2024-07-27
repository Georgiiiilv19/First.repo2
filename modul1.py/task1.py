from datetime import datetime

nbm = datetime(year=2022, month=9, day=18) 
current_date = datetime.now()

days_since = current_date.toordinal() - nbm.toordinal()
print(days_since)
