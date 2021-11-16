def calc_aver_heigth(heigths:list) -> float:
    """
    return(sum(heigth) / len(heigth))
    """
    i = 0
    tot_heigth = 0
    for h in heigths:
        tot_heigth += h
        i += 1
    return(round(tot_heigth / i, 2))


