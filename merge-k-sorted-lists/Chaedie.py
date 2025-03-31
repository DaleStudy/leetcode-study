"""
Solution:
    1) 모든 linked list 의 value 를 arr에 담는다.
    2) arr 를 정렬한다.
    3) arr 로 linked list 를 만든다.

Time: O(n log(n)) = O(n) arr 만들기 + O(n log(n)) 정렬하기 + O(n) linked list 만들기
Space: O(n)
"""


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for linked_list in lists:
            while linked_list:
                arr.append(linked_list.val)
                linked_list = linked_list.next

        dummy = ListNode()
        node = dummy

        arr.sort()
        for num in arr:
            node.next = ListNode(num)
            node = node.next
        return dummy.next
