using Printf

function normalize(s::String)::String
    st = []
    res = ""
    for c in s
        if c == '(' || c == '-'
            push!(st, c)
        elseif c == ')'
            if !isempty(st) && st[end] == '-'
                res *= '-'
            end
            pop!(st)
        else
            if !isempty(st) && st[end] == '-'
                if c == '+'
                    res *= '-'
                elseif c == '-'
                    res *= '+'
                else
                    res *= c
                end
            else
                res *= c
            end
        end
    end
    return res
end

function main()
    T = parse(Int, readline())
    for _ in 1:T
        P1 = readline()
        P2 = readline()
        println(normalize(P1) == normalize(P2) ? "YES" : "NO")
    end
end

main()