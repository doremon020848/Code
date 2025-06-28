#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 6XXXXXXXX
# HW08_1
# 229223 Sec 00?1

from math import isclose


def main():
    print(pi(3))
    # pass


def pi(n,x=2,y=2):
    if n == 0:
        return 3
    f1 = -(4/(x * (x + 1) * (x + 2))) * ((-1) ** y)
    f2 = pi(n - 1,x + 2,y + 1) 
    return f2,f1

 
def test_pi():
    epsilon = 10**-10
    assert isclose(pi(0), 3, abs_tol=epsilon)
    assert isclose(pi(1), 3.1666666666666665, abs_tol=epsilon)
    assert isclose(pi(2), 3.1333333333333333, abs_tol=epsilon)
    assert isclose(pi(5), 3.1427128427128426, abs_tol=epsilon)
    print("All OK!")


if __name__ == '__main__':
    main()

