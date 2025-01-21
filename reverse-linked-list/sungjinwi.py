"""
	풀이 : 
		cur의 next를 tmp로 저장해놓고 cur의 next를 prv로 바꾼 후 tmp를 통해 다음 노드로 이동

	링크드리스트 길이 n

	TC : O(N)

	SC : O(1)
		prv, cur 두 개만 사용하므로 O(1)

	- stack에 넣어서 reverse할 수도 있음
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prv = None
        cur = head
        while cur :
            tmp = cur.next
            cur.next = prv
            prv = cur
            cur = tmp
        return prv
