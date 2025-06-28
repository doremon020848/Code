#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW06_2
# 229223 Sec 001

def main():
    dest_rotate_list()
    
    
def dest_rotate_list(list_a, n):
    if n > 0:
        len_ = len(list_a)
        mod = n % len_
        find1 = list_a[:len_ - mod]
        del list_a[:len_ - mod]
        list_a.extend(find1)

    elif n < 0:
        len_ = len(list_a)
        mod = abs(n) % len_
        find1 = list_a[:mod]
        del list_a[:mod]
        list_a.extend(find1)
    
    
if __name__ == '__main__':
    main()