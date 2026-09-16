nums = [10, 20, 30]

def ava(nums):
    n = len(nums)
    s = sum(nums)
    return s / n

print(ava(nums))

letters = ["x", "y"]
for i, ch in enumerate(letters, start=1):
    print(f"第{i}个是{ch}")    

text = "banana"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch, 0) + 1
print(f"{counts}")

nums = [3,3,1,1,2]
result = sorted(set(nums),reverse=True)
print(f"去重结果：{set(nums)}")
print(f"去重后排序结果：{result}")


date = "2025-09-17".split("-")
print(date)

part = ["a", "b", "c"]
joined = "-".join(part)
print(joined)

s_nums = [1,2,3,4,5,6]
evens = [i for i in s_nums if i > 3]
print(evens)



     