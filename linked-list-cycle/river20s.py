# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # 플로이드 토끼와 거북이 알고리즘
        # 느린 포인터와 빠른 포인터, 사이클이 있다면 
        # 느린 포인터를 빠른 포인터가 따라 잡아 
        # 언젠가 같은 노드에서 만나게 될 것
        # TC: O(N)
        # SC: O(1)
        # 리스트가 비어 있거나 노드가 하나뿐이면 사이클 X
        if not head or not head.next:
            return False

        slow = head # 느린 포인터
        fast = head # 빠른 포인터

        while fast is not None and fast.next is not None: # fast와 fast.next 모두 유효해야 fast.next.next 접근 가능
            slow = slow.next # 느린 포인터 한 칸 이동
            fast = fast.next.next # 빠른 포인터 한 칸 이동

            if slow == fast: # 두 포인터가 만난다면
                return True  # 사이클 존재

        # 루프가 끝났다면 포인터가 리스트 끝에 도달한 것이므로 사이클 X
        return False
