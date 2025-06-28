#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW03_1
# 229223 Sec 001


def main():
    a = int(input("a:"))
    b = int(input("b:"))
    c = int(input("c:"))
    my_min_mid_max(a, b, c )
    

    
def my_min_mid_max(a, b, c ):
    if a > b:
        max_ = a
        min_ = b
    else:
        max_ = b
        min_ = a
    if c > max_:
        max_ = c
    if c < min_:
        min_ = c
    
    mid_ = (a+b+c) - (min_ + max_)
    print("min = ",min_)
    print("mid = ",mid_)
    print("max = ",max_)



if __name__ == '__main__':

    main()



