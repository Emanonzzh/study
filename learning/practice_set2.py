def count_by_source(data):
    counts = {}
    for ds in data:
        source = ds["source"]
        counts[source] = counts.get(source,0) + 1
    return counts

datasets = [
    {"name": "青藏走廊形变", "source": "国家冰川冻土沙漠科学数据中心"},
    {"name": "理塘形变反演", "source": "国家冰川冻土沙漠科学数据中心"},
    {"name": "中巴走廊形变", "source": "甘肃省生态环境科学数据中心"},
]
print(count_by_source(datasets))

def region_stats(records):
    region_max = {}
    for r in records:
        region = r["region"]
        value = r["value"]
        if region not in region_max:
            region_max[region] = value
        elif value > region_max[region]:
            region_max[region] = value
    return region_max

records = [
    {"region": "川西", "value": 98.5},
    {"region": "珠海", "value": 60.0},
    {"region": "川西", "value": 55.2},
    {"region": "珠海", "value": 45.0},
]
print(region_stats(records))


def mask_keyword(name, keyword):
    star = '*' * len(keyword)
    return name.replace(keyword, star)

print(mask_keyword("青藏走廊滑坡数据.txt", "滑坡"))    # 青藏走廊**数据.txt
print(mask_keyword("泥石流预警.txt", "泥石流"))        # ****预警.txt
print(mask_keyword("中巴走廊形变数据.txt", "滑坡"))    # 中巴走廊形变数据.txt（没有就不变）