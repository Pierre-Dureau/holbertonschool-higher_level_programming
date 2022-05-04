#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0
    sum, div = 0, 0
    for tuple in my_list:
        sum += tuple[0] * tuple[1]
        div += tuple[1]
    return float(sum / div)
