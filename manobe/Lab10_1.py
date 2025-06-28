#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# Lab10_1
# 229223 Sec 001

def main():
    print(bean_count(99))

def bean_count(n):
    if n <= 0:
        return 0
    
    if n < 100:
        g1 = n // 10
        g2 = n % 10
        g3 = (g1 * 4) + g2
        return g3
    
    while n >= 100:
        f1 =  n % 100
        return (f1 // 10) * 4 + (f1 % 10)

    
if __name__ == '__main__':
    main()
    