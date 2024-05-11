defmodule Solution do
  def is_valid(s) when byte_size(s) > 1 do
    brackets = %{")" => "(", "}" => "{", "]" => "["}
    opens = ["[", "{", "("]

    result = Enum.reduce_while(String.graphemes(s), [], fn x, acc ->
      cond do
        x in opens ->
          {:cont, List.insert_at(acc, -1, x)}
        brackets[x] == List.last(acc) ->
          {:cont, List.delete_at(acc, -1)}
        true ->
          {:halt, List.insert_at(acc, -1, x)}
      end
    end)

    length(result) < 1
  end

  def is_valid(_), do: false
end
