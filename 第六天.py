import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time

plt.rcParams["font.family"] = ["Microsoft YaHei"]
plt.rcParams["axes.unicode_minus"] = False

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
time.sleep(1.5)
print("\n=== 数据基本信息 ===")
print(f"数据形状: {df.shape}")
print("\n前5行数据:")
print(df.head())
print("\n数据基本信息:")
print(df.info())
print("\n数值列的统计信息:")
print(df.describe())


print("\n=== 按产品类别分析 ===")
category_analysis = df.groupby('产品类别').agg({
    '销售额': ['sum', 'mean', 'count'],
    '总利润': 'sum',
    '利润率': 'mean'
}).round(2)
print(category_analysis)


print("\n=== 按地区分析 ===")
region_analysis = df.groupby('地区').agg({
    '销售额': 'sum',
    '总利润': 'sum',
    '数量': 'sum'
}).round(2)
print(region_analysis)



print("\n正在创建图表...")
time.sleep(1.5)


fig, axes = plt.subplots(2, 2, figsize=(15, 12))

# 图表1：各产品类别的销售额总和
category_sales = df.groupby('产品类别')['销售额'].sum().sort_values(ascending=False)
axes[0, 0].bar(category_sales.index, category_sales.values)
axes[0, 0].set_title('各产品类别销售额总和')
axes[0, 0].set_ylabel('销售额')
axes[0, 0].tick_params(axis='x', rotation=45)

# 图表2：各地区的销售额分布
region_sales = df.groupby('地区')['销售额'].sum()
axes[0, 1].pie(region_sales.values, labels=region_sales.index, autopct='%1.1f%%')
axes[0, 1].set_title('各地区销售额分布')

# 图表3：销售额随时间的变化
df_sorted = df.sort_values('日期')
axes[1, 0].plot(df_sorted['日期'], df_sorted['销售额'])
axes[1, 0].set_title('销售额随时间变化')
axes[1, 0].set_ylabel('销售额')
axes[1, 0].tick_params(axis='x', rotation=45)

# 图表4：销售额与利润率的散点图
axes[1, 1].scatter(df['销售额'], df['总利润'], alpha=0.6)
axes[1, 1].set_title('销售额 vs 总利润')
axes[1, 1].set_xlabel('销售额')
axes[1, 1].set_ylabel('总利润')

# 调整布局
plt.tight_layout()


plt.savefig('sales_analysis.png', dpi=400, bbox_inches='tight')
print("图表已保存为 'sales_analysis.png'")

with pd.ExcelWriter('数据分析报告.xlsx', engine='xlsxwriter') as writer:
    # 7.1 导出原始数据
    df.to_excel(writer, sheet_name='原始数据', index=False)

    # 7.2 导出分类汇总数据
    category_analysis.to_excel(writer, sheet_name='产品类别分析')
    region_analysis.to_excel(writer, sheet_name='地区分析')

    # 7.3 创建数据透视表
    pivot_table = pd.pivot_table(df,
                                 values='销售额',
                                 index='产品类别',
                                 columns='地区',
                                 aggfunc='sum',
                                 fill_value=0)
    pivot_table.to_excel(writer, sheet_name='数据透视表')

    # 获取工作簿和工作表对象
    workbook = writer.book

    # 7.4 添加图表到Excel（可选）
    # 创建一个总结工作表
    summary_sheet = workbook.add_worksheet('分析总结')

    summary_sheet.write('A1', '数据分析报告')
    summary_sheet.write('A2', f'分析时间: {pd.Timestamp.now()}')
    summary_sheet.write('A3', f'总数据量: {len(df)} 行')
    summary_sheet.write('A4', f'总销售额: {df["销售额"].sum():,.2f}')
    summary_sheet.write('A5', f'总利润: {df["总利润"].sum():,.2f}')

    # 在工作表中插入图片
    summary_sheet.insert_image('A7', 'sales_analysis.png')

print("数据已成功导出到 '数据分析报告.xlsx'")

