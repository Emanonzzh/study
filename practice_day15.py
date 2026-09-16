# 手写第3组：split_two（列表切分）/ parse_point（JSON解析）/ MonitorPoint 类（OOP启蒙）
#
# 【review 修正记录 2026-09-16】
#   ① 函数名 qplit_two → split_two（拼写错误，s 打成了 q）
#   ② parse_point 静默丢掉了 coordinates 的第三个值 → 改成显式说明
#   ③ PEP8：切片别写空格、return 后不加括号、逗号后要空格、import 置顶
#   ④ 补边界测试：奇数 / 单元素 / 空列表（原来只有偶数）
#   ⑤ 删掉重复创建 p2 的代码（追加实验时复制粘贴留下的）
#   ⑥ 加 if __name__ == "__main__" 保护：被 import 时不再执行顶层代码

import json


def split_two(values):
    """把列表从中间切成两半，返回 (前半, 后半)。

    奇数长度时，中间那个元素归到**后半**（因为 len // 2 向下取整）。
    """
    mid = len(values) // 2
    front = values[:mid]
    back = values[mid:]
    return front, back


def parse_point(point):
    """从 GeoJSON 字符串里取出 (区域, x, y)。

    ⚠️ 注意：coordinates 是三维 [x, y, z]，第三个值（高程/形变量）这里**不返回**。
    本练习只需要平面坐标，但**丢数据必须显式写出来**，不能悄悄丢 ——
    静默丢数据比报错更危险（调用方会以为拿全了）。
    需要时改成：return region, coords[0], coords[1], coords[2]
    """
    data = json.loads(point)
    region = data["properties"]["region"]
    coords = data["geometry"]["coordinates"]
    return region, coords[0], coords[1]


class MonitorPoint:
    """形变监测点：用来验证 self 是「每个实例自己的盒子」。"""

    def __init__(self, name, x, y):
        self.name = name
        self.x = x
        self.y = y
        self.rate = 0.0

    def set_rate(self, rate):
        """给速率赋值。"""
        self.rate = rate


POINT_JSON = (
    '{"type": "Feature", "properties": {"region": "川西"}, '
    '"geometry": {"coordinates": [102.5, 30.1, 3.2]}}'
)


if __name__ == "__main__":
    # ① 列表切分：偶数 + 三个边界
    print(split_two([2.1, 3.5, 5.0, 7.2, 9.8, 12.5]))   # 偶数 → ([2.1, 3.5, 5.0], [7.2, 9.8, 12.5])
    print(split_two([1, 2, 3]))                          # 奇数 → ([1], [2, 3])
    print(split_two([9]))                                # 单元素 → ([], [9])
    print(split_two([]))                                 # 空 → ([], [])

    # ② JSON 解析
    print(parse_point(POINT_JSON))                       # ('川西', 102.5, 30.1)

    # ③ 两个实例互不干扰（self 概念实锤）
    p1 = MonitorPoint("川西-01", 102.5, 30.1)
    p2 = MonitorPoint("珠海-02", 113.2, 22.5)
    p1.set_rate(3.5)
    p2.set_rate(1.2)
    print(p1.name, p1.x, p1.y, p1.rate)                  # 川西-01 102.5 30.1 3.5
    print(p1.rate, p2.rate)                              # 3.5 1.2 —— 互不串台
