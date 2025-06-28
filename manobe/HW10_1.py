#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# HW10_1
# 229223 Sec 001


def main():
    print(float_to_base_b(44.1875, 16))
    
def float_to_base_b(x, b):
    
    x1 = abs(x)

    
    if int(x1) != 0:
        honda = int(x1) # ton
        digit = []
        while honda != 0:
            
            
            if (honda % b) < 10:
                digit += [str(honda % b)]
                honda = honda // b
            elif (honda % b) == 10 :
                digit += ['A']
                honda = honda // b
            elif (honda % b) == 11:
                digit += ['B']
                honda = honda // b
            elif (honda % b) == 12:
                digit += ['C']
                honda = honda // b
            elif (honda % b) == 13 :
                digit += ['D']
                honda = honda // b
            elif (honda % b) == 14:
                digit += ['E']
                honda = honda // b
            elif honda % b == 15 :
                digit += ['F']
                honda = honda // b
                
            v = ''.join(digit[::-1])
                
        wave = x1 % int(x1) # pai
        number = []
        
        while len(number) != 6:
            
            if (wave * b) < 1:
                number += [str(int(wave * b))]
                wave = wave * b
                
            else:
                if (wave * b) < 10:
                    number += [str(int(wave * b))]
                    wave = (wave * b) % int(wave * b)
                
                elif (wave * b) >= 10 and (wave * b) < 11:
                    number += ['A']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 11 and (wave * b) < 12:
                    number += ['B']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 12 and (wave * b) < 13:
                    number += ['C']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 13 and (wave * b) < 14:
                    number += ['D']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 14 and (wave * b) < 15:
                    number += ['E']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 15 and (wave * b) < 16:
                    number += ['F']
                    wave = (wave * b) % int(wave * b)
                
        n = ''.join(number)
        
    else:
        
        wave = x1  # pai
        number = []
        
        while len(number) != 6:
            
            if (wave * b) < 1:
                number += [str(int(wave * b))]
                wave = wave * b
                
                
            
            else:
                if (wave * b) < 10:
                    number += [str(int(wave * b))]
                    wave = (wave * b) % int(wave * b)
                
                elif (wave * b) >= 10 and (wave * b) < 11:
                    number += ['A']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 11 and (wave * b) < 12:
                    number += ['B']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 12 and (wave * b) < 13:
                    number += ['C']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 13 and (wave * b) < 14:
                    number += ['D']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 14 and (wave * b) < 15:
                    number += ['E']
                    wave = (wave * b) % int(wave * b)
                    
                elif (wave * b) >= 15 and (wave * b) < 16:
                    number += ['F']
                    wave = (wave * b) % int(wave * b)
                
                
        v = '0' 
        n = ''.join(number)
    s1000 = v + '.' + n
    
    
    if x < 0:
        s1000 = '-' + v + '.' + n
    
        
    return s1000
    
    
if __name__ == '__main__':
    main()