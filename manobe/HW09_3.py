#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW09_3
# 229223 Sec 001


def main():
    print(left_max([3, 3, 1, 1, 2, 4]  ))
    
def left_max(list_a, n=1, one=0 ,two=1 , x=1):
    
    if n == len(list_a):
        return list_a
    
    else:
        if list_a[one] < list_a[two]:
            f1 = list_a[two]
        
        else:
            f1 = list_a[one]
    
    g1 = list_a[:x] + [f1] + list_a[x+1:]
    
        
    return left_max(g1, n + 1, one + 1 , two + 1, x+1)
    
    
if __name__ == '__main__':
    main()
