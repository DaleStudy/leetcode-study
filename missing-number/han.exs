defmodule Solution do
  @spec missing_number(nums :: [integer]) :: integer
  def missing_number(nums) do
    (0..length(nums) |> Enum.to_list) -- nums |> Enum.at(0)
  end
end
