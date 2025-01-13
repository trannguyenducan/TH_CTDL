function linear_search(arr, target)
    for (index, value) in enumerate(arr)
        if value == target
            return index
        end
    end
    return -1
end

arr = [4, 2, 5, 1, 3]
println(linear_search(arr, 5)) # Output: 2