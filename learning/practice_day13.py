def recent_rate(values):
    if len(values) < 4:
        return  None
    else:
        return round((values[-1] - values[-4]) / 3, 1)

values = [2.1, 3.5, 5.0, 7.2, 9.8]

print(recent_rate(values))

def max_deform(data):
    best_region = None
    best_value = None
    for region in data:
        values = data[region]
        local_max = values[0]
        for v in values:
            if v > local_max:
                local_max = v
        if best_value is None or local_max > best_value:
            best_value = local_max
            best_region = region
    return best_region,best_value



def longest_growth(values):
    if len(values) == 0:
        return 0
    longest = 1
    current = 1
    for i in range(1, len(values)):
        if values[i] > values[i-1]:
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1
    return longest