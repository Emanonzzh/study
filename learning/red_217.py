nums = [3,1,4,1,5,9,2,6]
print(f"最大值{max(nums)},顺序{nums.index(max(nums))}")

print(float("3.14") + 1)

list_1 = ["川西","珠海","滇池"]
for i, ch in enumerate(list_1):
    print(f"{i} : {ch}")

list_2 = [("a",3),("b",1)]
print(sorted(list_2, key=lambda t:t[1]))

text = "雨水是资源"
print(text[::-1])


for year in range(2024,2013, -2):
    print(year)

def two_sum(nums, target):
    seen = {}
    for i in range(len(nums)):
        x = nums[i]
        need = target - x 
        if need in seen:
            return [seen[need], i]
        seen[x] = i

print(two_sum([2, 7, 11, 15], 9))   
print(two_sum([3, 2, 4], 6))        
print(two_sum([3, 3], 6))