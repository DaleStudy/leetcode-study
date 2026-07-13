# from typing import Optional, List

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#     # 파이썬의 toString 역할을 하는 __repr__을 [1,3,4] 형태로 출력되게 수정
#     def __repr__(self):
#         nodes = []
#         curr = self
#         while curr:
#             nodes.append(str(curr.val))
#             curr = curr.next
#         return "[" + ",".join(nodes) + "]"

# # 파이썬 list를 ListNode 리스트로 변환해주는 헬퍼 함수
# def make_linked_list(arr: List[int]) -> Optional[ListNode]:
#     if not arr:
#         return None
#     dummy = ListNode(0)
#     curr = dummy
#     for val in arr:
#         curr.next = ListNode(val)
#         curr = curr.next
#     return dummy.next


# list1의 노드 개수를 n, list2의 노드 개수를 m이라 할 때
# 시간 복잡도: O(n + m)
# 공간 복잡도: O(n + m) -> 
class Solution_01:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 맨 앞에 더미 노드를 하나 추가한다
        # 없는 상태로 짰는데 if node: else: 구문 늘어나서 맨 앞에 가상의 노드를 하나 추가해줬다
        dummy = ListNode(None)
        node = dummy
        
        while True:
            # list1이 비어있으면 현재 노드 뒤로 list2를 이어준다.
            if not list1:
                node.next = list2
                break
            
            # list2가 비어있으면 현재 노드 뒤로 list1을 이어준다.
            if not list2:
                node.next = list1
                break
                
            # 값을 비교해서 작은 값을 next 노드에 추가한다.
            if list1.val <= list2.val:
                node.next = ListNode(list1.val)
                # list1 하나 소비
                list1 = list1.next
            else:
                node.next = ListNode(list2.val)
                # list2 하나 소비
                list2 = list2.next
    
            # 다음 노드를 현재 노드로 할당해준다
            node = node.next

        return dummy.next
    

# [접근법] Solution_01 의 공간 복잡도를 개선했습니다.
# ListNode를 새로 생성하지 않고 기존 노드를 활용하도록 수정했습니다.

# list1의 노드 개수를 n, list2의 노드 개수를 m이라 할 때
# 시간 복잡도: O(n + m)
# 공간 복잡도: O(1) -> dummy만 사용, 추가 공간 복잡도는 O(1)
class Solution_01:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 맨 앞에 더미 노드를 하나 추가한다
        # 없는 상태로 짰는데 if node: else: 구문 늘어나서 맨 앞에 가상의 노드를 하나 추가해줬다
        dummy = ListNode(None)
        node = dummy
        
        while True:
            if not list1: # list1이 비어있으면 현재 노드 뒤로 list2를 이어준다.
                node.next = list2
                break
            
            if not list2: # list2가 비어있으면 현재 노드 뒤로 list1을 이어준다.
                node.next = list1
                break
                
            # 값을 비교해서 작은 값을 next 노드에 추가한다.
            if list1.val <= list2.val:
                node.next = list1 # 새로운 ListNode를 생성하지 않고 list1를 할당해준다.
                list1 = list1.next # list1 하나 소비
            else:
                node.next = list2 # 새로운 ListNode를 생성하지 않고 list2를 할당해준다.
                list2 = list2.next # list2 하나 소비
    
            # 다음 노드를 현재 노드로 할당해준다
            node = node.next

        return dummy.next


# 4. 예시 입력으로 호출 및 테스트
# if __name__ == "__main__":
#     list1 = make_linked_list([1, 2, 4])
#     list2 = make_linked_list([1, 3, 4])
    
#     solution = Solution()
#     merged_list = solution.mergeTwoLists(list1, list2)

#     print(merged_list)
