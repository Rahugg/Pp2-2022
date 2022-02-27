import datetime as dt

a = dt.datetime(2013,12,30,23,59,59)
b = dt.datetime(2013,12,31,23,59,59)

(b-a).total_seconds()