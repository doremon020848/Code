#!/usr/bin/env python3
# ธฯธรณ์
# 670510755
# 229223 Sec 001

def main():
   
    print(max_len_of_2(['i', 'bought', 'me', 'a', 'boat'],
    ['a', 'man', 'and', 'a', 'dog']))
    

    
def max_len_of_2(list_a, list_b):
    return list(map(lambda x,y: x if len(x) >= len(y) else y, list_a,list_b))
   
if __name__ == '__main__':
    main()