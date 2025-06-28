#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# Lab10_2
# 229223 Sec 001


def main():
    print(comma_separated(1234567,8))
    
    
def comma_separated(n,digit = 3):
     
    f = str(n)[::-1]
    x = []
    
    while len(f) != 0:
            x += [f[:digit]]
            f = f[digit:]
            s1000 = ','.join(x)[::-1]
    print(s1000)

if __name__ == '__main__':
    main()