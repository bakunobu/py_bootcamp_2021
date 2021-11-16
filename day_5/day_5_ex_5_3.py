def even_sum(start:int=1, end:int=100) -> None:
    total = 0
    if start % 2:
        start += 1
    for i in range(start, end+1, 2):
        total += i
    return(total)

print(even_sum())