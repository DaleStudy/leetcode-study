defmodule Solution do
  @spec climb_stairs(n :: integer) :: integer
  def climb_stairs(n) do
      do_climb_stairs(n, 1, 0, 1)
  end

  defp do_climb_stairs(n, n, n_1, n_2), do: n_1 + n_2

  defp do_climb_stairs(n, step, n_1, n_2) do
    do_climb_stairs(n, step + 1, n_2, n_1 + n_2)
  end
end
