# 연결 리스트의 노드를 정의하는 클래스
class ListNode:
    def __init__(self, val=0, next=None):
        # 노드의 값
        self.val = val
        # 다음 노드를 가리키는 포인터 
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode):
        # 더미 노드 생성 - 결과 리스트의 시작점으로 사용
        dummy = ListNode()
        # 현재 위치를 추적하는 포인터
        current = dummy
        
        # 병합과정 : 두 리스트가 모두 존재하는 동안 반복, 
        # 작은 값을 가진 노드를 선택해 결과 리스트에 추가, 
        # 선택된 리스트의 포인터를 다음 노드로 이동
        # 결과 리스트의 포인터도 다음으로 이동 
        while list1 and list2:
            # list 1의 값이 list2의 값보다 작거나 같은 경우
            if list1.val <= list2.val:
                # list1의 노드를 결과에 추가
                current.next = list1
                #list1의 포인터를 다음 노드로 이동
                list1 = list1.next
            else:
                #list2의 노드를 결과에 추가
                current.next = list2
                #list2의 포인터를 다음 노드로 이동
                list2 = list2.next
                #결과 리스트의 포인터를 다음으로 이동
            current = current.next
        
        # 한 리스트가 끝나면 다른 리스트의 남은 노드들을 모두 연결
        ## list1에 남은 노드가 있으면 모두 연결
        if list1:
            current.next = list1
        
        ## list2에 남은 노드가 있으면 모두 연결
        else:
            current.next = list2

        # 더미 노드의 다음 노드부터가 실제 결과    
        return dummy.next


#시간 복잡도 (Time Complexity): O(n + m)
    #n: list1의 길이
    #m: list2의 길이
    #이유:
        #각 리스트의 모든 노드를 정확히 한 번씩만 방문
        #각 노드에서의 연산(비교, 연결)은 상수 시간
        #따라서 전체 시간 복잡도는 O(n + m)
#공간 복잡도 (Space Complexity): O(1)
    #이유:
        #추가적인 데이터 구조를 사용하지 않음
        #사용하는 변수:
        #dummy: 상수 공간
        #current: 상수 공간
        #입력 크기와 관계없이 일정한 메모리만 사용
        #따라서 공간 복잡도는 O(1)

