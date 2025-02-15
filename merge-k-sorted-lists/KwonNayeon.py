"""
Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4

Time Complexity: O(N log k)
- N은 모든 노드의 총 개수, k는 연결 리스트의 개수
- 힙 연산에 log k 시간이 걸리고, 이를 N번 수행함

Space Complexity: O(k)
- 힙에는 항상 k개의 노드만 저장됨

풀이방법:
1. 최소 힙을 사용하여 k개의 정렬된 리스트를 효율적으로 병합하는 알고리즘
2. 각 리스트의 첫 번째 노드를 힙에 넣고 시작함
3. 힙에서 가장 작은 값을 가진 노드를 꺼내서 결과 리스트에 추가
4. 꺼낸 노드의 다음 노드를 다시 힙에 넣음
5. 이 과정을 힙이 빌 때까지 반복함

Note: 이 문제는 풀기 어려워서 풀이를 보고 공부했습니다. 복습 필수
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        min_heap = []
        
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))
                
        head = point = ListNode(0)
        
        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            point.next = node
            point = point.next
            
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))
                
        return head.next
