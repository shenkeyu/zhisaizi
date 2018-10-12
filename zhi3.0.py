'''
版本：3.0
作者：sky
日期：20181011
作用：显示各点数次数,投两个骰子
'''

import random
import matplotlib #macos需增加此句话
matplotlib.use('TkAgg')  #macos需增加此句话
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import *

def main():
    total = 100

    roll1_np = np.random.randint(1, 7, size=total)
    roll2_np = np.random.randint(1, 7, size=total)
    roll_np = roll1_np + roll2_np

    hist, bins = np.histogram(roll_np, bins=range(2, 14))
    print(hist)
    print(bins)

    zhfont1 = matplotlib.font_manager.FontProperties(fname='/Library/Fonts/songti.ttc')  # 从mac系统指定一个中文ttf文件
    plt.hist(roll_np, bins=range(2, 14), density=1, edgecolor='black', linewidth=1, rwidth=0.5)

    tick_labels = ['2点', '3点', '4点', '5点', '6点', '7点', '8点', '9点', '10点', '11点', '12点']
    tick_pos = np.arange(2, 13)+0.5
    plt.xticks(tick_pos, tick_labels, fontproperties=zhfont1)

    plt.title('点数概率', fontproperties=zhfont1)
    plt.xlabel('两个骰子之和', fontproperties=zhfont1)
    plt.ylabel('概率', fontproperties=zhfont1)
    plt.show()

if __name__ == '__main__':
    main()