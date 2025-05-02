num_list = [3, 1, -2, -1, 5, 4]
k = 2
result = []
start_indexs = list(range(0, len(num_list) - k + 1))
end_indexs = list(range(k, len(num_list) + 1))

for start_indexs, end_indexs in zip(start_indexs, end_indexs):
    sub_list = num_list[start_indexs:end_indexs]
    result.append(max(sub_list))

print(result)