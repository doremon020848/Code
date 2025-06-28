#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW04_3
# 229223 Sec 001

import string

def main():
    text = str(input(""))
    old = str(input(""))
    new = str(input(""))
    print(substitute_once(text, old, new))

def substitute_once(text, old, new):

    if old in text:

        if len(old) == 1:
            mom = text.find(old)
            sis = text[:mom]
            dad = text[mom+1:]
            nin = sis +''+ new +''+ dad
                
            return nin

        elif len(old) > 1:
            mom = text.find(old)
            sis = text[:mom]
            dad = text[mom+len(old):]
            nin = sis +''+ new +''+ dad
            
            return nin
            
    else:
        return text




if __name__ == '__main__':
    main()

# txt = "battle"

# x = txt.find("tle")

# print(x)

# txt = "Hello, welcome to my world."

# x = txt.find("e", 5, 10)

# print(x)
