function printPairs(n)
    for i in 1:n
        for j in 1:n
            println("($i, $j)")
        end
    end
end

printPairs(3)