#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW04_2
# 229223 Sec 001

def main():
    hour1 = int(input())
    min1 = int(input())
    period1 = str(input())
    hour2 = int(input())
    min2 = int(input())
    period2 = str(input())
    mom = min_diff(hour1, min1, period1, hour2, min2, period2)
    print(mom)
    test_min_diff()


# implement this function
def min_diff(hour1, min1, period1, hour2, min2, period2):
# กรณี เวลาที่ period1 เป็น 12 หรือไม่เท่ากับ 12   
    if period1 == "AM" and hour1 == 12:
      hour1 = 0
    elif period1 == "PM" and hour1 != 12:
        hour1 += 12
    mom = (hour1 * 60) + min1
# กรณี เวลาที่ period2 เป็น 12 หรือไม่เท่ากับ 12   
    if period2 == "AM" and hour2 == 12:
      hour2 = 0
    elif period2 == "PM" and hour2 != 12:
        hour2 += 12
    dad = (hour2 * 60) + min2
# คืนค่าที่ได้
    sis = abs(mom - dad)

    return sis
    
    
        
# test function
def test_min_diff():
    assert(min_diff(8, 23, "AM", 8, 24, "AM")) == 1
    assert(min_diff(8, 23, "AM", 1, 24, "PM")) == 301
    assert(min_diff(1, 24, "PM", 8, 23, "AM")) == 301
    assert(min_diff(2, 39, "AM", 12, 26, "PM")) == 587


if __name__ == "__main__":
    main()



