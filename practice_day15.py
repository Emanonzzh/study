# 手写第3组：split_two（列表切分）/ parse_point（JSON解析）/ MonitorPoint 类（OOP启蒙）
def qplit_two(values):
    mid = len(values) // 2
    front = values[ : mid]
    back = values[mid: ]
    return(front, back)
values = [2.1, 3.5, 5.0, 7.2, 9.8, 12.5]
print(qplit_two(values))

import json

def parse_point(point):
    data = json.loads(point)
    region = data["properties"]["region"]
    coords = data["geometry"]["coordinates"]
    return(region, coords[0], coords[1])

point = '{"type": "Feature", "properties": {"region": "川西"}, "geometry": {"coordinates": [102.5, 30.1, 3.2]}}'
print(parse_point(point))

class MonitorPoint:
    def __init__(self,name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.rate = 0.0

    def set_rate(self, rate):
        """给速率赋值"""
        self.rate = rate

p1 = MonitorPoint("川西-01", 102.5, 30.1)   
p1.set_rate(3.5)
print(p1.name, p1.x, p1.y, p1.rate)
p1.set_rate(3.5)          # 你已有的
p2 = MonitorPoint("珠海-02", 113.2, 22.5)    # 追加：造第二个
p2.set_rate(1.2)
print(p1.rate, p2.rate)   # 预期：3.5 1.2 —— 两个盒子互不串台
# 追加实验：两个实例互不干扰（self = 实例自己的验证）
p2 = MonitorPoint("珠海-02", 113.2, 22.5)
p2.set_rate(1.2)
print(p1.rate, p2.rate)   # 预期 3.5 1.2
