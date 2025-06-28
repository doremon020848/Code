#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW05_1
# 229223 Sec 001
import string

def main():

    license_str = str(input("ไอ้เเดงมันเป็นนักสู้=")) 
    x = is_valid_license(license_str)
    print(x)
    
def is_valid_license(license_str):
    
    find_1 = license_str[0]
    find_2 = license_str[1:3]
    find_3 = license_str[3:]
    wow1 = license_str[1:2]
    wow2 = license_str[2:3]
    
    find_4 = license_str[:2]
    find_5 = license_str[2:]
    wow3 = license_str[:1]
    wow4 = license_str[1:2]

    mom = string.ascii_uppercase
    
    k = ((wow1 and wow2) in mom) and 1 <= len(find_3) <= 4
    m = ((wow3 and wow4) in mom) and 1 <= len(find_5) <= 4
    
    
    
    if 8 > len(license_str) >= 1 :
        if find_1 in string.digits :
            if find_2.isalpha() and k:
                if find_3.isdigit():
                    return True
                else:
                    return False
            else:
                return False
        elif find_1 not in string.digits :
            
            if find_4.isalpha() and m:
                if find_5.isdigit():
                    return True
                else:
                    return False
            else:
                return False           
    elif len(license_str) > 7:
        return False

if __name__ == "__main__":
    main()