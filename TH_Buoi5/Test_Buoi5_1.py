num_list = [0, 7, 0, 2, 0, 4]
k=2
sub_list = []
result = []

for elemnet in num_list:
    sub_list.append(elemnet)

    if len(sub_list) == k:
        result.append(max(sub_list))
        del sub_list [0]

print(result)