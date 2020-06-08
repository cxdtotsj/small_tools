import matplotlib.pyplot as plt
from pylab import *
#支持中文
mpl.rcParams['font.sans-serif'] = ['SimHei']
x = [0, 8, 64, 128, 256, 512, 1024, 2048]
# x = range(0, 2067, 128)
y = [0, 37275.11, 243875.38, 368415.17, 434837.07, 465835.41, 492339, 489720.75]
plt.plot(x, y, marker='o', mec='r', mfc='w',label='并发吞吐量')
# plt.xlim(0, 2067)  # 限定横轴的范围
plt.ylim(0, 510000)  # 限定纵轴的范围
plt.legend()  # 让图例生效
plt.xticks(range(0, 2067, 128), rotation=45)
# plt.xticks(x)
# plt.yticks(int(max(y_num))+40000)
plt.margins(0)
plt.subplots_adjust(bottom=0.15)
plt.xlabel("并发数") #X轴标签
plt.ylabel("QPS") #Y轴标签
plt.title("insert单条") #标题
plt.savefig('temp.png')
plt.show()