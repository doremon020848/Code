#!/usr/bin/env python3
# thanathorn chanaphochai benz
# 670510755
# HW02_3
# 229223 Sec 001


def main():
    n = int(input())
    k = int(input())
    v = int(input())
    g = kth_digit(n,k)
    volume = set_kth_digit(n,k,v,g)
    print(volume)
    
    test_set_kth_digit()
    
# สร้างสมาการ คำนวนลงในฟังชั่น

def kth_digit(n, k):
    return (abs(n) //  (10 ** k)) % 10

def set_kth_digit(g,n,k,v):
    z = g * (10 ** k)
    z1 = v * (10 ** k)
    z2 = (abs(n) - z)
    z3 = z1 +z2
    return z3
    
def test_set_kth_digit():
    assert set_kth_digit(2343, 2, 7) == 2743
    assert set_kth_digit(51, 0, 2) == 52
    assert set_kth_digit(1, 2, 5) == 501
    assert set_kth_digit(-2343, 2, 7) == 2743
    print("all ok")

if __name__ == '__main__':
    main()

