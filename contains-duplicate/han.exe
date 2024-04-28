defmodule Solution do
  @spec contains_duplicate(nums :: [integer]) :: boolean
  def contains_duplicate(nums) do
    if nums |> Enum.into(MapSet.new) |> Enum.to_list |> length == length(nums) do
        false
    else
        true
    end
  end
end
