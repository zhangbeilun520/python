import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

def create_sample_data():
    data = {
        '日期': pd.date_range('2024-01-01', periods=100, freq='D'),
        '产品类别': np.random.choice(['电子产品', '服装', '食品', '家居', '书籍'], 100),
        '销售额': np.random.normal(1000, 300, 100),
        '数量': np.random.randint(1, 50, 100),
        '利润率': np.random.uniform(0.1, 0.4, 100),
        '地区': np.random.choice(['华北', '华东', '华南', '西部'], 100)
    }

    df = pd.DataFrame(data)

    df['总利润'] = df['销售额'] * df['利润率']


    return df
print("正在创建示例数据...")
df = create_sample_data()
time.sleep(2)
print("\n=== 数据基本信息 ===")
print(f"数据形状: {df.shape}")
print("\n前5行数据:")
print(df.head())





