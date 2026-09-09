def recent_average(deforms, n):
    if len(deforms) < n:
        return None
    recent = deforms[-n:]
    total = 0
    for v in recent:
        total += v
    return total / n

deforms = [3.2, 5.1, 8.4, 12.0, 18.6, 27.5]
print(recent_average(deforms, 3))


datasets = [
    {"name": "青藏走廊形变", "source": "国家冰川冻土沙漠科学数据中心"},
    {"name": "理塘形变反演", "source": "国家冰川冻土沙漠科学数据中心"},
    {"name": "中巴走廊形变", "source": "甘肃省生态环境科学数据中心"},
]

counts = {}
for ds in datasets:
    source = ds["source"]
    counts[source] = counts.get(source, 0) + 1

for source, num in counts.items():
    print(f"{source}: {num}")