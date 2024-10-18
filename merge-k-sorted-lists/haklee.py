"""TC: O(n*log(l)), SC: O(l)

l은 리스트 개수, n은 전체 아이템 개수

아이디어:
- 각 리스트에서 제일 앞에 있는 값을 뽑아서 우선순위 큐에 넣는다.
- 우선순위 큐의 제일 앞에 있는 값을 뽑아서
    - 이 값이 어느 리스트에서 나왔는지 확인해서 해당 리스트의 제일 앞에 있는 값을 새로 뽑아서 우선순위 큐를 채운다.
    - 우선순위 큐에서 뽑은 값은 결과 리스트에 더한다.

SC:
- 우선순위 큐에 최대 list의 개수 만큼의 아이템 존재 가능. O(l).
- 

TC:
- heap 크기는 최대 l이다.
- 이 heap에 아이템을 push하고 pop할때 O(log(l)) 시간 소요.
- 위의 시행을 전체 아이템 개수 만큼 한다.
- 종합하면 O(n*log(l))
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        head = ListNode()
        tail = head

        # init
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next

        # process
        while heap:
            v, idx = heappop(heap)

            # heap 다시 채워넣기
            if lists[idx]:
                heappush(heap, (lists[idx].val, idx))
                lists[idx] = lists[idx].next

            # 결과물 채워넣기
            tail.next = ListNode(v)
            tail = tail.next

        return head.next
