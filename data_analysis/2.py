import pandas as pd
import matplotlib.pyplot as plt

# 读取csv文件
df = pd.read_csv("guest.csv")

# 统计guest_login_type中0和1的数量
zero_count = df.guest_login_type.value_counts()[0]
one_count = df.guest_login_type.value_counts()[1]

# 计算0和1的比例
ratio = zero_count / (zero_count + one_count)

# 创建饼图
plt.pie([zero_count, one_count], labels=["registered visitor", "temporary visitor"], autopct="%.1f%%")
plt.title("guest_login_type distribution")
plt.show()
