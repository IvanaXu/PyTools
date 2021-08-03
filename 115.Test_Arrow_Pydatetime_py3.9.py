#
import sys
if sys.version.startswith("3.9"):
    from zoneinfo import ZoneInfo
    from datetime import datetime
    dt = datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
    print(dt)
else:
    print("Error")
