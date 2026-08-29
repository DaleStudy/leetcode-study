
"""
시간복잡도: O(n)
공간복잡도: O(1)

1. 토끼와 거북이를 초기화한다.
  - 토끼 : 두 칸씩 이동
  - 거북이 : 한 칸씩 이동
2. 토끼와 거북이가 만날 때까지 이동한다.
3. 토끼와 거북이가 만나면 사이클이 있다고 판단한다.
4. 토끼와 거북이가 만나지 않으면 사이클이 없다고 판단한다.

# 원리 #
- 사이클이 존재하지 않는다면 토끼와 거북이는 결국 끝에 도달한다.
- 사이클이 존재한다면 토끼와 거북이는 결국 사이클 내에서 만난다.
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hare = head
        tortoise = head

        while hare and hare.next:
            hare = hare.next.next
            tortoise = tortoise.next

            if hare is tortoise:
                return True

        return False
