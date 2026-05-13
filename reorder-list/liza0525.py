# 7기 풀이
# 시간 복잡도: O(n)
# - head 리스트의 길이 만큼의 시간 복잡도가 든다.
# 공간 복잡도: O(1)
# - 변수 몇 개만 사용
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # slow-fast를 이용해서 리스트의 중간 노드를 찾는다
        # fast는 두 칸, slow는 한 칸을 움직이며 fast가 끝 노드에 도달할 때까지 loop를 돌면
        # slow로 중간 노드 찾을 수 있다.
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 중간 노드부터 마지막 노드까지의 리스트를 reversing해준다.
        # prev, curr로 노드 포인터를 잡아 리스트를 뒤집느다.
        prev, curr = None, slow

        while curr:
            next_ = curr.next
            curr.next, prev = prev, curr
            curr = next_
        
        # 원본이었던 head와 prev(중간부터 뒤집은 리스트)를 번갈아 가며 붙여준다.
        # head의 포인터는 first, prev의 포인터는 second로 지정
        first, second = head, prev

        # second의 리스트를 다 돌 때까지 노드를 서로 연결해주면 된다.
        while second.next:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            second = second_next
            first = first_next
