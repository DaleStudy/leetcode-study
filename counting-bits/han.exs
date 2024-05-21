defmodule Solution do
  @spec count_bits(n :: integer) :: [integer]
  def count_bits(n) do
    Enum.map(0..n, fn i ->
      Integer.digits(i, 2) |> Enum.count(&(&1 != 0))
    end)
  end
end
