using Printf

function solve(s::String)::Int
    balance = 0
    changes = 0
    for c in s
        if c == '('
            balance += 1
        else
            balance -= 1
        end
        if balance < 0
            changes += 1
            balance = 1
        end
    end
    return changes
end

function main()
    T = parse(Int, readline())
    for _ in 1:T
        S = readline()
        println(solve(S))
    end
end

main()