defmodule Solution do
  @spec hamming_weight(n :: integer) :: integer
  def hamming_weight(n) do
    Integer.to_string(n, 2) |> String.graphemes |> Enum.count(& &1 != "0")
  end
end
