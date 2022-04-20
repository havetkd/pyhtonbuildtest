from datetime import datetime
from dateutil.relativedelta import relativedelta
now = datetime.now()
before_one_year = now - relativedelta(years=6)
date = before_one_year.strftime('%Y-%m-%d')
print(date)