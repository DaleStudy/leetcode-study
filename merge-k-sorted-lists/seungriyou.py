# https://leetcode.com/problems/merge-k-sorted-lists/

from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        [Complexity]
            - TC: O(mlogn) (n = len(lists), m = node의 전체 개수)
            - SC: O(n) (min heap)

        [Approach]
            각각 이미 sorted인 linked list들을 하나의 sorted linked list로 merge 하는 것이므로,
            주어진 각각의 linked list에서 node 하나씩을 꺼내어 보며 그 값을 비교하면 된다.
            이때, 길이가 n(= len(lists))인 min heap을 사용하면 각 linked list에서의 node 하나씩을 담아 최솟값을 가진 node를 O(logn)에 pop 할 수 있게 된다.
            다만, min heap에 node만 넣으면 비교할 수 없으므로, 다음과 같이 구성된 tuple을 min heap에 넣는다.
            (* 파이썬에서 tuple 끼리 비교할 때는 앞 원소부터 차례로 비교되며, 앞 원소에서 값이 동일하면 다음 원소로 넘어간다.)
                (value, index in lists, node)
                    - value: 가장 먼저 value를 비교하도록 한다.
                    - index in lists: 만약 value가 서로 같은 상황이라면 더이상 최솟값을 고르기 위한 비교가 진행되지 않도록 unique한 값인 lists에서의 index로 비교하도록 한다.
                                      실제로 사용되는 값은 아니나, node 끼리 비교가 불가능하므로 사용한다.
                    - node: 결과 merged linked-list에 넣기 위해 실물 node가 필요하며, next node를 min heap에 넣을 때 필요하다.
        """
        import heapq

        # 주어진 각 linked list의 첫 node를 min heap에 넣기
        q = [(node.val, i, node) for i, node in enumerate(lists) if node]
        heapq.heapify(q)  # list를 먼저 완성하고 heapify하면 O(n)

        res = curr = ListNode()

        while q:
            # 최솟값을 가진 node 추출
            value, i, node = heapq.heappop(q)

            # res에 node 추가
            curr.next = node
            curr = curr.next

            # node의 다음 노드를 min heap에 넣어주기
            if node.next:
                heapq.heappush(q, (node.next.val, i, node.next))

        return res.next
