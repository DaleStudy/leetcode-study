# Definition for singly-linked list.
#
# defmodule ListNode do
#   @type t :: %__MODULE__{
#           val: integer,
#           next: ListNode.t() | nil
#         }
#   defstruct val: 0, next: nil
# end

defmodule Solution do
  def reverse_list(head) when is_nil(head), do: nil

  @spec reverse_list(head :: ListNode.t | nil) :: ListNode.t | nil
  def reverse_list(head, arr \\ [])  do
    new_arr = List.insert_at(arr, -1, head.val)
    if head.next do
      reverse_list(head.next, new_arr)
    else
      Enum.reduce(tl(new_arr), %ListNode{val: hd(new_arr), next: nil}, fn x, acc ->
        %ListNode{val: x, next: acc}
      end)
    end
  end
end
