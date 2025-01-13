function merge!(arr, left, mid, right)
    n1 = mid - left + 1
    n2 = right - mid

    left_arr = arr[left:mid]
    right_arr = arr[mid+1:right]

    i = 1
    j = 1
    k = left

    while i <= n1 && j <= n2
        if left_arr[i] <= right_arr[j]
            arr[k] = left_arr[i]
            i += 1
        else
            arr[k] = right_arr[j]
            j += 1
        end
        k += 1
    end

    while i <= n1
        arr[k] = left_arr[i]
        i += 1
        k += 1
    end

    while j <= n2
        arr[k] = right_arr[j]
        j += 1
        k += 1
    end
end

function mergeSort!(arr, left, right)
    if left < right
        mid = left + (right - left) ÷ 2
        mergeSort!(arr, left, mid)
        mergeSort!(arr, mid + 1, right)
        merge!(arr, left, mid, right)
    end
end

function main()
    arr = [5, 2, 9, 1, 5, 6]
    mergeSort!(arr, 1, length(arr))
    println("Ket qua Merge Sort: ", arr)
end

main()