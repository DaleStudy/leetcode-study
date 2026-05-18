# 7기 풀이
# 시간 복잡도: O(n)
# - 마지막 노드까지, 모든 노드를 탐색해야 하므로 노드의 개수에 시간 복잡도가 정해짐
# 공간 복잡도: O(n)
# - 재귀 스택이 노드의 개수만큼 쌓임
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # dummy 노드와 next node 설정 및 curr_node로 포인터 지정
        dummy = ListNode()
        dummy.next = head
        curr_node = head

        def dfs(parent, node):
            if not node:
                # 끝에 도달했으므로 카운팅 시작점 0을 return
                # 호출부에서 +1을 하면 마지막 노드가 1이 됨
                return 0

            curr_i = dfs(node, node.next) + 1

            # (뒤로부터 셌을 때의) 현재 노드의 순번이 주어진 n과 같을 때
            if curr_i == n:
                # 부모 노드의 next 노드를, 현재 노드의 next 노드로 변경하여
                # 현재 노드의 연결을 끊는다.
                parent.next = node.next

            return curr_i
        
        dfs(dummy, curr_node)
        return dummy.next
