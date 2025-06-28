#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW05_3
# 229223 Sec 001
    
import string
def main():
    n = str(input("มาดิน้องๆๆๆๆ="))
    print(to_roman_numeral(n))
    
def to_roman_numeral(n):  
    if int(n) <= 4999:
        if len(str(int(n) % 10000)) == 4:
            if str(int(n) % 10000)[0] == "1":
                th = 'M'
            elif str(int(n) % 10000)[0] == "2":
                th = 'MM'
            elif str(int(n) % 10000)[0] == "3":
                th = 'MMM'
            elif str(int(n) % 10000)[0] == "4":
                th = 'MMMM'
        else:
            th = ''
         
        if len(str(int(n) % 1000)) == 3:
                
                if str(int(n) % 1000)[0] == "1":
                    hun = 'C'
                elif str(int(n) % 1000)[0] == "2":
                    hun = 'CC'
                elif str(int(n) % 1000)[0] == "3":
                    hun = 'CCC'
                elif str(int(n) % 1000)[0] == "4":
                    hun = 'CD'
                elif str(int(n) % 1000)[0] == "5":
                    hun = 'D'
                elif str(int(n) % 1000)[0] == "6":
                    hun = 'DC'
                elif str(int(n) % 1000)[0] == "7":
                    hun = 'DCC'
                elif str(int(n) % 1000)[0] == "8":
                    hun = 'DCCC'
                elif str(int(n) % 1000)[0] == "9":
                    hun = 'CM'
        else:
            hun = ''
        if len(str(int(n) % 100)) == 2:
                if str(int(n) % 100)[0] == "0":
                    ten = ''
                elif str(int(n) % 100)[0] == "1":
                    ten = 'X'
                elif str(int(n) % 100)[0] == "2":
                    ten = 'XX'
                elif str(int(n) % 100)[0] == "3":
                    ten = 'XXX'
                elif str(int(n) % 100)[0] == "4":
                    ten = 'XL'
                elif str(int(n) % 100)[0] == "5":
                    ten = 'L'
                elif str(int(n) % 100)[0] == "6":
                    ten = 'LX'
                elif str(int(n) % 100)[0] == "7":
                    ten = 'LXX'
                elif str(int(n) % 100)[0] == "8":
                    ten = 'LXXX'
                elif str(int(n) % 100)[0] == "9":
                    ten = 'XC'
        else:
            ten = ''
        if len(str(int(n) % 10)) == 1:
                if str(int(n) % 10)[0] == "0":
                    u = ''
                elif str(int(n) % 10)[0] == "1":
                    u = 'I'
                elif str(int(n) % 10)[0] == "2":
                    u = 'II'
                elif str(int(n) % 10)[0] == "3":
                    u = 'III'
                elif str(int(n) % 10)[0] == "4":
                    u = 'IV'
                elif str(int(n) % 10)[0] == "5":
                    u = 'V'
                elif str(int(n) % 10)[0] == "6":
                    u = 'VI'
                elif str(int(n) % 10)[0] == "7":
                    u = 'VII'
                elif str(int(n) % 10)[0] == "8":
                    u = 'VIII'
                elif str(int(n) % 10)[0] == "9":
                    u = 'IX'
        else:
            u = ''
        
    return th +''+ hun +''+ ten +''+ u    
                  
if __name__ == "__main__":
    main()