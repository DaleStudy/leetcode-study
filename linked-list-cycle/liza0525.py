# 7기 풀이
class Solution:
    # 1. 첫번째 풀이: 이 풀이는 한 칸 씩 헤드를 옮기는 것과 두 칸 씩 헤드를 옮기는 것을 비교하여
    #                헤드가 동일해지면 해당 리스트는 순환한다는 아이디어에서 착안
    # 시간 복잡도: O(n)
    # - 리스트의 길이(n) 만큼의 시간이 최대
    # 공간 복잡도: O(1)
    # - slow, fast 변수만 사용
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        
        while slow and fast:
            slow = slow.next

            if not fast.next:
                # fast의 다음 노드가 없다면
                # 순환이 되지 않다는 것을 의미하므로 loop 탈출
                break
            fast = fast.next.next

            if slow == fast:
                # 같아지는 순간이 순환한다는 것을 의미하므로 True로 early return
                return True

        # loop 탈출 조건에 의해 순환하지 않음을 확인하여 False return
        return False

    # 2. 두번째 풀이: 이미 방문한 노드에 다시 방문하는 경우에 순환한다고 판단
    # 시간 복잡도: O(n)
    # - 리스트의 길이(n) 만큼의 시간이 최대
    # 공간 복잡도: O(n)
    # - list의 길이(n)이 최대 공간 복잡도(checked가 늘어남)
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        checked = set()  # 노드 방문 여부를 저장
        curr = head

        while curr:  # curr가 None이 되기 전까지(== 끝에 도달할 때까지)
            if curr in checked:
                # 이미 방문한 노드라면 순환한다는 의미이므로 True로 early return
                return True
            
            # 방문한 노드는 checked에 추가
            checked.add(curr)
            curr = curr.next  # 다음 node 탐색

        # loop 탈출 조건에 의해 순환하지 않음을 확인하여 False return
        return False
