#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab04_2
# 229223 Sec 001

# สามารถแก้ไข เพิ่ม ลด function ต่างๆ ได้ตามที่ต้องการ ระบบ grader ตรวจเฉพาะ function is_p_triple()


def main():
    test_p_triple()

# เทียบค่าเลยค้าบทุกคน
def is_p_triple(x, y, z):
    if x**2 == (y**2)+(z**2):
        return True

    elif  y**2 == (x**2)+(z**2):
        return True

    elif  z**2 == (x**2)+(y**2):
        return True
    else:
        return False
        

def test_p_triple():
    assert is_p_triple(4, 5, 3) == True
    assert is_p_triple(42, 9, 41) == False
    print("all ok!")


if __name__ == '__main__':
    main()