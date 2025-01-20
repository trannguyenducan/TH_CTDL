def decimal_to_binary(n):
    stack = []
    print(f"Chuyen doi so thap phan: {n} sang he nhi phan.")

    if n == 0:
        stack.append(0)
        print(f"Da day phan du '0' vao ngan xep.")

    while n > 0:
       remainder = n % 2
       stack.append(remainder)
       print(f"Chia {n} cho 2, phan du: {remainder} -> Day {remainder} vao ngan xep.")
       n = n // 2
       print(f"Thuong moi: {n}")

    binary = ""
    print("Chuyen doi ngan xep thanh so nhi phan:")
    while stack:
        binary += str(stack.pop())
        print(f"Lay {binary[-1]} tu ngan xep va noi vao ket qua.")

    return binary

# Minh hoa
number = 13
binary = decimal_to_binary(number)
print(f"So thap phan {number} chuyen sang he nhi phan la: {binary}") # Output: 1101     
