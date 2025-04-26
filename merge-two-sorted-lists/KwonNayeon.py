"""
Constraints:
 1. 0 <= list1.length, list2.length <= 50 
 2. -100 <= Node.val <= 100
 3. list1 and list2 are sorted in non-decreasing order

<Solution 1>

Time Complexity: n과 m이 각각 list1과 list2의 길이를 나타낼 때, O(n + m)
 - 각 노드를 한 번씩만 방문하기 때문

Space Complexity: O(1)
 - 새로운 노드를 만들지 않고 기존 노드들의 연결만 바꾸기 때문

풀이 방법:
 1. 더미 노드를 만들어서 결과 리스트의 시작점으로 사용
 2. 두 리스트를 앞에서부터 순회하면서 값을 비교
 3. 더 작은 값을 가진 노드를 결과 리스트에 연결하고, 해당 리스트의 포인터를 다음으로 이동
 4. 한쪽 리스트가 끝나면, 남은 리스트를 그대로 결과 리스트 뒤에 연결
 5. 더미 노드의 next를 반환 (실제 정렬된 리스트의 시작점)
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        current = result

        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return result.next

"""
<Solution 2>
Time Complexity:

Space Complexity:

풀이 방법:
"""
