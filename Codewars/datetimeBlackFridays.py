from datetime import date

def unlucky_days(year):
    return len([i for i in range(1, 13) if date(year, i, 13).weekday() == 4])

print(unlucky_days(2015))