def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def main():
    arr = [5, 2, 9, 1, 5]
    bubble_sort(arr)
    print("Ket qua sau Bubble Sort:", arr)

if __name__ == "__main__":
    main()