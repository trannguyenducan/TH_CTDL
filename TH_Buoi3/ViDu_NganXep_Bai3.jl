import Base: push!, pop! # Import ca hai phuong thuc

mutable struct Stack
    elements::Vector{Any}
    Stack() = new(Vector{Any}())
end

function push!(s::Stack, item)
    push!(s.elements, item) # Su dung push! truc tiep voi s.elements
    println("Da them '$item' vao ngan xep.")
end

function pop!(s::Stack)
    if !isempty(s.elements)
        item = pop!(s.elements) # Su dung pop! truc tiep voi s.elements
        println("Da lay '$item' ra khoi ngan xep.")
        return item
    else
        println("Ngan xep rong.")
        return nothing
    end
end

function peek(s::Stack)
    if !isempty(s.elements)
        return s.elements[end]
    else
        println("Ngan xep trong.")
        return nothing
    end
end

function is_empty(s::Stack)
    return isempty(s.elements)
end

function Base.display(s::Stack) # Them Base. prefix cho display
    println("Ngan xep (dinh den day): ", reverse(s.elements))
end

function main()
    stack = Stack()
    push!(stack, "Sach A")
    push!(stack, "Sach B")
    push!(stack, "Sach C")
    display(stack)

    top_item = peek(stack)
    println("Phan tu dinh cua ngan xep: ", top_item)

    pop!(stack)
    display(stack)

    println("Ngan xep co trong khong?", is_empty(stack) ? "Co." : "Khong.")
end

main()