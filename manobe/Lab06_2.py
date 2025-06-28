#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab06_2
# 229223 Sec 001

def main():
    list_x = [10, 'hello', 23.5, 4]
    print(classify(list_x))
   
    
def classify(list_x):
    
    str1 = list(filter(lambda x: isinstance(x, str) ,list_x))
    int1 = list(filter(lambda x: isinstance(x, int) ,list_x))
    float1 = list(filter(lambda x: isinstance(x, float) ,list_x))
    
    return int1,float1,str1
    
 
if __name__ == "__main__":
    main()