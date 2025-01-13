def merge(arr, left, mid, right):
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:mid + 1]
    right_arr = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < n1 and j < n2:
        if left_arr[i] <= right_arr[j]:
            arr[k] = left_arr[i]
            i += 1
        else:
            arr[k] = right_arr[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = left_arr[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = right_arr[j]
        j += 1
        k += 1

def mergeSort(arr, left, right):
    if left < right:
        mid = left + (right - left) // 2

        mergeSort(arr, left, mid)
        mergeSort(arr, mid + 1, right)

        merge(arr, left, mid, right)

def main():
    arr = [5, 2, 9, 1, 5, 6]
    mergeSort(arr, 0, len(arr) - 1)

    print("Ket qua Merge Sort:", arr)

if __name__ == "__main__":
    main()