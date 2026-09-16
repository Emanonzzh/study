"""Python 刷题必备函数速查（跑一遍，看输出）—— 不是背，是"见过 + 用过一次"。

用法：直接运行，看每个函数打印出什么。
      看完之后，把最后那部分【练习】自己写一遍。
"""

print("=" * 66)
print("① 最核心的 10 个（几乎每道题都用）")
print("=" * 66)

nums = [3, 1, 4, 1, 5]

print(f"len(nums)            = {len(nums)}          # 长度 → 5")
print(f"len('hello')         = {len('hello')}          # 字符串长度 → 5")
print(f"sum(nums)            = {sum(nums)}         # 求和 → 14")
print(f"max(nums) / min(nums)= {max(nums)} / {min(nums)}       # 最大/最小")
print(f"abs(-7)              = {abs(-7)}          # 绝对值")
print(f"round(3.567, 1)      = {round(3.567, 1)}        # 四舍五入 → 3.6")
print(f"sorted(nums)         = {sorted(nums)}   # 排序（返回新列表，原列表不变）")
print(f"nums 还是 {nums}          # ← 原列表没变")
print(f"sorted(nums, reverse=True) = {sorted(nums, reverse=True)}  # 倒序")
print(f"list(reversed(nums)) = {list(reversed(nums))}   # 反转")
print(f"list(range(5))       = {list(range(5))}         # 0,1,2,3,4")
print(f"list(range(2, 6))    = {list(range(2, 6))}         # 2,3,4,5")
print(f"list(range(0, 10, 3))= {list(range(0, 10, 3))}         # 步长 3 → 0,3,6,9")
print(f"3 in nums            = {3 in nums}          # 判断存在 → True")
print(f"int('42')            = {int('42')}          # 字符串 → 整数")
print(f"str(42)              = {str(42)!r}        # 整数 → 字符串")
print(f"float('inf') > 1e9   = {float('inf') > 1e9}          # 正无穷（找最小值时初始值）")

print()
print("=" * 66)
print("② enumerate / zip —— 遍历神器")
print("=" * 66)

letters = ["a", "b", "c"]
print("enumerate 同时拿下标和值：")
for i, ch in enumerate(letters):
    print(f"    i={i}, ch={ch}")
print(f"    list(enumerate(letters)) = {list(enumerate(letters))}")
print("    👉 以前你要写 for i in range(len(x)): x[i]，现在一个 enumerate 搞定")

a, b = [1, 2, 3], ["x", "y", "z"]
print(f"\nzip 把两个列表配对：{list(zip(a, b))}")
print("    👉 同时遍历两个列表时用")

print()
print("=" * 66)
print("③ 列表 list 的常用方法")
print("=" * 66)

lst = [1, 2, 3]
lst.append(4)
print(f"lst.append(4)      → {lst}          # 末尾加一个")
lst.pop()
print(f"lst.pop()          → {lst}          # 弹出末尾（返回被弹出的值）")
lst.insert(0, 99)
print(f"lst.insert(0, 99)  → {lst}       # 在下标 0 插入 99")
print(f"lst.index(2)       → {lst.index(2)}           # 2 在哪（第一个出现的下标）")
print(f"lst.count(1)       → {[1,1,2].count(1)}           # 1 出现了几次")
lst2 = [1, 2, 3, 4, 5]
print(f"lst2[1:4]          → {lst2[1:4]}       # 切片：下标 1 到 3（不含 4）")
print(f"lst2[:2]           → {lst2[:2]}          # 前两个")
print(f"lst2[2:]           → {lst2[2:]}       # 从下标 2 到最后")
print(f"lst2[-1]           → {lst2[-1]}            # 最后一个（负索引）")
print(f"lst2[::-1]         → {lst2[::-1]}       # 反转（切片魔法）")

print()
print("=" * 66)
print("④ 字典 dict —— 统计频次必用（★ 你最需要掌握的）")
print("=" * 66)

d = {}
d["apple"] = 1
d["banana"] = 2
print(f"d = {d}")
print(f"d['apple']             → {d['apple']}           # 取值（键不存在会报错！）")
print(f"d.get('pear')          → {d.get('pear')}        # 键不存在返回 None（不报错）")
print(f"d.get('pear', 0)       → {d.get('pear', 0)}           # 键不存在返回默认值 0 ★")
print(f"'apple' in d           → {'apple' in d}          # 判断键在不在")
print(f"d.keys()               → {list(d.keys())}")
print(f"d.values()             → {list(d.values())}")
print(f"d.items()              → {list(d.items())}      # 同时拿键和值")
print(f"d.pop('banana', 0)     → {d.pop('banana', 0)}           # 弹出键，给默认值防报错")

print("\n★ 统计频次的标准写法（刷题出现率极高）：")
text = "anagram"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(f'    "{text}" → {counts}')

print()
print("=" * 66)
print("⑤ 集合 set —— 去重 + 判断存在")
print("=" * 66)

s = {1, 2, 3}
s.add(4)
print(f"set.add(4)         → {s}          # 加元素")
s.discard(1)
print(f"set.discard(1)     → {s}          # 删除（不存在也不报错）")
print(f"list(set([1,1,2,3,3])) → {sorted(set([1,1,2,3,3]))}   # 去重！")
print(f"{{1,2}} & {{2,3}}        → {{1,2}} & {{2,3}} = {({1,2} & {2,3})}     # 交集")
print(f"{{1,2}} | {{2,3}}        → {({1,2} | {2,3})}        # 并集")
print(f"{{1,2,3}} - {{2}}      → {({1,2,3} - {2})}        # 差集")

print()
print("=" * 66)
print("⑥ 字符串 str 的常用方法")
print("=" * 66)

t = "  Hello World  "
print(f"t.strip()          → {t.strip()!r}   # 去首尾空格")
print(f"'a,b,c'.split(',') → {('a,b,c'.split(','))}   # 切成列表 ★")
print(f"'-'.join(['a','b']) → {('-'.join(['a','b']))!r}       # 拼成字符串 ★")
print(f"'AbC'.lower()      → {('AbC'.lower())!r}")
print(f"'AbC'.upper()      → {('AbC'.upper())!r}")
print(f"'aaa'.replace('a','b') → {('aaa'.replace('a','b'))!r}")
print(f"'123'.isdigit()    → {('123'.isdigit())}          # 是不是数字")
print(f"'abc'.isalpha()    → {('abc'.isalpha())}          # 是不是字母")
print(f"sorted('cba')      → {sorted('cba')}      # 字符串排序 → 变成字符列表 ★")

print()
print("=" * 66)
print("⑦ 列表推导式 —— 一行写循环（读别人代码必会）")
print("=" * 66)

nums = [1, 2, 3, 4, 5]
print(f"[x*2 for x in nums]        → {[x*2 for x in nums]}       # 每个 ×2")
print(f"[x for x in nums if x > 2] → {[x for x in nums if x > 2]}          # 只要 >2 的")
print(f"[x for x in nums if x % 2 == 0] → {[x for x in nums if x % 2 == 0]}          # 偶数")
print("👉 等价于：result = []");
print("          for x in nums:")
print("              if x % 2 == 0: result.append(x)")

print()
print("=" * 66)
print("⑧ 进阶工具（见到知道是什么就行，不用背）")
print("=" * 66)

from collections import Counter, defaultdict, deque
import heapq

print(f"Counter('anagram')        → {Counter('anagram')}   # 自动统计频次 ★")
print(f"Counter('aab') == Counter('aba') → {Counter('aab') == Counter('aba')}   # 比较组成")
dd = defaultdict(list)
dd["k"].append(1)
print(f"defaultdict(list)         → {dict(dd)}   # 键不存在时自动给默认值")
dq = deque([1, 2, 3])
dq.appendleft(0)
print(f"deque.appendleft(0)       → {list(dq)}   # 两端都能高效增删（BFS 用）")
h = [3, 1, 2]
heapq.heapify(h)
print(f"heapq 最小堆              → {h}（堆顶 {h[0]} 是最小值）")
print("👉 排序带条件：sorted(students, key=lambda x: x[1], reverse=True)")

# ==================================================================
print()
print("=" * 66)
print("【练习】关掉上面的代码，自己写这 6 个（写在下面，跑通为止）")
print("=" * 66)
print("""
1. 用 len() 和 sum() 算 [10, 20, 30] 的平均值
   → 你的代码：

2. 用 enumerate 打印 ['a','b','c'] 的"下标:值"
   → 你的代码：

3. 用字典统计 "hello" 里每个字母出现几次
   → 你的代码：

4. 用 set 把 [1,1,2,2,3] 去重并排序
   → 你的代码：

5. 用 split 把 "a-b-c" 切成列表，再用 join 拼回 "a|b|c"
   → 你的代码：

6. 用列表推导式取出 [1,2,3,4,5,6] 里的偶数
   → 你的代码：
""")
