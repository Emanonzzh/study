"""练习 2-6 的答案 + 逐行解释 + 【你的变体练习】。

用法：先看答案和解释 → 然后关掉这个文件，自己写最后的变体练习。
"""

print("=" * 64)
print("第 2 题：用 enumerate 打印 '下标:值'")
print("=" * 64)

letters = ["a", "b", "c"]
for i, ch in enumerate(letters):
    print(f"  {i}:{ch}")

print("""
【解释】enumerate 一次给你两样东西：
    第 1 个：序号（0, 1, 2...）
    第 2 个：元素本身（'a', 'b', 'c'）
    for i, ch in ... 的意思是【拆包】：把 (序号, 元素) 拆成两个变量

【对比】以前你得写：
    for i in range(len(letters)):
        ch = letters[i]          ← 啰嗦，还容易写错
【现在】for i, ch in enumerate(letters):   ← 一行搞定
""")

print("=" * 64)
print("第 3 题：用字典统计 'hello' 里每个字母出现几次")
print("=" * 64)

text = "hello"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(f"  {counts}")

print("""
【解释】counts.get(ch, 0) 的意思是：
    "去 counts 里找 ch 这个键；找不到就返回 0（而不是报错）"
    所以第一次遇到 h：get('h', 0) → 0，然后 +1 → 1，存进去
    第二次遇到 l：get('l', 0) → 1，然后 +1 → 2

★ 关键：这一行你【已经写过】！
  翻 learning/practice_risk.py：
      counts[source] = counts.get(source, 0) + 1
  一模一样的代码，只是统计的东西从"数据来源"变成了"字母"。
""")

print("=" * 64)
print("第 4 题：用 set 把 [1,1,2,2,3] 去重并排序")
print("=" * 64)

nums = [1, 1, 2, 2, 3]
result = sorted(set(nums))
print(f"  set(nums)      = {set(nums)}        ← 去重")
print(f"  sorted(set(...)) = {result}   ← 再排序")

print("""
【解释】这是【嵌套调用】：把里面函数的返回值，直接喂给外面的函数。
    set(nums)        → {1, 2, 3}（集合，无序）
    sorted({1,2,3})  → [1, 2, 3]（列表，有序）
  读法：从里往外读 —— "先把 nums 去重，再把结果排序"
""")

print("=" * 64)
print("第 5 题：split 切分 + join 拼回")
print("=" * 64)

parts = "a-b-c".split("-")
print(f'  "a-b-c".split("-")  = {parts}      ← 字符串 → 列表')
joined = "|".join(parts)
print(f'  "|".join({parts}) = {joined!r}          ← 列表 → 字符串')

print("""
【解释】这两个方向相反，记住一对：
    split(分隔符)  ：把字符串【切成】列表
    join(分隔符)   ：把列表【拼成】字符串

⚠️ join 的写法容易记错：是 "分隔符".join(列表)，不是 列表.join("分隔符")
""")

print("=" * 64)
print("第 6 题：用列表推导式取出偶数")
print("=" * 64)

nums = [1, 2, 3, 4, 5, 6]
evens = [x for x in nums if x % 2 == 0]
print(f"  [x for x in nums if x % 2 == 0] = {evens}")

print("""
【解释】读作：
    "对于 nums 里的每个 x，如果 x 除以 2 余数是 0，就把 x 放进新列表"
     [x     for x in nums     if x % 2 == 0]
      ↑            ↑                  ↑
   要什么        从哪来            什么条件

【等价于】普通写法：
    evens = []
    for x in nums:
        if x % 2 == 0:
            evens.append(x)
""")

# ==================================================================
print()
print("=" * 64)
print("【你的变体练习】关掉上面的代码，自己写这 6 个")
print("=" * 64)
print("""
1. 用 enumerate 打印 ["x", "y"] 的 "第1个是x" 这种格式（序号从 1 开始）
   → 提示：enumerate(列表, start=1)

2. 用字典统计 "banana" 里每个字母出现几次
   → 提示：和第 3 题一模一样，只换字符串

3. 用 set 和 sorted 把 [3,3,1,1,2] 去重并【倒序】排（从大到小）
   → 提示：sorted(..., reverse=True)

4. 把 "2025-09-17" 按 "-" 切开，得到年月日三个部分
   → 提示：split("-") 会得到 3 个元素的列表

5. 用 join 把 ["a", "b", "c"] 拼成 "a-b-c"
   → 提示："-".join(列表)

6. 用列表推导式，从 [1,2,3,4,5,6] 里取出【大于 3】的数
   → 提示：把 x % 2 == 0 换成 x > 3
""")
