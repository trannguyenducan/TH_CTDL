function sum_1_to_n(n)
    s = 0
    for i in 1:n
        s += i
    end
    return s
end

n = 5
println("Tong 1..n = ", sum_1_to_n(n)) # Output: 15