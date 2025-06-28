#!/usr/bin/env python3
# Thanathorn chanaphochai benz
# 670510755
# Lab02_1
# 229223 Sec 001
import math


def main():
    # รับข้อมูลพื้นที่ผิวจาก user
    surface_area = float(input("input surface area: "))

    # นำพื้นที่ผิวที่ได้มาคำนวณหารัศมี
    radius = find_r_from_surface_area(surface_area)

    # นำรัศมีที่คำนวณได้มาคำนวณหาปริมาตร
    volume = sphere_volume(surface_area)

    # แสดงปริมาตรทรงกลม แบบทศนิยมสองต่ำแหน่ง
    print("volume = %.2f"%(volume))


def find_r_from_surface_area(surface_area):
    r = math.sqrt(surface_area / 4 * ( math.pi))
    return r


def sphere_volume(radius):
    volume = (4/3 * math.pi * (surface_area ** 3))
    return volume


if __name__ == '__main__':
    main()
