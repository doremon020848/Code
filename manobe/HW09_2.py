#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW09_2
# 229223 Sec 001

def main():
    n = 1171777332 
    print(longest_digit_run(n))
    
    
def longest_digit_run(n, sos=None, wow=0,count=0):
    f = str(n)
    if len(f) == 0:
        return count
    
    index_one = f[0]

    if index_one == sos:
        wow += 1
        
    else:
        count = max(count, wow)
        sos = index_one
        wow = 1

    return longest_digit_run(f[1:], sos, wow, max(count, wow))


if __name__ == '__main__':
    main()