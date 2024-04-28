defmodule Solution do
  @spec is_anagram(s :: String.t, t :: String.t) :: boolean
  def is_anagram(s, t) do
    s |> String.split("", trim: true) |> Enum.sort == t |> String.split("", trim: true) |> Enum.sort
  end
end
