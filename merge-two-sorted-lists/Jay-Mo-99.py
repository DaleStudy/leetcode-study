        #해석
        #list1 과 list2는 이미 오름차순 정렬된 리스트
        #두 리스트의 첫 노드값을 비교해 더 작은값을 첫번째 노드로 선택
        #이후 선택된 노드의 next포인터를 재귀적으로 처리하여 노드 병합 


        #Big O
        #N: 매개변수 n의 크기(계단 갯수)
        
        #Time Complexity: O(M + N)
        #- M: list1의 길이 
        #- N: list2의 길이
        #- 각 재귀 호출에 하나의 노드가 다뤄진다, 따라서 최대 M+N 번의 재귀호출 발생

        
        #Space Complexity: O(M+N)
        #- 병합 리스트의 최대 길이 M+N이므로, 스택 공간 사용도 이에 비례한다.  

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        if list1 and list2: ## 두 리스트가 모두 비어있지 않은 경우에만 해당 
            if list1.val > list2.val: # list1의 현재 값이 list2보다 크다면
                list1, list2 = list2, list1 # 값을 교환하여 항상 list1이 더 작은 값을 가짐
            list1.next = self.mergeTwoLists(list1.next, list2) # list1의 다음 노드와 list2로 재귀 호출
        return list1 or list2 # 리스트가 하나라도 비어 있다면 비어 있지 않은 리스트를 반환


