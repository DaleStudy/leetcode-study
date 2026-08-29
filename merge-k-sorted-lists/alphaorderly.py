"""
시간복잡도: O(n log k)
공간복잡도: O(k)
- k는 연결 리스트의 개수, n은 모든 노드의 개수

- 각 연결 리스트의 첫 번째 노드 값을 (값, 인덱스) 형태로 힙에 추가한다.
- 힙에서 가장 작은 값을 꺼내 결과 더미 연결 리스트에 노드로 연결한다.
- 꺼낸 노드가 속했던 리스트의 다음 노드가 있으면 힙에 추가한다.
- 힙이 빌 때까지 위 과정을 반복한다.
- 더미 연결 리스트의 다음 노드를 반환한다.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ans = ListNode()
        head = ans

        values = [(node.val, index) for index, node in enumerate(lists) if node]
        heapify(values)

        while values:
            _, index = heappop(values)

            head.next = lists[index]
            head = head.next

            lists[index] = lists[index].next
            if lists[index]:
                heappush(values, (lists[index].val, index))

        return ans.next
