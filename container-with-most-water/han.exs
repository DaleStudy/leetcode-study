defmodule Solution do
  @spec max_area(height :: [integer]) :: integer
  def max_area(heights) do
    List.to_tuple(heights) |> max_area(0, length(heights) - 1, 0)
  end

  defp max_area(_, left_pointer, right_pointer, answer) when left_pointer == right_pointer, do: answer

  defp max_area(heights, left_pointer, right_pointer, answer) do
    lh = elem(heights, left_pointer)
    rh = elem(heights, right_pointer)
    height = min(lh, rh)
    width = right_pointer - left_pointer

    new_max_area = max(answer, height * width)
    cond do
      lh < rh ->
        max_area(heights, left_pointer + 1, right_pointer, new_max_area)
      true ->
        max_area(heights, left_pointer, right_pointer - 1, new_max_area)
    end
  end
end
