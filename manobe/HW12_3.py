#!/usr/bin/env python3
# ธนธรณ์
# 670510755
# HW12_3
# 229223 Sec 001

def main():
    print(subset_sum({1,2,3}))
    
def subset_sum(set_a):
    
    list_a = list(set_a)
    honda = test(list_a)
    
    aws = []
    for i in honda:
        aws += [sum(i)]
    return aws  

def test(set):
    
        wow = [[]]  
        for i in set:
            wow += [j + [i] for j in wow]
        return wow
    
if __name__ == '__main__':
    main()             