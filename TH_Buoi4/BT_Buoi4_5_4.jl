using Printf

results = Set{String}()

function generate(s::String, index::Int, open::Int, close::Int, current::String)
    if index == length(s) + 1
        if open == close
            push!(results, current)
        end
        return
    end
    if s[index] == '('
        generate(s, index + 1, open + 1, close, current * '(')
        generate(s, index + 1, open, close, current)
    elseif s[index] == ')'
        if close < open
            generate(s, index + 1, open, close + 1, current * ')')
        end
        generate(s, index + 1, open, close, current)
    else
        generate(s, index + 1, open, close, current * s[index])
    end
end

function main()
    expression = readline()
    generate(expression, 1, 0, 0, "")
    for res in results
        println(res)
    end
end

main()