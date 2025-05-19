"""
Time complexity O(n+m)
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2):
            return list1 or list2 # if empty list

        nums = []
        while(list1 or list2):
            if not list1:
                val = list2.val
                list2 = list2.next
            elif not list2:
                val = list1.val
                list1 = list1.next
            else:
                if list1.val <= list2.val:
                    val = list1.val
                    list1 = list1.next
                else:
                    val = list2.val
                    list2 = list2.next
            nums.append(val)
        
        head = ListNode(nums[0])
        node = head
        if len(nums) == 1:
            return head
        for n in nums[1:]:
            tmp = ListNode(n)
            node.next = tmp
            node = tmp
        return head
