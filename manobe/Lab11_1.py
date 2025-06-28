#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 670510755
# Lab11_1
# 229223 Sec 001


import sys
import string
def main():
    text = input_data()
    # word_count()
    print(word_count(text))
 
def input_data():
    
    text = ""
    for line in sys.stdin:
        text += line 
    
    return text


def word_count(text):
    text1 = text.lower().split()
    text2 = list(map(lambda x: x.strip(string.punctuation),text1))
    gg = {}
    for i in text2:
        gg[i] = text2.count(i)
    return gg
    
    
    
    
if __name__ == '__main__':
    main()                    