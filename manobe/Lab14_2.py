#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# Lab14_2
# 229223 Sec 001

def main():
    print(remove_row_col([[2, 3, 4, 5],
[8, 7, 6, 5],
[0, 1, 2, 3]],
    1,
    -3))
    
    
def remove_row_col(list_a, row, col):
    if 0 <= row < len(list_a):
        list_a = list_a[:row] + list_a[row + 1:]
    
    if len(list_a) > 0 and 0 <= col < len(list_a[0]):
        list_a = [r[:col] + r[col + 1:] for r in list_a]
    
    return list_a
    
if __name__ == "__main__":
    main()