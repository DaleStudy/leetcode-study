import heapq

# 7기 풀이
# 시간 복잡도: O(n log k)
# - while문의 매 루프마다 최소힙 계산(리스트의 개수 k에 입각) * 전체 노드 수(n) 만큼 최대 시간복잡도 나옴
# 공간 복잡도: O(k)
# - 리스트의 개수(k) 만큼의 heap 사이즈가 나옴
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        head = dummy  # 초기 head를 dummy로 지정

        heap = []  # 최소힙 계산을 위한 heap

        # 먼저 힙에 노드를 push
        for i, node in enumerate(lists):
            if node:
                # heap push 기준은 node.val과 node가 위치한 index를 기준으로
                heapq.heappush(heap, (node.val, i, node))

        # heap의 모든 노드를 pop할 때까지 while 루프 돌린다
        while heap:
            _, i, node = heapq.heappop(heap)  # 최소값이 들어있는 node를 pop
            head.next = node  # head의 next에 현재의 node를 저장 후
            head = head.next  # head 다음 노드로 변경

            if node.next:
                # node에 next 노드가 있었다면 해당 노드의 val을 기준으로 heap에 push한다
                heapq.heappush(heap, (node.next.val, i, node.next))

        # dummy 노드였으므로 next node를 return
        return dummy.next
