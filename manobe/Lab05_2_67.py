#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab05_2
# # 229223 Sec 001

def main():
    d1 = str(input("="))
    d2 = str(input("="))
    print(compare_date(d1,d2))

def compare_date(d1,d2):
    mom1 = d1.find("/")
    dad1 = d1.rfind("/")
    
    mom2 = d2.find("/")
    dad2 = d2.rfind("/")
      
    year1 = d1[dad1 + 1:]
    month1 = d1[mom1 + 1:dad1]
    day1 = d1[:mom1]

    year2 = d2[dad2 + 1:]
    month2 = d2[mom2 + 1:dad2]
    day2 = d2[:mom2]

    year11 = int(year1)
    month11 = int(month1)
    day11 = int(day1)

    year22 = int(year2)
    month22 = int(month2)
    day22 = int(day2)

    if year11 < year22 :
       return "-1"
        
    elif year11 > year22:
        return "1"
        
    elif year11 == year22 and month11 < month22:
        return "-1"
        
    elif year11 == year22 and month11 > month22:
        return "1"
        
    elif year11 == year22 and month11 == month22 and day11 < day22:
        return "-1"
        
    elif year11 == year22 and month11 == month22 and day11 > day22:
        return "1"
        
    elif year11 == year22 and month11 == month22 and day11 == day22:
        return "0"
        
if __name__ == "__main__":
    main()