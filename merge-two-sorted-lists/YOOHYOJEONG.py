# https://leetcode.com/problems/merge-two-sorted-lists

# gpt의 도움을 받아 해결했습니다
class Solution:
    def mergeTwoLists(self, list1, list2):
        # base case 1:
        # list1이 비어있으면, 남은 list2를 그대로 반환
        if not list1:
            return list2
        
        # base case 2:
        # list2가 비어있으면, 남은 list1을 그대로 반환
        if not list2:
            return list1

        # 두 리스트의 현재 노드 값을 비교
        if list1.val < list2.val:
            # list1의 값이 더 작으면
            # list1을 결과 리스트의 현재 노드로 선택
            
            # list1의 다음 노드는
            # (list1.next와 list2를 다시 병합한 결과)로 연결
            list1.next = self.mergeTwoLists(list1.next, list2)
            
            # 현재 선택된 list1을 반환
            return list1
        else:
            # list2의 값이 더 작거나 같으면
            # list2를 결과 리스트의 현재 노드로 선택
            
            # list2의 다음 노드는
            # (list1과 list2.next를 다시 병합한 결과)로 연결
            list2.next = self.mergeTwoLists(list1, list2.next)
            
            # 현재 선택된 list2를 반환
            return list2
