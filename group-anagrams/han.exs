defmodule Solution do
  @spec group_anagrams(strs :: [String.t]) :: [[String.t]]
  def group_anagrams(strs) do
    Enum.group_by(strs, &(String.codepoints(&1) |> Enum.sort)) |> Map.values
  end
end

# 최초엔 아래 코드로 시도했으나 strs.length가 커지면 시간초과...
#
# defmodule Solution do
#   @spec group_anagrams(strs :: [String.t]) :: [[String.t]]
#   def group_anagrams(strs) when length(strs) < 2, do: [strs]
#   def group_anagrams([], res), do: res

#   def group_anagrams([head|tail], res \\ []) do
#     split_sort_head = split_sort(head)
#     anagrams = Enum.reduce(tail, [head], fn x, acc ->
#       if split_sort(x) == split_sort_head do
#         acc ++ [x]
#       else
#         acc
#       end
#     end)

#     group_anagrams(tail -- anagrams, [anagrams|res])
#   end

#   defp split_sort(str) do
#     String.graphemes(str) |> Enum.sort_by(&(&1), :asc)
#   end
# end
