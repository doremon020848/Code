#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW09_1
# 229223 Sec 001

def main():
    print(life_path(13092004))
    
def life_path(n):
    if len(str(n)) == 1:
        return n
    if len(str(n)) != 1:
        f1 = n % 10
        f2 = n // 10
        return life_path(f1 + f2)

if __name__ == '__main__':
    main()
    
