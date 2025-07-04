#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 670510755
# HW11_3
# 229223 Sec 001


def main():
    print(words_to_num('forty two billion six hundred forty one million three hundred twenty three thousand eight hundred sixty two'))     # 42641323862
    
def words_to_num(words):
    num_words = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
        'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
        'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13, 'fourteen': 14,
        'fifteen': 15, 'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
        'twenty': 20, 'thirty': 30, 'forty': 40, 'fifty': 50,
        'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
        'hundred': 100, 'thousand': 1000, 'million': 1000000, 'billion': 1000000000
    }
    
    yoi = words.replace('-',' ').split()
    l1 = []
    
    for i in yoi:
        l1 += [num_words[i]]
    
    result = 0
    current = 0 
    
    for i in l1:
        if i == 100:  
                current *= i
        elif i == 1000 or i == 1000000 or i == 1000000000:  
            result += current * i
            current = 0
        else:
            current += i
    result += current   
    return result
    
    
if __name__ == '__main__':
    main()                    