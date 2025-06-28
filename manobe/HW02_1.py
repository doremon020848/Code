#!/usr/bin/env python3
# thanathorn chanaphochai benz
# 670510755
# Lab02_2
# 229223 Sec 00B

def main():
     x = float(input("ส่งค่ามาเลยจ้า: "))
     octagon_area(x)
     y = octagon_area(x)
     print("octagon = %.2f"%(y))
     test_octagon_area()
 



# สร้างสมาการใส่ฟังชั่น
def octagon_area(x):
    square_area = (x ** 2)
    triangle_area = ((1/2 * ((x/3) * (x/3) ))) * 4
    a = (square_area - triangle_area)
    return a

#test ครับๆ
def test_octagon_area():
    assert octagon_area(9) == 63.00
    print("All OK!")



if __name__ == '__main__':
    main()

