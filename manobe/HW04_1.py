#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW04_1
# 229223 Sec 001
import string

def main():

    text = str(input(""))
    c = str(input(""))
    dad = palindrome_without(text, c)
    print(dad)
    # test_palindromee_without()

def palindrome_without(text, c):
# ทำให้เป็นพิมเล็ก
    mom = str.lower(text)
# ลบค่า c ออก
    sis = mom.replace(c, '',)
# ลบ space ออก
    dad = sis.replace(' ','')
# เเล้วก็รีคับ
    bro = dad[::-1] 
    

    if bro == '':
        return False
        
    elif bro == dad:
        return True
        
    else:
        return False
        
    

        
    # if bro == ' ':
    #     return False
    
    # elif (c not in mom) and (bro == sis) :
    #     return True
    
    # elif c not in mom:
    #     return False
        
    # elif bro != ' ':
    #     bro == sis
    #     return True
        
    # elif bro != ' ':
    #     sis != sis
    #     return False
        
    
def test_palindromee_without():
    assert palindrome_without("Banana") == True
    assert palindrome_without("Swap of paws") == True
    assert palindrome_without("T") == False


if __name__ =="__main__": 
    main()