#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 670510755
# Lab12_1
# 229223 Sec 001


def main():
    print(multiply_polynomials([2, 3, 4, 5], [1, 2, 1]) )
    
def multiply_polynomials(p1, p2):
    
    len_wow = (len(p1) + len(p2)) - 1
    zero = [0] * len_wow
    
    # print(zero)
    
    for i in range(len(p1)):
        for j in range(len(p2)):
            zero[i + j] += p1[i] * p2[j]
            

    return zero
    
            
if __name__ == '__main__':
    main()                    