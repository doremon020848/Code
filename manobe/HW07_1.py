#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# HW07_1
# 229223 Sec 001

def main():
    square_frame(3)
     
def square_frame(n, sep=' '):
    
    if sep != '' :
        
        k = list(range(1, n - 1))
        a1 = list(range((n + 1) , (4 * n - 4) + 1))
        
        # ใส่ศูนย์
        zero = str(a1[-1])
        zero_wow = len(zero)
        
        # หา บนสุด
        top = str(list(range(1,n + 1))).strip('[]').replace(',','').split()
        top_1 = list(map(lambda x:(x.zfill(zero_wow)) ,top))
        top_2 = ' '.join(top_1).replace(',','').replace(' ',sep)
    
        #  หาล่างสุด
        under = list((str(list(range((n * 2) - 1,((n * 2) - 1) + n))[::-1]).replace(',','').strip('[]')).split())
        under_1 = list(map(lambda x:(x.zfill(zero_wow)) ,under))
        under_2 = ' '.join(under_1).replace(',','').replace(' ',sep)
        
        # หาจุด
        mom = len(under_2)- (len(zero) * 2)

        # หาตรงกลาง
        h = list(map(lambda x: list(range((n + x) , (4 * n - 4) + 2 - x))[::-1],k))
        l = list(map(lambda x: (len(x) - 2) + 1,h))
        g = list(map(lambda x,y: y[::x] ,l,h))
        all_g = list(map(lambda x: str(x[0]).zfill(zero_wow) + (sep * mom) + str(x[-1]).zfill(zero_wow) ,g))
        all_g_1 = '\n'.join(all_g).replace(',','')
        
        for y in top_2,all_g_1,under_2:
            print(y)

    elif sep == '':
        
        k = list(range(1, n - 1))
        a1 = list(range((n + 1) , (4 * n - 4) + 1))
    
        # ใส่ศูนย์
        zero = str(a1[-1])
        zero_wow = len(zero)
        # หา บนสุด
        top = str(list(range(1,n + 1))).strip('[]').replace(',','').split()
        top_1 = list(map(lambda x:(x.zfill(zero_wow)) ,top))
        top_2 = ' '.join(top_1).replace(',','')
    
        #  หาล่างสุด
        under = list((str(list(range((n * 2) - 1,((n * 2) - 1) + n))[::-1]).replace(',','').strip('[]')).split())
        under_1 = list(map(lambda x:(x.zfill(zero_wow)) ,under))
        under_2 = ' '.join(under_1).replace(',','')
        
        # หาจุด
        mom = len(under_2)- (len(zero) * 2)

        # หาตรงกลาง
        h = list(map(lambda x: list(range((n + x) , (4 * n - 4) + 2 - x))[::-1],k))
        l = list(map(lambda x: (len(x) - 2) + 1,h))
        g = list(map(lambda x,y: y[::x] ,l,h))
        all_g = list(map(lambda x: str(x[0]).zfill(zero_wow) + (' ' * mom) + str(x[-1]).zfill(zero_wow) ,g))
        all_g_1 = '\n'.join(all_g).replace(',','')
        
        for y in top_2,all_g_1,under_2:
            print(y)
    
if __name__ == '__main__':
    main()
    