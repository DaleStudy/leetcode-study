defmodule Solution do
  @spec top_k_frequent(nums :: [integer], k :: integer) :: [integer]
  def top_k_frequent(nums, k) do
    nums |>
      Enum.frequencies |>
      Enum.sort_by(fn {_, v} -> v end, :desc) |>
      Enum.take(k) |>
      Enum.map(fn {k, _} -> k end)
  end
end
