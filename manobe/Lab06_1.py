#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab06_1
# 229223 Sec 001

def main():
    n = int(input("ว่าใดครับน้องๆ="))
    print(triangle(n))
    
    
    
def triangle(n):
    if n >= 3:
        a = list(range(1, n - 1))
        b = list(map(lambda x:  ('*.' + ('..' * int(x - 1) ) +'*' +'\n' ), a))
        c = (['*' + '\n'] + b + ["* " * n + '\n'] )
        
        result = ''.join(c)
        return result

                
if __name__ == "__main__":
    main()