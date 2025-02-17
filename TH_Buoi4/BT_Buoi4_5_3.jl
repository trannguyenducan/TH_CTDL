using Printf

function simplify(s::String)::String
    ops = [true]
    res = ""
    for i in 1:length(s)
        if s[i] == '('
            if i > 1 && s[i - 1] == '-'
                push!(ops, !ops[end])
            else
                push!(ops, ops[end])
            end
        elseif s[i] == ')'
            pop!(ops)
        elseif s[i] == '+' || s[i] == '-'
            if ops[end]
                res *= s[i]
            else
                res *= (s[i] == '+' ? '-' : '+')
            end
        else
            res *= s[i]
        end
    end
    return res
end

function main()
    T = parse(Int, readline())
    for _ in 1:T
        P = readline()
        println(simplify(P))
    end
end

main()