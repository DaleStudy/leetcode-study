#이 문제의 제약조건 : 1) 인접한 집은 방문할 수 없음, 2)각 집에는 일정 금액의 돈이 있음, 3) 최대로 훔칠 수 있는 금액을 구해야 함
#이 문제는 각 위치에서 두 가지 선택이 있음 : 1) 현재 집을 털기(이전 집은 털 수 없음), 2) 현재 집을 털지 않기(이전 집은 털 수 있음)
#Example 1.의 예시를 들어 생각해보면,

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        #특수 케이스 처리 : 베열이 비어 있거나, 길이가 1인 경우
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        
        #첫번째 집의 금액을 저장 prev2 = 1
        #이 값은 0번째 집까지 털 수 있는 최대 금액을 의미
        prev2 = nums[0]
        #첫 두 집 중 최대 금액을 저장 max(1, 2) = 2
        prev1 = max(nums[0], nums[1])
        
        #i = 2 (세번째 집, value = 3)
        for i in range(2, n):
            #현재 집을 털거나 털지 않는 경우 중 최대값 : 
            #현재 집 털기 : prev2 + num[2] = 1 + 3 = 4
            #현재 집 안 털기 : prev1 = 2 
            #current = max(2, 4) = 4 
            current = max(prev1, prev2 + nums[i])
            #다음 반복을 위해 값 업데이트
            #prev2, prev1 = 2, 4
            prev2, prev1 = prev1, current
        
        return prev1
        #i = 3까지 했을 때 최대로 훔칠 수 있는 금액은 4

        #시간 복잡도 
            #O(n), n은 집의 수
        #공간 복잡도
            #O(1) DP 배열을 사용하는 방법보다 변수 2개만 사용하는 방식이 
            #공간 복잡도는 동일하면서 공간을 절약할 수 있어 더 효율적임          
