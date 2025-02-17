using Printf

function toInfix(s::String)::String
    st = []
    for c in s
        if isalnum(c)
            push!(st, string(c))
        else
            op2 = pop!(st)
            op1 = pop!(st)
            push!(st, "($op1$c$op2)")
        end
    end
    return st[end]
end

function main()
    T = parse(Int, readline())
    for _ in 1:T
        expr = readline()
        println(toInfix(expr))
    end
end

main()