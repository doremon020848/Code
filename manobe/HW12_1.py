#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# HW12_1
# 229223 Sec 001

def main():
    print(nth_term(1))
    
def nth_term(n):
    
    wow = ['6', '7']
    
    count = 0
    
    for i in range(n + count):
            
        honda = wow[count]
        count += 1
        
        if count == n:
            return int(honda)
            
        wow.append(honda + '6')
        wow.append(honda + '7')

if __name__ == '__main__':
    main()             