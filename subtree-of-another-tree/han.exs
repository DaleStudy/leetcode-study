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
  @spec is_subtree(root :: TreeNode.t | nil, sub_root :: TreeNode.t | nil) :: boolean
  def is_subtree(root, root), do: true

  def is_subtree(%TreeNode{left: left, right: right}, sub_root) do
    is_subtree(left, sub_root) || is_subtree(right, sub_root)
  end

  def is_subtree(_, _), do: false
end
