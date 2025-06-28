#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW03_3
# 229223 Sec 001

def main():
    l1 = float(input())
    t1 = float(input())
    w1 = float(input())
    h1 = float(input())
    l2 = float(input())
    t2 = float(input())
    w2 = float(input())
    h2 = float(input())
    sis = is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2)
    print(sis)
    test_is_overlapped()


def is_overlapped(l1, t1, w1, h1, l2, t2, w2, h2):

   if ((t1 + h1) < (t2) ) or (( t1) > (t2 + h2 )) :
       return False
   elif (l1 + w1) < (l2) or  (l1) > (l2 + w2) :
       return False
   else:
       return True
   


def test_is_overlapped():
    assert(is_overlapped(10, 10, 50, 75, 30, 55, 60, 60)) == True
    assert(is_overlapped(10, 10, 50, 75, 70, 55, 60, 60)) == False

if __name__ =="__main__":
    main()