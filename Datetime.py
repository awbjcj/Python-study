import re
from datetime import datetime, timezone, timedelta
def to_timestamp(dt_str, tz_str):
    inputT = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    timeZ = re.match(r'UTC([+-]\d+):00',tz_str).group(1)
    zoneT = inputT.replace(tzinfo = timezone(timedelta(hours = int(timeZ))))
    return zoneT.timestamp()
# 测试:
t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

t2 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
assert t2 == 1433121030.0, t2

print('ok')