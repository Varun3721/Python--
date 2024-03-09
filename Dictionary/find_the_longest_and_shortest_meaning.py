dict1 = {'piece': 'portion of an object', 'patch': 'a piece of cloth or material ,produced by cutting',
         'area': 'a region or'}
keys = list(dict1.keys())
values = list(dict1.values())

length = [len(x) for x in values]
max_len = max(length)
min_len = min(length)
max_index = length.index(max_len)
min_index = length.index(min_len)

print("max", keys[max_index], values[max_index])
print("min", keys[min_index], values[min_index])
