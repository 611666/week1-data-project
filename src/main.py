import pandas as pd
import json

# 读取CSV数据
df = pd.read_csv('../data/data.csv')

# 计算统计值
score_counts = df['score'].value_counts(bins=5)

# 把区间键转成字符串
distribution = {}
for key, value in score_counts.items():
    distribution[str(key)] = int(value)

result = {
    "平均分": float(df['score'].mean()),
    "最高分": int(df['score'].max()),
    "最低分": int(df['score'].min()),
    "及格人数": int((df['score'] >= 60).sum()),
    "成绩分布": distribution
}

# 保存为JSON
with open('../result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("完成！结果已保存到 result.json")
