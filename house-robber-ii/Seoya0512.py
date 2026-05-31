'''
Time Complexity: O(N)
- dpf 함수를 nums의 길이에 대해 2번 호출 하므로 O(N) + O (N) = O(N)

Space Complexity: O(N)
- dfp 함수에서 dp 배열을 생성해서 저장하는 공강 O(N) 소요     
'''
from typing import (
    List,
)

def rob(nums: List[int]) -> int:
    def dpf(nums):
        dp = [0]+[0] * len(nums)
        for idx in range(1, len(dp)):
            dp[idx] = max(dp[idx-2]+ nums[idx-1], dp[idx-1])
        print(dp)
        return dp[-1]

    return max(dpf(nums[1:]),dpf(nums[:-1]))
