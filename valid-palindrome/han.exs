defmodule Solution do
  @spec is_palindrome(s :: String.t) :: boolean
  def is_palindrome(s) do
    non_alphanumeric_ascii_codes = [?a..?z, ?0..?9] |>
        Enum.reduce([], fn x, acc -> 
            acc ++ (x |> Enum.to_list)
        end)
    converted = s
        |> String.downcase
        |> String.replace(~r/./, fn char ->
            if :binary.first(char) in non_alphanumeric_ascii_codes, do: char, else: ""
        end)

    length = converted |> String.length

    if length < 2, do: true

    center = length |> div(2)

    converted |> String.slice(0..center) ==
        converted
        |> String.slice(-(center+1)..-1)
        |> String.reverse
  end
end
