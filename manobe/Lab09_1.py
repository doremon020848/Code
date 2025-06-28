#!/usr/bin/env python3
# Thanathorn chanaphochai
# 670510755
# Lab09_1
# 229223 Sec 001


def main():
    print( is_anagram('heard',
'hrade'))
def  is_anagram(s1, s2):
    f1 = s1.lower().replace(' ','')
    f2 = s2.lower().replace(' ','')
    
    if len(f1) == 0 :
        return True
    
    elif f1[0] not in f2 or len(f1) != len(f2):
        return False
    
    else:
        return is_anagram(f1[1:],f2.replace(f1[0],'',1))
    
    
        

if __name__ == '__main__':
    main()