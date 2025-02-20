class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Intuition:
            nodes 리스트에 모든 노드를 저장한다.
            현재 노드가 -i - 1번째 노드일 때,
            현재 노드의 next는 head의 next로 설정하고,
            head의 next는 현재 노드로 설정한다.
            이후 마지막에 중간에 있는 노드를 None으로 설정한다.

        Time Complexity:
            O(N):
                모든 노드를 순회하므로 O(N)이다.

        Space Complexity:
            O(N):
                모든 노드를 nodes 리스트에 저장하므로 O(N)이다.
        """
        nodes = []
        node = head
        while node:
            nodes.append(node)
            node = node.next

        for i in range((len(nodes) - 1) // 2):
            cur = nodes[-i - 1]
            cur.next = head.next
            head.next = cur
            head = cur.next

        nodes[len(nodes) // 2].next = None
