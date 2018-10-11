'''
版本：2.0
作者：sky
日期：20181011
作用：显示各点数次数,投两个骰子
'''

import random
import matplotlib #macos需增加此句话
matplotlib.use('TkAgg')  #macos需增加此句话
import matplotlib.pyplot as plt

def roll_dice():
    saizi=random.randint(1, 6)
    return  saizi

def main():
    total = 100
    dice_list = [0]*11

    dianshu_list = list(range(2, 13))

    roll1_list = []
    rool2_list = []

    dict_roll = dict(zip(dianshu_list, dice_list))
    for i in range(total):
        roll1 = roll_dice()
        roll2 = roll_dice()
        #数据记录
        roll1_list.append(roll1)
        rool2_list.append(roll2)

        for j in range(2, 13):
            if (roll1+roll2) == j:
                dict_roll[j] += 1
    y = []
    for i, x in dict_roll.items():
        print('点数{}的次数为：{}，频率:{}'.format(i, x, x/total))
        y.append(x/total)

    # 点数为x，频率为y
    j = range(2, 13)
    plt.scatter(j, y, c='blue')
    plt.show()


    #数据可视化
    x = range(1, total+1)
    plt.scatter(x, roll1_list, c='red', alpha=0.5)
    plt.scatter(x, rool2_list, c='green', alpha=0.5)
    plt.show()





if __name__ == '__main__':
    main()