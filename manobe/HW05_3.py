#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW05_3
# 229223 Sec 001
    

def main():
    n = str(input("มาดิน้องๆๆๆๆ="))
    print(to_roman_numeral(n))
    
def to_roman_numeral(n):  
      
    if len(n) ==4 and int(n[0]) <= 4:   
        thon = int(n[0]) *'M'  
        if  n[1] == "4":
            hun = "CD"
        elif n[1] == "9":
                    hun = "CM"
        elif n[1] == "1":
                    hun = "C"
        elif n[1] == "2":
                    hun = "CC"
        elif n[1] == "3":
                    hun = "CCC"
        elif n[1] == "5":
                    hun = "D"
        elif n[1] == "6":
                    hun = "DC"
        elif n[1] == "7":
                    hun = "DCC"
        elif n[1] == "8":
                    hun = "DCCC"
        elif n[1] == "0":
                    hun = ''
        if  n[2] == "4":
                        ten = "XL"
        elif n[2] == "9":
                        ten = "XD"
        elif n[2] == "1":
                        ten = "X"
        elif n[2] == "2":
                        ten = "XX"
        elif n[2] == "3":
                        ten = "XXX"
        elif n[2] == "5":
                        ten = "L"
        elif n[2] == "6":
                        ten = "LX"
        elif n[2] == "7":
                        ten = "LXX"
        elif n[2] == "8":
                        ten = "LXXX" 
        elif n[2] == "0":
                        ten = ''
        if  n[3] == "4":
                            unint = "IV"
        elif n[3] == "9":
                            unint = "IX"
        elif n[3] == "1":
                            unint = "I"
        elif n[3] == "2":
                            unint = "II"
        elif n[3] == "3":
                            unint = "III"
        elif n[3] == "5":
                            unint = "V"
        elif n[3] == "6":
                            unint = "VI"
        elif n[3] == "7":
                            unint = "VII"
        elif n[3] == "8":
                        unint = "VIII"
        elif n[3] == "0":
                        unint = ''
        return thon +''+ hun +''+ ten +''+ unint 
    
    elif len(n) == 3:
        if  n[0] == "4":
            hun = "CD"
        elif n[0] == "9":
                    hun = "CM"
        elif n[0] == "1":
                    hun = "C"
        elif n[0] == "2":
                    hun = "CC"
        elif n[0] == "3":
                    hun = "CCC"
        elif n[0] == "5":
                    hun = "D"
        elif n[0] == "6":
                    hun = "DC"
        elif n[0] == "7":
                    hun = "DCC"
        elif n[0] == "8":
                    hun = "DCCC"
        elif n[0] == "0":
                    hun = ''
        if  n[1] == "4":
                        ten = "XL"
        elif n[1] == "9":
                        ten = "XD"
        elif n[1] == "1":
                        ten = "X"
        elif n[1] == "2":
                        ten = "XX"
        elif n[1] == "3":
                        ten = "XXX"
        elif n[1] == "5":
                        ten = "L"
        elif n[1] == "6":
                        ten = "LX"
        elif n[1] == "7":
                        ten = "LXX"
        elif n[1] == "8":
                        ten = "LXXX" 
        elif n[1] == "0":
                        ten = ''
        if  n[2] == "4":
                            unint = "IV"
        elif n[2] == "9":
                            unint = "IX"
        elif n[2] == "1":
                            unint = "I"
        elif n[2] == "2":
                            unint = "II"
        elif n[2] == "3":
                            unint = "III"
        elif n[2] == "5":
                            unint = "V"
        elif n[2] == "6":
                            unint = "VI"
        elif n[2] == "7":
                            unint = "VII"
        elif n[2] == "8":
                        unint = "VIII"
        elif n[2] == "0":
                        unint = ''
        return hun +''+ ten +''+ unint
    
    elif len(n) == 2:
        if  n[0] == "4":
                        ten = "XL"
        elif n[0] == "9":
                        ten = "XD"
        elif n[0] == "1":
                        ten = "X"
        elif n[0] == "2":
                        ten = "XX"
        elif n[0] == "3":
                        ten = "XXX"
        elif n[0] == "5":
                        ten = "L"
        elif n[0] == "6":
                        ten = "LX"
        elif n[0] == "7":
                        ten = "LXX"
        elif n[0] == "8":
                        ten = "LXXX" 
        elif n[0] == "0":
                        ten = ''
        if n[1] == "4":
                            unint = "IV"
        elif n[1] == "9":
                            unint = "IX"
        elif n[1] == "1":
                            unint = "I"
        elif n[1] == "2":
                            unint = "II"
        elif n[1] == "3":
                            unint = "III"
        elif n[1] == "5":
                            unint = "V"
        elif n[1] == "6":
                            unint = "VI"
        elif n[1] == "7":
                            unint = "VII"
        elif n[1] == "8":
                        unint = "VIII"
        elif n[1] == "0":
                        unint = ''
        return ten +''+ unint
                        
    elif len(n) == 1:
        if  n[0] == "4":
                            unint = "IV"
        elif n[0] == "9":
                            unint = "IX"
        elif n[0] == "1":
                            unint = "I"
        elif n[0] == "2":
                            unint = "II"
        elif n[0] == "3":
                            unint = "III"
        elif n[0] == "5":
                            unint = "V"
        elif n[0] == "6":
                            unint = "VI"
        elif n[0] == "7":
                            unint = "VII"
        elif n[0] == "8":
                        unint = "VIII"
        elif n[0] == "0":
                        unint = ''
        return unint
    
if __name__ == "__main__":
    main()