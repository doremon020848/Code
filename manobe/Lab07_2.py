#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab07_2
# 229223 Sec 001

import string
 
def main():
    print(uniform('klo KOI 2255'))
    
def uniform(line):
    lower_case = list(filter(lambda x : x in string.ascii_lowercase , line.replace('',' ').split()))
    upper_case = list(filter(lambda x : x in string.ascii_uppercase , line.replace('',' ').split()))

    if len(lower_case) > len(upper_case):
        return line.lower()
        
    elif len(lower_case) < len(upper_case):
        return line.upper()
    
    elif len(lower_case) == len(upper_case):
        if line[0] in string.ascii_uppercase:
            return line.upper()
        else:
            return line.lower()
    
if __name__ == '__main__':
    main()