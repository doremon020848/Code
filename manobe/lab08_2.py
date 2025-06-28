#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# lab08_2
# 229223 Sec 001

def main():
    print(reverse_digits(-12345))
      
def reverse_digits(x,y=0):
    if x < 0:
        return -reverse_digits(-x,y)

    if x == 0:
        return y
    y = y * 10 + x % 10
    
    return reverse_digits(x // 10,y)
        
    
        

      

if __name__ == '__main__':
    main()