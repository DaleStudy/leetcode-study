defmodule Solution do
  @spec three_sum(nums :: [integer]) :: [[integer]]
  def three_sum(nums) do
    length_of_nums = length nums
    num_index_map = nums |> Enum.with_index |> Map.new
    frequencies_of_num = nums |> Enum.frequencies()
    tuple_nums = nums |> List.to_tuple
    num_indexs_map = nums |>
      Enum.with_index() |>
      Enum.group_by(fn {v, _} -> v end, fn {_, i} -> i end)

    Stream.unfold({0, 1}, fn {i, j} ->
      if j < length_of_nums - 1,
      do: {{i, j}, {i, j + 1}},
      else: {{i, j}, {i + 1, i + 2}}
    end) |>
      Stream.take_while(fn {i, _} ->
        i < length_of_nums - 1
      end) |>
      Stream.map(fn {i, j} ->
        a = elem tuple_nums, i
        b = elem tuple_nums, j
        c = -(a + b)

        case frequencies_of_num[c] do
          nil -> nil
          count when count >= 3 -> [a, b, c] |> Enum.sort()
          _ ->
            if num_indexs_map[c] |> Enum.filter(& &1 != i && &1 != j) |> Enum.at(0),
            do: [a, b, c] |> Enum.sort(),
            else: nil
        end
      end) |>
      Stream.reject(& &1 == nil) |>
      Stream.uniq |>
      Enum.to_list
  end
end
