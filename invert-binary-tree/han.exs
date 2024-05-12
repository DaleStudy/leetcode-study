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
  @spec invert_tree(root :: TreeNode.t | nil) :: TreeNode.t | nil
  def invert_tree(nil), do: nil

  def invert_tree(root) do
    invert(root, root.left, root.right)
  end

  defp invert(parent, nil, nil), do: parent

  defp invert(parent, left, nil) do
    %TreeNode{parent | left: nil, right: invert(left, left.left, left.right)}
  end

  defp invert(parent, nil, right) do
    %TreeNode{parent | left: invert(right, right.left, right.right), right: nil}
  end

  defp invert(parent, left, right) do
    tmp = left

    %TreeNode{parent |
      left: invert(right, right.left, right.right),
      right: invert(tmp, tmp.left, tmp.right)}
  end
end
