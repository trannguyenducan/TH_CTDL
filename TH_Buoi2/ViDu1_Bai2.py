def sum_1_to_n(n):
    s = 0
    for i in range(1, n + 1):
        s += i
    return s

n = 5
print("Tong 1..n = ", sum_1_to_n(n)) # Output: 15