#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW04_2
# # 229223 Sec 001

def main():
    # num = int(input(""))
    # pos = int(input(""))
    test_rotate()
    # print(rotate(num, pos))
    
def rotate(num, pos):
    num1 = str(num)

    if pos >= 0:
        mom = num1[(-1)*pos % len(num1):]
        dad = num1[:(-1)*pos % len(num1)]
        son = mom +""+ dad
        return int(son)
    
    elif pos < 0:
        dad = num1[:((-1) * pos) % len(num1) ]
        mom = num1[((-1)*pos) % len(num1):]
        son = mom +""+ dad
        return int(son)
    
def test_rotate():
        assert rotate(12345, 9) == 23451
        assert rotate(12345, 8 ) == 34512
        assert rotate(12345, 7) == 45123
        assert rotate(12345, 6) == 51234
        assert rotate(12345, 5) == 12345
        assert rotate(12345, 4) == 23451
        assert rotate(12345, 3) == 34512
        assert rotate(12345, 2) == 45123
        assert rotate(12345, 1) == 51234
        assert rotate(12345, 0) == 12345
        assert rotate(12345, -1) == 23451
        assert rotate(12345, -2) == 34512
        assert rotate(12345, -3) == 45123
        assert rotate(12345, -4) == 51234
        assert rotate(12345, -5) == 12345
        assert rotate(12345, -6) == 23451
        assert rotate(12345, -7) == 34512
        assert rotate(12345, -8) == 45123
        assert rotate(12345, -9) == 51234
        print("mom")


    

if __name__ == '__main__':
    main()
