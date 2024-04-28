defmodule Solution do
  @spec max_profit(prices :: [integer]) :: integer
  def max_profit([head | tail]) do
        {_, answer} = Enum.reduce(tail, {head, 0}, fn x, {buy, profit} ->
            {min(buy, x), max(profit, x - buy)}
        end)

        answer
    end
end
