"""TC: O(n), SC: -

n은 주어진 두 리스트의 길이 중 큰 값

아이디어:
- 주어진 조건에 의해 두 리스트에 들어있는 값들은 non-decreasing이므로, 새로운 리스트를 만들고
  두 리스트의 앞에 있는 값 중 작은 값을 하나씩 뽑아서 더해주면 된다.
- 빈 리스트가 주어질 수 있는 것만 유의하자.

SC:
- 특별히 관리하는 값이 없다.

TC:
- 모든 노드에 한 번씩 접근해서 리턴할 값에 이어준다. 이어주는 시행마다 O(1).
- 리턴할 값에 새 노드를 추가할 때마다 값 비교를 한 번씩 한다. O(1).
- n이 두 리스트 길이 중 큰 값이므로 이어주는 시행은 x는 n <= x <= 2*n 만족.
- 즉, 총 O(n).
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        # 1. init head
        # - 두 리스트를 보고 혹시 하나라도 비어있으면 다른 리스트를 리턴한다.
        # - 둘 다 비어있지 않을 경우 첫 아이템을 보고 둘 중 작은 값을 결과물의 첫 아이템으로 씀.
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        # 여기 도달했으면 둘 다 최소한 한 아이템씩은 존재.
        sol = None
        if list1.val < list2.val:
            sol = ListNode(list1.val)
            list1 = list1.next
        else:
            sol = ListNode(list2.val)
            list2 = list2.next

        sol_head = sol

        # 2. add item
        # - 앞의 과정을 비슷하게 반복한다.
        while True:
            # 언젠가 둘 중 한 리스트는 비게 되므로 무한 루프를 돌지 않는다.
            if list1 is None:
                sol_head.next = list2
                return sol
            if list2 is None:
                sol_head.next = list1
                return sol

            if list1.val < list2.val:
                sol_head.next = ListNode(list1.val)
                list1 = list1.next
            else:
                sol_head.next = ListNode(list2.val)
                list2 = list2.next

            sol_head = sol_head.next
