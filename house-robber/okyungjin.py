# https://leetcode.com/problems/house-robber/description/

# 훔칠 수 있는 최대 금액을 구한다
# 단 연속된 집을 훔치면 경찰에 체포됨

# 앞집, 앞앞집의 최대 수익을 아래 변수들에 기록한다
# prev2, prev1, curr

# Time: O(N)
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev2 = 0 # 앞앞집 최대 수익
        prev1 = 0 # 앞집 최대 수익
        
        for num in nums:
            # 현재 최대 수익은
            # 1) 앞집 수익
            # 2) 앞앞집 수익 + 현재수익
            curr = max(prev1, prev2 + num)

            # 다음 턴을 위해 값을 슬라이딩(?)
            # prev3 prev2 prev1 curr
            #         a     b    c
            #  a      b     c 
            prev2 = prev1
            prev1 = curr

        # 순회 끝나면 직전 최대 수익이 prev1에 저장됨
        return prev1
            
