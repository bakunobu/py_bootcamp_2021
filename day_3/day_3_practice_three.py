def is_leap_year(year:int) -> bool:
    cond= not year % 4
    cond = cond and (bool(year % 100))
    cond = cond or not year % 400
    return(cond)


for year in (2100, 1900, 1999, 2000, 2004):
    print(f'{year} is leap: {is_leap_year(year)}') 