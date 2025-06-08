"""
Constraints:
- The number of the nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list


<Solution 1>

Time Complexity: O(n)
- while 루프를 최대 n번 실행 (노드의 개수만큼)

Space Complexity: O(n)
- visited set에 최대 n개의 노드 저장함
- set() 조회/삽입에 O(1)

풀이 방법:
- 한 번 마주친 노드를 다시 만나는지를 체크하는 방식
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited = set()

        current = head
        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False

"""
<Solution 2>

Time Complexity: O(n)
- while 루프를 최대 n번 실행 (노드의 개수만큼)

Space Complexity: O(1)
- 투 포인터 이외의 추가 메모리 사용하지 않음

풀이 방법:
- 투 포인터 방식 (slow, fast)
- 만약 cycle이 있다면, fast가 slow와 언젠가 만나게 됨
- cycle이 없다면 둘은 만나지 않음
"""
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False
