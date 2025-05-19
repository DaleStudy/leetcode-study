'''
문제 의도 : linked list가 주어졌을 때, 이 리스트를 순서를 반대로 해서 반환하는 문제임
해결 방법 : 리스트를 처음부터 끝까지 한번씩 돌면서 각 노드의 다음 노드를 이전 노드로 바꿔주면 됨

시간 복잡도: O(n)
    리스트의 모든 노드를 한 번씩만 방문하므로
공간 복잡도: O(1)
    추가로 사용하는 변수는 prev, curr, next_temp 세 개뿐임

Example 1.의 경우

단계	prev	curr	next_temp	리스트 상태
1	   None	    1	    2	        1 → None, 2 → 3 → 4 → 5
2	    1	    2	    3	        2 → 1 → None, 3 → 4 → 5
3	    2	    3	    4	        3 → 2 → 1 → None, 4 → 5
4	    3	    4	    5	        4 → 3 → 2 → 1 → None, 5
5	    4	    5	    None	    5 → 4 → 3 → 2 → 1 → None

'''

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]):
        prev = None           # 이전 노드를 저장할 변수. 맨 처음엔 아무것도 없으므로 None으로 시작
        curr = head           # 현재 작업할 노드를 head(리스트의 첫번째 노드)로 시작함

        # 현재 노드가 None이 아닐 때(= 끝까지 가지 않았을 때) 반복함
        while curr:           
            # 현재 노드의 다음 노드를 임시로 저장함(다음 줄에서 연결을 바꿔버리기 때문).
            next_temp = curr.next   
            # 현재 노드의 next를 이전 노드로 바꿔줌(=화살표 방향을 뒤집는 역할)
            curr.next = prev        
            # prev를 현재 노드로 이동
            prev = curr             
            # curr를 다음 노드로 이동시킴
            curr = next_temp        
        # 반복이 끝나면 prev가 역순으로 바뀐 리스트의 첫 번째 노드(새로운 head)가 됨
        return prev           



