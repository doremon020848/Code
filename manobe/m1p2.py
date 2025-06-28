#!/usr/bin/env python3
# ชื่อ (ไม่ต้องใส่นามสกุล)
# รหัสนศ
# Sec00x


def main():

    assert mask_code(95, 'white') == 'N95-wh'
    assert mask_code(97, 'black') == 'N97-bl'
    assert mask_code(90, 'brown') == 'N90-br'

    print("All tests passed!")


def mask_code(PFE, color):
    
    mask = str(PFE)
    color1 = color[:2]
    f1 = 'N' + mask + '-' + color1
    return f1


if __name__ == '__main__':
    main()
