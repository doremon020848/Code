#!/usr/bin/env python3
# thanathorn chanaphochai
# 670510755
# Lab07_1
# 229223 Sec 001

def main():
    print(corner_frame(7))

def corner_frame(n):
    h = list(range(1, n + 1))
    k = list(range(0, n))
    if n >= 2:
          wow = list(map(lambda x: str(list(range(x ,n + 1))),h))
          mom = list(map(lambda x: x.strip('[]'),wow))
          ro = list(map(lambda x,y,z: ''.join((str(x) + ' ') * z) + y + '\n', h,mom,k)) 
          re = ''.join(ro).replace(',','')
          print(ro)
          return re

if __name__ == '__main__':
    main()
