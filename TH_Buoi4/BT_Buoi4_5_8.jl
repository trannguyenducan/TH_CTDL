using Printf

function toPostfix(s::String)::String
    st = []
    for i in length(s):-1:1
        if isalnum(s[i])
            push!(st, string(s[i]))
        else
            op1 = pop!(st)
            op2 = pop!(st)
            push!(st, op1 * op2 * s[i])
        end
    end
    return st[end]
end

function main()
    T = parse(Int, readline())
    for _ in 1:T
        expr = readline()
        println(toPostfix(expr))
    end
end

main()