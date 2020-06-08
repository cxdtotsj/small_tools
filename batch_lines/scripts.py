import os
import matplotlib.pyplot as plt
import matplotlib.axes as ax
from pylab import *

# 支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']

dp = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(dp, 'test_data.txt')

def deal_content(content):
    '''读取文件'''
    indexs = []
    signles = []
    for i, c in enumerate(content):
        if '测试场景' in c:
            indexs.append(i)
    if len(indexs) == 1:
        signle = content
    elif len(indexs) > 1:
        for i in range(len(indexs)):
            try:
                signle = content[indexs[i]:indexs[i+1]]
                signles.append(signle)
            except IndexError:
                signle = content[indexs[i]:]
                signles.append(signle)
    return signles

def deal_signle(signle):
    '''处理单个场景数据'''
    labels = {}
    x = []
    y = []
    try:
        signle.remove('\n')
    except ValueError:
        pass
    for i, v in enumerate(signle):
        v = v.strip('\n')
        data = v.split(',')
        if i == 0:
            labels['title'] = data[0].split(':')[1]
        elif i == 1:
            labels['x_name'] = data[0]
            labels['y_name'] = data[1]
        elif i > 1:
            x.append(int(data[0]))
            y.append(float(data[1]))
    return x, y, labels

def save_fig(i, signle):
    '''设置折线图'''
    # 格式设置
    plt.figure(i, facecolor='black', clear=True) # facecolor: 最外层背景图
    # 网格
    plt.grid(True, linestyle='-.')
    # 设置背景色
    ax = plt.gca()
    ax.patch.set_facecolor("k")
    ax.patch.set_alpha(0.5)
    # 去除边框
    ax.spines['top'].set_visible(False) #去掉上边框
    # ax.spines['bottom'].set_visible(False) #去掉下边框
    # ax.spines['left'].set_visible(False) #去掉左边框
    ax.spines['right'].set_visible(False) #去掉右边框
    # 设置边颜色
    ax.spines['bottom'].set_color('dimgray')
    ax.spines['left'].set_color('dimgray')
    # 设置边框线宽
    ax.spines['bottom'].set_linewidth(2)
    ax.spines['left'].set_linewidth(2)
    # 设置边框线型
    ax.spines['bottom'].set_linestyle('-')
    ax.spines['left'].set_linestyle('-')

    # 写入数据
    x, y, labels = deal_signle(signle)
    # plt.plot(x, y, marker='.', mec='b', mfc='k',label='QPS')
    plt.plot(x, y, '.-b', label='QPS')
    # 判断 y 轴最大值
    max_y = int(max(y))
    if 1000 < max_y < 9000:
        max_y += 1000
    elif 10000 < max_y < 99999:
        max_y += 10000
    elif 100000 < max_y < 999999:
        max_y += 100000
    plt.ylim(0, max_y)  # 限定纵轴的范围
    plt.legend()  # 让图例生效
    plt.xticks(range(0, 2067, 128), rotation=45) # 设置横坐标
    plt.margins(0) # 设置x,y 轴共享同一个0刻度
    plt.subplots_adjust(bottom=0.15)
    plt.xlabel(labels['x_name']) #X轴标签
    plt.ylabel(labels['y_name']) #Y轴标签
    plt.title(labels['title']) #标题
    plt.savefig('{}.png'.format(labels["title"]))
    # plt.show()

def main():
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.readlines()
        signles = deal_content(content)
        for signle in signles:
            x, y, labels = deal_signle(signle)
            print(labels)
            print(x)
            print(y)
        for i, signle in enumerate(signles):
            save_fig(i, signle)


if __name__ == "__main__":
    main()

