def two_sum_fast(deforms, target):
    seen = {}
    for i in range(len(deforms)):
        x = deforms[i]
        need = target - x
        if need in seen:
            return [seen[need], i]
        seen[x] = i
print(two_sum_fast([2, 7, 11, 15], 9))
print(two_sum_fast([3, 2, 4], 6))      
