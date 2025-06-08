# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 시간복잡도 O(n), 공간복잡도 O(n)
        # Follow up : 공간복잡도 O(1) 방식도 생각해 볼 것.
        
        # 방문한 노드 set으로 저장
        visited = set()

        while head:
            # 방문했던 노드라면 사이클 존재 -> True 리턴
            if head in visited:
                return True

            visited.add(head)   # 방문 노드로 저장
            head = head.next    # 다음 노드로 이동

        return False
