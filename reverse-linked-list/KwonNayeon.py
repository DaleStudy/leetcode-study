"""
Constraints:
- The number of nodes in the list is the range [0, 5000]
- -5000 <= Node.val <= 5000

<Solution 1>

Time Complexity: O(n)
- n은 linked list의 노드 수
- 리스트를 한 번 순회하면서 각 노드를 한 번씩만 방문

Space Complexity: O(1)
- 추가 공간으로 prev, curr, temp 세 개의 포인터만 사용
- 입력 크기와 관계없이 일정한 추가 공간만 사용함

풀이 방법:
1. 세 개의 포인터를 사용하여 리스트를 순회하면서 뒤집기
   - prev: 이전 노드를 가리키는 포인터
   - curr: 현재 노드를 가리키는 포인터
   - temp: 다음 노드를 임시 저장하는 포인터

2. 각 단계에서:
   - 다음 노드 임시 저장 (temp)
   - 현재 노드의 next를 이전 노드로 변경
   - 포인터들을 한 칸씩 전진

3. 참고:
   - 포인터들의 이동 순서가 중요
   - prev가 새로운 head가 됨
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr is not None:

            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
    
"""
<Solution 2>

Time Complexity: O(n)
- 스택에 모든 노드를 넣을 때/뺄 때 각 O(n) 시간을 소모함

Space Complexity: O(n)
- 스택에 모든 노드를 넣었다가 빼야 하므로

풀이방법:
- 스택의 LIFO 특성을 활용

노트:
- 풀이 1보다 공간 복잡도가 올라가지만, 더 이해하기 쉬운 풀이
"""

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 모든 노드를 순서대로 저장할 빈 리스트 생성
        nodes = []
        
        # 현재 노드를 헤드로 초기화
        node = head
        
        # 링크드 리스트의 모든 노드를 순회하며 리스트에 저장
        while node:
            nodes.append(node)
            node = node.next
        
        # 새 링크드 리스트의 시작점이 될 더미 노드
        dummy = ListNode(-1)
        
        # 새 리스트를 만들기 위한 포인터 초기화
        node = dummy
        
        # nodes 리스트에서 역순으로 노드를 꺼내서 새 리스트 구성
        while nodes:
            node.next = nodes.pop()  # 리스트의 마지막 노드를 꺼내서 연결
            node = node.next         # 노드 이동
        
        # 마지막 노드의 next를 None으로 설정하여 리스트 종료
        node.next = None
        
        # 더미 노드의 next = 뒤집힌 리스트의 헤드
        return dummy.next
