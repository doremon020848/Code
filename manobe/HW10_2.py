#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW10_2
# 229223 Sec 001

def main():
    result = eratosthenes(20,True)    
    print('----')
    print(result)
    
def eratosthenes(n, show_step=False):
    
    if show_step == True:
        first = list(range(2, n + 1))
        x = 0
        number = first[x]
    
        while number <= n ** 0.5:
            g1 = list(filter(lambda x: x if x % number != 0 or x // number == 1 else None,first))
            print(str(number) + ':','{}'.format(g1))
            first = g1
            x += 1
            number = first[x]
        
        return g1
        
    else:
        first = list(range(2, n + 1))
        x = 0
        number = first[x]
        
        while number <= n ** 0.5:
            g1 = list(filter(lambda x: x if x % number != 0 or x // number == 1 else None,first))
            first = g1
            x += 1
            number = first[x]
        return g1
            
    
            
if __name__ == '__main__':
    main()


