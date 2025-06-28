#!/usr/bin/env python3
# ธฯธรณ์
# 670510755
# 229223 Sec 001

def main():
    print(make_licence_code(1234, 'BKK'))

    
def  make_licence_code(number,province):
    return province + '-' + str(number)

   
if __name__ == '__main__':
    main()