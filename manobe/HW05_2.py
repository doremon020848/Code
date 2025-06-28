#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW05_2
# 229223 Sec 001

import string

def main():
    name = str(input("มาดิน้องๆๆๆๆ="))
    print(transform_name(name))
    
def transform_name(name):
    strip = name.strip()
    find = strip.find(' ')
    front = strip[:find]
    black = strip[find + 1:]
    len_front = len(front)
    len_black = len(black)
    
    
    if len_black <= 9 :
        wow = (9 - len_black) + 5
        return  string.capwords(black) +'.'+ string.capwords(front[:wow])
        
    elif len_front <= 5 :
        wow = (5 - len_front) + 9
        return  string.capwords(black[:wow]) +'.'+ string.capwords(front)
    
    elif len_black >= 9 or len_front >= 5 :
        return string.capwords(black[:9]) +'.'+ string.capwords(front[:5])
       
    
    
if __name__ == "__main__":
    main()
            
            
        
        
            
            
    
    
            
            
            
            
            
    
