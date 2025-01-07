class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # 더미 노드 생성
        dummy = ListNode(-1)
        current = dummy

        # 두 리스트를 순회하며 병합
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # 남아 있는 노드 처리
        if list1:
            current.next = list1
        elif list2:
            current.next = list2

        # 더미 노드 다음부터 시작
        return dummy.next

if __name__ == "__main__":
    solution = Solution()

    # test case
    list1 = ListNode(1, ListNode(2, ListNode(4, )))
    list2 = ListNode(1, ListNode(3, ListNode(4, )))

    result = solution.mergeTwoLists(list1, list2)

    while result is not None:
        print(result.val)
        result = result.next






