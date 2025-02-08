"""
    풀이 :
        set에 지나온 node를 저장하고 새 node로 이동하면 set안에 존재하는지 확인
        이미 존재하는 node를 지나면 True
        None에 도달하면 False
    
        노드의 길이 = n

    TC : O(N)

    SC : O(N)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()
        while head :
            if head in visited :
                return True
            else :
                visited.add(head)
            head = head.next
        return False
