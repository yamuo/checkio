import datetime

def days_diff(date1, date2):
    date1_date = datetime.datetime(date1[0],date1[1],date1[2])
    date2_date = datetime.datetime(date2[0],date2[1],date2[2])
    td = date2_date - date1_date
    return abs(td.days)

print(days_diff((1982, 4, 19), (1982, 4, 22)))