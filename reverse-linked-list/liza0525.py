class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre_node, curr_node = None, head
        while curr_node:
            temp = curr_node.next
            curr_node.next = pre_node
            pre_node, curr_node = curr_node, temp
        return pre_node


# 7기 풀이
# 시간 복잡도: O(n)
# - 링크드 리스트의 길이만큼 탐색
# 공간 복잡도: O(1)
# - 결과 변수 이외에는 curr_node 변수만 사용
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev_node, curr_node = None, head

        while curr_node:
            # next를 먼저 저장해두지 않으면 링크를 끊은 뒤 다음 노드를 잃어리므로 temp에 저장
            temp = curr_node.next

            # curr_node의 다음 노드로 prev_node를 저장
            curr_node.next = prev_node
            
            # prev_node와 curr_node에 각각 curr_node와 temp 노드를 저장하여 순서 바꾸기
            prev_node, curr_node = curr_node, temp

        return prev_node

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
