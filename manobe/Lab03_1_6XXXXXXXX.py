#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab04_1
# 229223 Sec 001

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function circle_intersect()

import math
def main():
    test_circle_intersect()
    # circle_intersect(x1, y1, r1, x2, y2, r2, epsilon)
    

def circle_intersect(x1, y1, r1, x2, y2, r2, epsilon = 10 ** -6):
    mom = ((((x1 - x2) ** 2) + ((y1 - y2) ** 2))**0.5) 
    wow = (r1 + r2)
    dis = mom - wow

    if  dis < 0:
        return 1
    elif dis <= epsilon:
        return 0
    else:
        return -1

def test_circle_intersect():
    assert circle_intersect(2, 3, 5, 5, 7, 1) == 1
    assert circle_intersect(0, 0, 2.5, 3, 4, 2.5) == 0
    assert circle_intersect(1, 1, 5, 6, 17, 7) == -1

    # now using specified epsilon
    assert circle_intersect(2, 3, 5, 5, 7, 1, epsilon=1.5) == 0
    print("all ok!")
    
    
if __name__ == '__main__':
    main()


    # if distance(x1, y1, r1, x2, y2, r2)  <= 0 or distance(x1, y1, r1, x2, y2, r2) == 0:
    #     print("1")
    # elif distance(x1, y1, r1, x2, y2, r2)  < epsilon  or distance(x1, y1, r1, x2, y2, r2)  == epsilon:
    #     print("0")
    # else:
    #     print("-1")

    



    