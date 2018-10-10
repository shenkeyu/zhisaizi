'''
版本：1.0
作者：sky
日期：20181010
作用：显示各点数次数
'''

import random

def roll_dice():
    saizi=random.randint(1, 6)
    return  saizi

def main():
    total = 10000
    dice_list =[0]*6
    for i in range(total):
        roll = roll_dice()
        for j in range(1, 7):
            if roll == j:
                dice_list[j-1] += 1

    print(dice_list)

    for i, x in enumerate(dice_list):
        print('点数{}的次数为：{}，频率:{}'.format(i+1, x, x/total))



if __name__ == '__main__':
    main()