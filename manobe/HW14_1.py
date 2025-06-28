#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# HW14_1
# 229223 Sec 001
import math
def main():
    print(reshape([[1, 2],
[1, 2, 3],
[1, 2],
[1, 2],
[1],
[3]]

))

def reshape(matrix):
    
    flat_list = [item for row in matrix for item in row]
    total_elements = len(flat_list)
    
    n = math.ceil(math.sqrt(total_elements))  
    m = math.ceil(total_elements / n)  
           
    matrix.clear()  
   
    for i in range(m):
        new_row = []
        for j in range(n):
            if flat_list:
                new_row.append(flat_list.pop(0))
            else:
                new_row.append(0)  
        matrix.append(new_row)
    
    return matrix
    
if __name__ == "__main__":
    main()