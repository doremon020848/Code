#!/usr/bin/env python3
# Thanathorn chanaphochai  
# 670510755
# Lab09_2
# 229223 Sec 001 

def main():
    print(sum_prime_in_range(3, 20))

def sum_prime_in_range(x, y):
    
    f = list(range(x,y + 1))
    f1 = list(filter(lambda x: x if is_prime(x) == True else None,f))
    return sum(f1)
    
def is_prime(n, div=2):
    if n <= 1:
        return False  
    if div > n ** 0.5:
        return True 
    if n % div == 0:
        return False  
    return is_prime(n, div + 1)  

if __name__ == '__main__':
    main()