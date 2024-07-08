def is_leap(year):
    if year%4==0:
        if year%100==0:
            if year%400==0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(month, year):
    month_days = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year) == True:  # you can also remove the ==True
        return 29
    else:
        return month_days[month - 1]


year = int(input("enter a year"))
month = int(input("enter a month"))
if month < 13:
    is_leap(year)
    days = days_in_month(month, year)
    print(days)
else:
    print("enter a valid month")