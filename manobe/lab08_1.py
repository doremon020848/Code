#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# lab08_1
# 229223 Sec 001
def main():
    print(gcd(200,50))
    # print(recursive_gcd(-39, 78))
    
def gcd(x, y):
    
        if y == 0:
            return abs(x)
        else:
            return gcd(y, x % y)
        
   
if __name__ == '__main__':
    main()
 