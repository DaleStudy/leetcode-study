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
    @spec merge_two_lists(list1 :: ListNode.t | nil, list2 :: ListNode.t | nil) :: ListNode.t | nil
  def merge_two_lists(nil, nil), do: nil
  def merge_two_lists(nil, list2), do: list2
  def merge_two_lists(list1, nil), do: list1

  def merge_two_lists(list1, list2) when list1.val >= list2.val do
    %ListNode{list2 | next: merge_two_lists(list1, list2.next)}
  end

  def merge_two_lists(list1, list2) do
    %ListNode{list1 | next: merge_two_lists(list1.next, list2)}
  end
end
