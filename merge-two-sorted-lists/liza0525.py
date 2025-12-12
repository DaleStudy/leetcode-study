# 시간 복잡도: O(m + n)
# - 두 연결 리스트(list1, list2)를 각각 한 번씩만 순회하면 된다.
# - 각 노드를 정확히 한 번씩만 비교·이동하므로 전체 길이에 선형 시간.

# 공간 복잡도: O(1)
# - 새로운 노드를 생성해 리스트를 복제하지 않고,
#   기존 리스트 노드들을 그대로 이어붙이기 때문에 추가 메모리는 거의 없다.
# - 연결 작업을 위한 dummy 노드 1개만 사용.



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 결과 리스트의 첫 지점을 쉽게 관리하기 위해 더미(Dummy) 노드를 만든다.
        root_node = ListNode()
        cur_node = root_node  # 현재 결과 리스트를 이어가는 포인터

        # 두 리스트가 모두 남아있는 동안 반복한다.
        # - 각 리스트의 head를 비교해 더 작은 쪽을 결과 리스트에 붙인다.
        while list1 and list2:
            if list1.val < list2.val:
                # list1의 노드를 결과 리스트에 연결하고 list1 포인터를 다음으로 이동
                cur_node.next = list1
                list1 = list1.next
            else:
                # list2의 노드를 결과 리스트에 연결하고 list2 포인터를 다음으로 이동
                cur_node.next = list2
                list2 = list2.next

            # 결과 리스트 포인터도 한 칸 전진
            cur_node = cur_node.next

        # 어느 한쪽이 끝났다면, 남아 있는 리스트 전체를 그대로 이어붙인다.
        # - 이미 정렬되어 있으므로 추가 비교 없이 한 번에 연결 가능
        cur_node.next = list1 or list2

        # dummy 노드 다음부터가 실제 머지된 리스트의 시작점
        return root_node.next
