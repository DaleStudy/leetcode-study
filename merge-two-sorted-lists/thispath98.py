# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            두 리스트의 원소를 각각 비교하면서 한번씩 스캔한다.
            결과적으로 한번씩만 스캔하면 정렬할 수 있다.

        Time Complexity:
            O(N):
                두개의 리스트를 1번 순회하며 답을 찾으므로,
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(N):
                sorted_list에 정렬된 배열을 저장하므로,
                O(N)의 공간복잡도가 소요된다.
        """
        sorted_list = []
        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                sorted_list.append(list1.val)
                list1 = list1.next
            else:
                sorted_list.append(list2.val)
                list2 = list2.next

        while list1 is not None:
            sorted_list.append(list1.val)
            list1 = list1.next
        while list2 is not None:
            sorted_list.append(list2.val)
            list2 = list2.next

        sorted_node = None
        while sorted_list:
            val = sorted_list.pop()
            sorted_node = ListNode(val, sorted_node)

        return sorted_node
