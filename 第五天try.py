# import numpy as np
# np.random.seed(42)
# date = np.random.randint(1,100,10)
# print(date)
# np.random.seed(42)
# dates =np.random.randint(1,100,10)
# print(dates)

# import time
#
# # 每隔2秒显示一次内容
# for i in range(5):
#     print(i)
#     time.sleep(2)  # 暂停2秒
import pandas as pd
data = {"姓名" : ["zbl","lzr","hcj"],"年龄" : [18,18,18],"city" : ["shanghai","shanghai","shanghai"]}
df = pd.DataFrame(data)
df.index = [1, 2, 3]
print("\n=== 数据基本信息 ===")
print(f"数据形状: {df.shape}")  # 显示数据行数和列数
print("\n前5行数据:")
print(df.head())
print("\n数据基本信息:")
print(df.info())

print("\n数值列的统计信息:")
print(df.describe())

