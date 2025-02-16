# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Intuition:
            노드마다 고유한 id를 저장하고 중복되는 id가 있다면
            True를 반환한다. 그 외에는 False이다.

        Time Complexity:
            O(N):
                각 노드를 한번씩 스캔하므로 O(N)이 소요된다.

        Space Complexity:
            O(N):
                각 노드의 id를 저장하므로 O(N)이 소요된다.
        """
        node_ids = []
        node = head
        answer = False
        while node:
            node_id = id(node)
            if node_id not in node_ids:
                node_ids.append(node_id)
            else:
                answer = True
                break
            node = node.next

        return answer
