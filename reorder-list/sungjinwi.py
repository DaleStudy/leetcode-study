"""
    풀이 :
        list를 순회하면서 deque에 저장하고 순차적으로 앞, 뒤에서 pop하면서 다시 잇는다

        - 마지막 노드의 next를 None으로 할당해줄 것

    Node 개수 : N
    
    TC : O(N)

    SC : O(N)
"""

from collections import deque

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        tmp = head
        save = deque()

        while tmp:
            save.append(tmp)
            tmp = tmp.next
        
        dummy = ListNode(-1)
        tmp = dummy
        while save:
            tmp.next = save.popleft()
            tmp = tmp.next
            if (save):
                tmp.next = save.pop()
                tmp = tmp.next
        tmp.next = None

        head = dummy.next
