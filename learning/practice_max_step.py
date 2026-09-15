def my_max(deforms):
    max_value = deforms[0]
    for v in deforms:
        if v > max_value:
            max_value = v
    return max_value
deforms = [3.2, 5.1, 8.4, 12.0, 18.6, 27.5]

print(my_max(deforms))


def average_step(deforms):
    total = 0 
    count = 0
    for i  in range(1, len(deforms)):
        step = deforms[i] - deforms[i-1]
        total = step + total 
        count = count + 1
    return round(total / count, 2)

print(average_step(deforms))

