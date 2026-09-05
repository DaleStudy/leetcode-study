"""
# 시간 복잡도: O(n)
# 공간 복잡도: O(1)
#
# 한 번의 순회(one pass)로 연결 리스트의 끝에서 n번째 노드를 제거하는 방법:
# 1. dummy 노드를 만들어 head의 앞에 연결한다.
# 2. forerunner 포인터를 n칸 먼저 이동시킨다.
# 3. forerunner와 lastcomer(초기: dummy)를 같이 한 칸씩 이동하며, forerunner가 끝(None)에 도달하면 lastcomer는 제거할 노드 바로 앞에 위치하게 된다.
# 4. lastcomer.next를 갱신하여 n번째 노드를 제거한다.
"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head

        forerunner = head
        lastcomer = dummy

        for _ in range(n):
            forerunner = forerunner.next

        while forerunner:
            forerunner = forerunner.next
            lastcomer = lastcomer.next

        lastcomer.next = lastcomer.next.next

        return dummy.next
