"""
Constraints:
- The number of nodes in the list is in the range [1, 5 * 10^4].
- 1 <= Node.val <= 1000

Time Complexity: O(n)
- 리스트를 한 번씩 순회하면서 알고리즘의 각 단계를 수행함

Space Complexity: O(1)
- 정해진 변수 외에는 추가 공간을 사용하지 않음

풀이방법:
1. 중간 지점 찾기
- slow/fast 포인터를 사용하여 중간 지점 찾기
2. 뒷부분 뒤집기
- prev, curr 포인터로 링크드 리스트의 방향 전환
- next_temp에 다음 노드를 저장한 후 방향 변경
3. 앞부분과 뒷부분 합치기
- 두 리스트의 시작점(first, second)부터 시작
- temp1, temp2에 다음 노드 저장
- 포인터들을 번갈아가며 연결함

노트:
- 포인터 조작(연결리스트 뒤집기, 병합)이 어려움. 스택 풀이도 준비해두기.
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 초기 상태: 1->2->3->4->5
        """
        Do not return anything, modify head in-place instead.
        """
        # 1단계: 중간 지점 찾기
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2단계: 뒷부분 뒤집기
        prev = None
        curr = slow.next
        slow.next = None    # 분리: 1->2->3  |  4->5

        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp

        # 3단계: 앞부분과 뒷부분 합치기
        first = head
        second = prev

        while second:
            temp1 = first.next
            temp2 = second.next

            first.next = second
            second.next = temp1

            first = temp1
            second = temp2
