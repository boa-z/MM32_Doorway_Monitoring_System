# 导入所需的模块
import pandas as pd
import matplotlib.pyplot as plt

# 读取数据文件
df = pd.read_csv('guest.csv')

# 提取用户访问的小时
df['hour'] = df['guest_time'].str[11:13]

# 统计每个小时的用户数量
hour_count = df['hour'].value_counts()

# 排序并转换为DataFrame
hour_count = hour_count.sort_index().to_frame()

# 重命名列名
hour_count.columns = ['count']

# 绘制柱状图
plt.bar(hour_count.index, hour_count['count'])
plt.xlabel('Hour')
plt.ylabel('Count')
plt.title('User visits by hour')
plt.xticks(range(24)) # 设置x轴刻度为0-23
plt.show()
