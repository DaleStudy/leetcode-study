# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoListsList(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
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

    def mergeTwoListsNode(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Intuition:
            파이썬 리스트를 사용하지 않고
            주어진 ListNode로부터 바로 시작한다.

        Time Complexity:
            O(N):
                두개의 리스트를 1번 순회하며 답을 찾으므로,
                O(N)의 시간복잡도가 소요된다.

        Space Complexity:
            O(1):
                ListNode를 바로 사용하므로
                상수 만큼의 O(1)의 공간복잡도가 소요된다.

        Key takeaway:
            링크드 리스트를 오랜만에 접하니 잘 풀지 못했던 것 같다.
            전통적인 자료구조를 OOP 관점으로 고민해보자.
        """
        sorted_node = ListNode()
        current_node = sorted_node

        while True:
            if list1 is None:
                current_node.next = list2
                break
            elif list2 is None:
                current_node.next = list1
                break

            if list1.val < list2.val:
                current_node.next = ListNode(list1.val)
                current_node = current_node.next
                list1 = list1.next
            else:
                current_node.next = ListNode(list2.val)
                current_node = current_node.next
                list2 = list2.next

        return sorted_node.next
