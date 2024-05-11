# Definition for singly-linked list.
# class ListNode
#     attr_accessor :val, :next
#     def initialize(val)
#         @val = val
#         @next = nil
#     end
# end

# @param {ListNode} head
# @return {Boolean}
def hasCycle(head)
    return false unless head && head.next

    slow = head
    fast = head.next

    loop do
      break true if slow == fast

      slow = slow.next
      fast = fast&.next&.next

      break false unless fast
    end
  end
