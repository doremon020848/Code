#!/usr/bin/env python3
# ชื่อ นามสกุล (ชื่อเล่น)
# 670510755
# Lab11_2
# 229223 Sec 001

import sys


def main():
    treasures = read_input()

    # assert total_value('Gold', treasures) == 1090
    # assert total_value('Ruby', treasures) == -1

    print(total_value('Gold', treasures))
    print(total_value(total_value('Ruby', treasures)))
    
def read_input():
    treasures = {}

    
    for line in sys.stdin:
        
        line = line.strip()
        
        if line.startswith('#'):
            continue
        
        parts = line.split(',')

        location = parts[0].strip()
        treasure_type = parts[1].strip()
        value = int(parts[2].strip())
        
        if treasure_type not in treasures:
            treasures[treasure_type] = []
            
        treasures[treasure_type].append((location,value))
        
    return treasures

    
def total_value(treasure_type, treasures):
    total = 0
    if treasure_type not in treasures:
        return -1
    
    if treasure_type in treasures:
        for i in range(len(treasures[treasure_type])):
            total += treasures[treasure_type][i][1]
        
        return total

if __name__ == '__main__':
    main()
