using Printf

function precedence(op::Char)::Int
    if op == '+' || op == '-'
        return 1
    elseif op == '*' || op == '/'
        return 2
    else
        return 0
    end
end

function toPostfix(s::String)::String
    ops = []
    res = ""
    for c in s
        if isalnum(c)
            res *= c
        elseif c == '('
            push!(ops, c)
        elseif c == ')'
            while !isempty(ops) && ops[end] != '('
                res *= pop!(ops)
            end
            pop!(ops)
        else
            while !isempty(ops) && precedence(ops[end]) >= precedence(c)
                res *= pop!(ops)
            end
            push!(ops, c)
        end
    end
    while !isempty(ops)
        res *= pop!(ops)
    end
    return res
end

function main()
    T = parse(Int, readline())
    for _ in 1:T
        expr = readline()
        println(toPostfix(expr))
    end
end

main()