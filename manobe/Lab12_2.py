#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# Lab12_2
# 229223 Sec 001

def main():
    print( matching_sum((10, -1, 1, -8, 3, 1), 2))
    
def matching_sum(t, target_value):
    
    set_ = set()  
    for num in t:
       
        if target_value - num in set_:
            return [target_value - num, num]
        
        set_.add(num)
    return []
            
if __name__ == '__main__':
    main()                    