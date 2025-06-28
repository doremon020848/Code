#!/usr/bin/env python3
# ธฯธรณ์
# 670510755
# 229223 Sec 001

def main():
   
    print(word_len(['a', 'quick', 'brown', 'fox']))
    

    
def  word_len(list_a):
     list_a1 = list(map(lambda x: len(x),list_a))
     
     del list_a[:]
     list_a += list_a1
     return list_a

   
if __name__ == '__main__':
    main()