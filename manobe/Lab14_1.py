#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# Lab14_1
# 229223 Sec 001

def main():
    print(count_segment([(2, 7, 1.5), 
                        (3.2, 2.5, 4.06), 
                        (-5.5, -4.5, 2.5), 
                        (2, -5.2, 3), 
                        (7.2, -2.8, 1.2)] 
                        ))
    
def count_segment(list_a):
    
    q1, q2, q3, q4 = 0, 0, 0, 0

    for f1, f2, g1 in list_a:
        in_q1 = False
        in_q2 = False
        in_q3 = False
        in_q4 = False

        
        if f1 + g1 > 0 and f2 + g1 > 0:
            in_q1 = True
        if f1 - g1 < 0 and f2 + g1 > 0:
            in_q2 = True
        if f1 - g1 < 0 and f2 - g1 < 0:
            in_q3 = True
        if f1 + g1 > 0 and f2 - g1 < 0:
            in_q4 = True

        
        q1 += in_q1
        q2 += in_q2
        q3 += in_q3
        q4 += in_q4

    return (q1, q2, q3, q4)

if __name__ == "__main__":
    main()