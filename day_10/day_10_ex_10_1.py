def is_leap_year(year:int) -> bool:
    cond= not year % 4
    cond = cond and (bool(year % 100))
    cond = cond or not year % 400
    return(cond)


def get_input(msg:str) -> int:
    while 1:
        try:
            a = int(input(msg))
            return(a)
        except ValueError:
            print('Only intger input allowed')


def days_in_month(year:int=2021, month:int=1) -> int:
    month_days = [31, 28, 31, 30, 31, 31, 30, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return(month_days[month-1] + 1)
    else:
        return(month_days[month-1])
    
    
year = get_input('Enter a year: ')
month = get_input('Enter a month: ')
days = days_in_month(year=year,
                     month=month)

print(days)