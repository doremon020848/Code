#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab05_1
# # 229223 Sec 001


def main():
    pattern = str(input("น้ำพริก="))
    word = str(input("กะปิ="))
    print(is_wildcard_match(pattern, word))
    
def is_wildcard_match(pattern, word):

# # หาตำเเหน่ง ? เเรก
#     frond_pattern = pattern.find("?")
# # หาตำเเหน่ง ? หลัง
#     black_pattern = pattern.rfind("?")

#     pattern_wow = pattern[:frond_pattern]
#     word_wow = word[black_pattern + 1:]
    frond_pattern = pattern.find("?")
    black_pattern = pattern.count("?")
    mom = pattern[:frond_pattern]
    dad = pattern[frond_pattern + black_pattern:]


    if (mom in word ) and (dad in word):
        return True

    else:
        return False          
    
if __name__ == "__main__":
    main()