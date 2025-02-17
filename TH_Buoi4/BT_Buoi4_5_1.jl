using Printf

function hasRedundantParentheses(exp::String)::Bool
    st = []
    
    for ch in exp
        if ch == ')'
            top = pop!(st)
            isRedundant = true
            
            while !isempty(st) && top != '('
                if top in ('+', '-', '*', '/')
                    isRedundant = false
                end
                top = pop!(st)
            end
            
            if isRedundant
                return true
            end
        else
            push!(st, ch)
        end
    end
    return false
end

function main()
    T = parse(Int, readline())
    
    for _ in 1:T
        exp = readline()
        
        if hasRedundantParentheses(exp)
            println("Yes")
        else
            println("No")
        end
    end
end

main()