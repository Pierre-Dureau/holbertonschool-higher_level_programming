#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return None
    sum, div = 0, 0
    for tuple in my_list:
        sum += tuple[0] * tuple[1]
        div += tuple[1]
    if div == 0:
        return 0
    else:
        return float(sum / div)
