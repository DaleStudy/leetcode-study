"""
	기억할 키워드
		dummy.next 리턴해서 건너뜀
		list1 list2 둘 중 하나가 None이 되면 while문 끝내고 나머지 next로 이어줌

	list1의 길이 M, list2의 길이N

		TC : O(M + N)

		SC : O(1)

	추가적인 풀이 : 알고달레에서 재귀방법 확인
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node = dummy
        
        while list1 and list2 :
            if list1.val < list2.val :
                node.next = list1
                list1 = list1.next
            else :
                node.next = list2
                list2 = list2.next
            node = node.next
        node.next = list1 or list2
        return dummy.next
