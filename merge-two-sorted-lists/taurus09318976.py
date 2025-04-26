# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        # 더미 노드 생성
        dummy = ListNode()
        current = dummy
        
        # 두 리스트가 모두 존재하는 동안 반복
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 남은 노드들 연결
        if list1:
            current.next = list1
        else:
            current.next = list2
            
        return dummy.next

# 테스트 코드
def create_linked_list(lst):
    if not lst:
        return None
    head = ListNode(lst[0])
    current = head
    for val in lst[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# 테스트 케이스
solution = Solution()

# 테스트 케이스 1
list1 = create_linked_list([1,2,4])
list2 = create_linked_list([1,3,4])
result = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(result))  # [1,1,2,3,4,4]

# 테스트 케이스 2
list1 = create_linked_list([])
list2 = create_linked_list([])
result = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(result))  # []

# 테스트 케이스 3
list1 = create_linked_list([])
list2 = create_linked_list([0])
result = solution.mergeTwoLists(list1, list2)
print(linked_list_to_list(result))  # [0]

