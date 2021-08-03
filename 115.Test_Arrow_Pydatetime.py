#
import arrow
import datetime
from dateutil.relativedelta import relativedelta

utc1 = arrow.utcnow()
print(
    f"\nNow:\n {utc1} \nUS/Pacific: {utc1.to('US/Pacific')}"
    
    f"\nAdd 1 hours:\n {utc1 + datetime.timedelta(hours=1)}"
    f"\nAdd 1 hours:\n {utc1.shift(hours=1)}"
    
    f"\nAdd 1 days:\n {utc1 + datetime.timedelta(days=1)}"
    f"\nAdd 1 days:\n {utc1 + relativedelta(days=1)}"
    f"\nAdd 1 days:\n {utc1.shift(days=1)}"
    
    f"\nAdd 1 months:\n {utc1 + relativedelta(months=1)}"
    f"\nAdd 1 months:\n {utc1.shift(months=1)}"
)

utc2 = datetime.datetime.utcnow()
print(
    f"\nNow:\n {utc2}"
    
    f"\nAdd 1 hours:\n {utc2 + datetime.timedelta(hours=1)}"
    
    f"\nAdd 1 days:\n {utc2 + datetime.timedelta(days=1)}"
    f"\nAdd 1 days:\n {utc2 + relativedelta(days=1)}"
    
    f"\nAdd 1 months:\n {utc2 + relativedelta(months=1)}"
)
