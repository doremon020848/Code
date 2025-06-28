#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab04_1
# 229223 Sec 001

def main():
    num = str(input())
    mma = german_num_format(num)
    print(mma)
    test_german_num_format()
    


def german_num_format(num):

# มีทศนิยม
    if ',' in num and '.' not in num:
        mom = num.replace(',', '.')
        return mom
    # elif '.' in num and ',' not in num:
    #     mom = num.replace('.', ',')
    #     return mom
        
# ไม่มีทศนิยม
    elif ',' in num :
        mom = num.replace(",", "+")     
        dad = mom.replace(".", ",") 
        sis = dad.replace("+", ".")
        return sis
    
    elif '.' in num :
        mom = num.replace(".", "+")     
        dad = mom.replace(",", ".") 
        sis = dad.replace("+", ",")
        return sis
    else:
        return num
     
    

def test_german_num_format():
    assert german_num_format("1,234") == "1.234"
    assert german_num_format("1,020.50") == "1.020,50"
    assert german_num_format("12,356") == "12.356"
    assert german_num_format("123,560.90") == "123.560,90"
    assert german_num_format("123,456,789,104.5678") == "123.456.789.104,5678"
    assert german_num_format("123.456") == "123,456"
    print("all KO!!!")



if __name__ == '__main__':

    main()