#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW06_3
# 229223 Sec 001

def main():
    list_a = [1,2,3,4,5]
    w = 2
    print(moving_average(list_a, w))
    
def moving_average(list_a, w):
    if w <= len(list_a):
        r = list(range(0,((len(list_a) + 1) - w )))
        wow = list(map(lambda x: list_a[x:w + x],r))
        uwu = list(map(lambda x: sum(x) / w  ,wow))
        return uwu
    
if __name__ == '__main__':
    main()