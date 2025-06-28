#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab04_2
# 229223 Sec 001

def main():
    print(zodiac_element(2022))

def  zodiac_element(year):
     
# หาหมีเเพนด้า
    if int(year) % 2 == 0:
        mom = "Yang"
    elif int(year) % 2 != 0 :
        mom = "Yin"

#เหล็ก ธาตุ มีประโยชน์   
    year1 = str(year)

    if  year1[-1] == '2' or  year1[-1] == '3' :
        dad = "Water"
    
    elif  year1[-1] == '4' or  year1[-1] == '5' :
        dad = "Wood"
    
    elif  year1[-1] == '6' or  year1[-1] == '7' :
        dad = "Fire"
    
    elif  year1[-1] == '8' or  year1[-1] == '9' :
        dad = "Earth"
    
    elif  year1[-1] == '0' or  year1[-1] == '1' :
        dad = "Metal"

    

# ราศรี มีบังเกิด

    f = (year - 1992) % 12
    if f == 0:
        bro = "Monkey"
    elif f == 1:
        bro = "Rooster"
    elif f == 2:
       bro = "Dog"
    elif f == 3:
       bro = "Pig"
    elif f == 4:
       bro = "Rat"
    elif f == 5:
       bro = "Ox"
    elif f ==6:
       bro = "Tiger"
    elif f ==7:
       bro = "Rabbit"
    elif f ==8:
      bro = "Dragon"
    elif f ==9:
      bro = "Snake"
    elif f ==10:
      bro = "Horse"
    elif f ==11:
      bro = "Goat"


    aa = mom +" "+ dad +" "+ bro
    return aa

if __name__ =="__main__": 
    main()