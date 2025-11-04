import pandas as pd
# data   = pd.Series(["zbl","lzr"],index = [1,2])
# print(data)


# 从字典创建 DataFrame
data = {"姓名" : ["zbl","lzr","hcj"],"年龄" : [18,18,18],"city" : ["shanghai","shanghai","shanghai"]}
df = pd.DataFrame(data)
print(df)
df.index = [1, 2, 3]
