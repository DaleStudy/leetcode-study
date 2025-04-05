class Solution(object):
    def rob(self, nums):
        """
        # 초기 풀이
        rob_house_even = 0 # 짝수 집들을 터는 경우 금액의 합
        rob_house_odd = 0 # 홀수 집들을 터는 경우 금액의 합 
        for index, value in enumerate(nums):
            if index % 2 == 0:
                rob_house_even += value
            else:
                rob_house_odd += value
            
        return max(rob_house_even, rob_house_odd)
        # 실패:
        # 단순히 짝수와 홀수를 구분하는 것만으로 
        # 최적 해를 구할 수 없음

        ===========================================

        동적 프로그래밍을 활용해서 문제를 해결
        각각의 최적 해를 누적하여 마지막까지의 최적 해를 구해야 함
        
        """
        if not nums: # 빈 리스트가 주어질 경우, 0을 반환
            return 0
        if len(nums) == 1: # 요소가 하나인 경우, 그 값을 반환
            return nums[0]
        
        # prev2: i-2번째까지 고려 했을 때의 최대 금액
        # prev1: i-1번째까지 고려 했을 때의 최대 금액
        # 초기값 설정:
        # - 첫 번째 집(인덱스 0)만 고려한 경우 nums[0]
        # - 두 번째 집(인덱스 1)까지 고려한 경우 첫 번째 집과 두 번째 집 중 큰 값
        prev2, prev1 = nums[0], max(nums[0], nums[1])

        for i in range(2, len(nums)):
            # 두 선택지 중 더 금액이 큰 경우를 계산
            # 1. i번째 집을 털지 않을 때: 이전까지의 최대 금액 prev1
            # 2. i번째 집을 털 때: i-1번째 집은 털 수 없음
            #    i-2번째 집까지의 최대 금액 prev2에 현재 집의 금액 nums[i]를 더함
            current = max(prev1, prev2 + nums[i])

            # 이전 단계의 prev1은 다음 단계에서 prev2가,
            # current 값은 새로운 prev1이 됨
            prev2, prev1 = prev1, current
        
        # 마지막 집까지의 최대 금액인 prev1 반환 
        return prev1
