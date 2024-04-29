defmodule Solution do
    def two_sum([head | tail], target, index\\0) do
        second_index = Enum.find_index(tail, fn element -> 
            head + element == target
        end)

        if second_index, do: [index, second_index + index + 1], else: two_sum(tail, target, index + 1)
    end
end
