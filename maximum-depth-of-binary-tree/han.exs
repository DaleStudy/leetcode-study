# Definition for a binary tree node.
#
# defmodule TreeNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           left: TreeNode.t() | nil,
#           right: TreeNode.t() | nil
#         }
#   defstruct val: 0, left: nil, right: nil
# end

defmodule Solution do
  @spec max_depth(root :: TreeNode.t | nil) :: integer
  def max_depth(nil, max_depth), do: max_depth

  def max_depth(%TreeNode{left: left, right: right}, max_depth \\ 0) do
    Enum.max([max_depth(left, max_depth + 1), max_depth(right, max_depth + 1)])
  end
end
