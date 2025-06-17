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
- 포인터 조작(연결리스트 뒤집기, 병합) 방법을 다 까먹어서 복습용 예시 주석을 추가해둠
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 초기 상태: 1->2->3->4->5
        
        # 1단계: 중간 지점 찾기
        slow = head         # slow = 1
        fast = head         # fast = 1
        while fast and fast.next:
            slow = slow.next    # slow: 1->2->3
            fast = fast.next.next   # fast: 1->3->5->None
        # 결과: slow는 3에 위치
        
        # 2단계: 뒷부분 뒤집기
        prev = None         # prev = None
        curr = slow.next    # curr = 4 (뒷부분 시작점)
        slow.next = None    # 분리: 1->2->3  |  4->5
        
        while curr:
            # 1회전: curr=4, prev=None
            next_temp = curr.next   # next_temp = 5
            curr.next = prev        # 4->None
            prev = curr             # prev = 4
            curr = next_temp        # curr = 5
            # 상태: 1->2->3  |  4->None, curr=5
            
            # 2회전: curr=5, prev=4
            next_temp = curr.next   # next_temp = None
            curr.next = prev        # 5->4
            prev = curr             # prev = 5
            curr = next_temp        # curr = None (종료)
            # 상태: 1->2->3  |  5->4->None
        
        # 3단계: 앞부분과 뒷부분 합치기
        first = head        # first = 1->2->3
        second = prev       # second = 5->4
        
        while second:
            # 1회전: first=1, second=5
            temp1 = first.next      # temp1 = 2
            temp2 = second.next     # temp2 = 4
            
            first.next = second     # 1->5
            second.next = temp1     # 5->2
            # 현재 상태: 1->5->2->3, 남은 second = 4
            
            first = temp1           # first = 2
            second = temp2          # second = 4
            
            # 2회전: first=2, second=4
            temp1 = first.next      # temp1 = 3
            temp2 = second.next     # temp2 = None
            
            first.next = second     # 2->4
            second.next = temp1     # 4->3
            # 현재 상태: 1->5->2->4->3
            
            first = temp1           # first = 3
            second = temp2          # second = None (종료)
        
        # 최종 결과: 1->5->2->4->3
