"""
[문제풀이]
# Inputs
- head of singly linked list
# Outputs
- return the reversed list
# Constraints
- The number of nodes in the list is the range [0, 5000].
- 5000 <= Node.val <= 5000
# Ideas
1. 스택 활용?
첫 head의 노드부터 스택에 넣기
맨 끝 도달하면
스택 pop 하면서 새 리스트 만들기??

마지막 요소를 인식 못하나?

[회고]

"""
# 첫 제출

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        ret = ListNode()
        ret_head = ret
        st = []

        while True:
            # 왜 마지막 요소일 때 안나가지고 자꾸 NoneType object has no attribute 'val' 오류 뜸
            st.append(head.val)
            if head.next is None:
                break
            head = head.next

        while st:
            val = st.pop()
            node = ListNode(val, None)
            ret_head.next = node
            ret_head = ret_head.next

        return ret.next

# gpt 답변

## 스택 유지
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        st = []
        while head:
            st.append(head.val)
            head = head.next

        dummy = ListNode(0)
        current = dummy

        while st:
            current.next = ListNode(st.pop())
            current = current.next

        return dummy.next

## 스택 없이 포인터를 뒤집는 방식
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        return prev

