#!/usr/bin/env python3
# ธนธรณ์
# รหัสนศ 670510755
# Sec001

def main():
    print(diag_pattern(40), end='')
    print('---')
    
def diag_pattern(n):
    
    if 0 < n <= 1000:
        range_ = list((range(1, n + 1)))
        zfill_ = len(str(n))
        # upper
        lower_ = list(map(lambda x:list(range(x,n)),range_))
        lo1 = list(reversed(lower_))
        lo2 = list(map(lambda x: list(reversed(x)),lo1))
        lo3 = list(map(lambda y: ' '.join(list(map(lambda x: str(x).zfill(zfill_),y))),lo2))
        # lower
        upper_ = list(map(lambda x:list(range(x,n)),range_))
        up1 = list(map(lambda y: ' '.join(list(map(lambda x: str(x).zfill(zfill_),y))),upper_))
        up2 = list(map(lambda x,y:  (x + ' ' + str(n) + ' ' + y + '\n' ).strip(' '),up1,lo3))
        # all
        result = ''.join(up2)
        return result
    else:
        return False 
    
    

if __name__=='__main__':
    main()