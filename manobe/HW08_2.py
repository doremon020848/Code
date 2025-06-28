#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 670510755
# HW08_2
# 229223 Sec 001


def main():
    print(base_b(11,3))

def base_b(x, b):
        if x == 0:
            return 0
        f2 = x % b
        f1 = base_b(x // b,b)
        return  f1 * 10 + f2

if __name__ == '__main__':
    main()
