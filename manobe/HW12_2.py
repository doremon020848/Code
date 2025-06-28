#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# HW12_2
# 229223 Sec 001



def main():
    print(median_of_median( [28, 14,  13,  21,  19,  27,  23,  30, 
16]))
    
def quickselect(lst, k):
    
    if len(lst) == 1:
        return lst[0]

    pivot = lst[len(lst) // 2]
    lows = [x for x in lst if x < pivot]
    highs = [x for x in lst if x > pivot]
    pivots = [x for x in lst if x == pivot]

    if k < len(lows):
        return quickselect(lows, k)
    elif k < len(lows) + len(pivots):
        return pivots[0]
    else:
        return quickselect(highs, k - len(lows) - len(pivots))

def median_of_median(lst):
    if len(lst) <= 2:
     
        return quickselect(lst, len(lst) // 2)

  
    sublists = [lst[i:i + 5] for i in range(0, len(lst), 5)]


    medians = [quickselect(sublist, len(sublist) // 2) for sublist in sublists]

  
    return median_of_median(medians)

    
if __name__ == '__main__':
    main()             