#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab05_2
# 229223 Sec 001

def main():
    d1 = str(input())
    d2 = str(input())
    x = compare_date(d1,d2)
    print(x)

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

    if int(year1) == int(year2) :
        if int(month1) == int(month2):
            if int(day1) == int(day2):
                return 0
            elif int(day1) < int(day2):
                return -1
            else:
                return 1
        elif int(month1) < int(month2):
            return -1
        else:
            return 1
    else:
        if int(year1) < int(year2):
            return -1
        else:
            return 1
    
if __name__ == "__main__":
    main()