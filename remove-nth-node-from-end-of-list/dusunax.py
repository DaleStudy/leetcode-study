'''
# 19. Remove Nth Node From End of List

## 풀이 접근방식 레퍼런스
- https://www.algodale.com/problems/remove-nth-node-from-end-of-list/
'''
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        # 1. 노드 리스트
        - 음수 인덱스 원소 접근
        - nodes 배열을 사용하여 마지막 n번째 노드를 찾는다.
        - 메모리 낭비
        TC: O(N), SC: O(N)
        '''
        # nodes = [] # 배열
        # temp = ListNode(None, head)
        # node = temp

        # while node:
        #     nodes.append(node)
        #     node = node.next
        
        # nodes[-n - 1].next = nodes[-n - 1].next.next

        # return temp.next

        '''
        # 2. 큐
        - 큐를 사용하여 마지막 n번째 노드를 찾는다.
        - 최대 n+1개의 노드(필요한 범위)만 유지, 슬라이딩 윈도우
        TC: O(N), SC: O(N)
        '''
        # queue = deque() #큐
        # temp = ListNode(None, head)
        # node = temp

        # for _ in range(n + 1):
        #     queue.append(node)
        #     node = node.next
        
        # while node:
        #     queue.popleft()
        #     queue.append(node)
        #     node = node.next

        # queue[0].next = queue[0].next.next
        # return temp.next

        '''
        # 3. 포인터
        - 연결 리스트의 특성 이용
        - 첫번째 포인터는 n번 이동하여 마지막 노드를 찾는다.
        - 두번째 포인터는 첫번째 포인터가 마지막 노드를 찾을 때까지 이동한다.
        - 두번째 포인터는 첫번째 포인터가 마지막 노드를 찾으면 첫번째 포인터의 이전 노드를 삭제한다.
        TC: O(N), SC: O(1)
        '''
        first = head
        for _ in range(n):
            first = first.next

        temp = ListNode(None, head)
        second = temp
        
        while first:
            first = first.next
            second = second.next

        second.next = second.next.next
        return temp.next 
