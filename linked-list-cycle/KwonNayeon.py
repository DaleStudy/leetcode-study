"""
Constraints:
- The number of the nodes in the list is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list

Time Complexity:
- Solution 1: O(n)
- Solution 2: O(n)

Space Complexity:
- Solution 1: O(n) - visited set에 모든 노드를 저장할 수 있음
- Solution 2: O(1) - 추가 메모리 사용하지 않음

풀이방법:
1. 처음엔 직관적인 방법으로 해결, 한 번 마주친 노드를 다시 만나는지를 체크하는 방식
2. slow, fast 두 개의 노드를 활용, 만약 cycle이 존재하는 경우 fast가 slow와 언젠가 만나게 됨, 
  만약 cycle이 없다면 둘은 만나지 않음
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Solution 1: 한 번 마주친 노드를 다시 만나는지를 체크
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

# Solution 2: 두 개의 포인터 이용
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        
        return False

