#!/usr/bin/env python3
# ธฯธรณ์
# 670510755
# 229223 Sec 001

def main():
   
    print(cumulative_sum_of_sq([1, 2, 3, 4] ))
    

    
def cumulative_sum_of_sq(list_a): 
    return list(map(lambda x: sum(list(map(lambda y: y ** 2,x))),list(map(lambda x: list_a[:x],list(range(1,len(list_a) + 1))))))



   
if __name__ == '__main__':
    main()