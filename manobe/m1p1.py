#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# Sec001


def main():

    assert is_isosceles(3, 3, 3) == True
    assert is_isosceles(5, 5, 4) == True
    assert is_isosceles(7, 8, 9) == False
    assert is_isosceles(6, 10, 12) == False

    print("All tests passed!")


def is_isosceles(a, b, c):
    if a == b or a == c or b == c:
        return True
    else:
        return False


if __name__ == '__main__':
    main()
