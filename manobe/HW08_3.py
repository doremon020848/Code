#!/usr/bin/env python3
# ชื่อ นามสกุล ชื่อเล่น
# 670510755
# HW08_3
# 229223 Sec 001






def main():
    print(patterned_message("ab**c14d*",'''
****** ** *
* **** *** 
*       ** *
		********
'''))


def patterned_message(message,pattern,ans=''):
    f1 = message.replace(' ','')
    if len(pattern) != 0:
        if pattern[0] == '*':
            f2 = f1[0]
            f3 = patterned_message(f1[1:] + f1[0],pattern[1:],f2)
        elif pattern[0] == ' ':
            f2 = ' '
            f3 = patterned_message(f1,pattern[1:],f2)
        else:
            f2 = '\n'
            f3 = patterned_message(f1,pattern[1:],f2)
        return ans + f3
    else:
        return ans 

        

if __name__ == '__main__':
    main()
 