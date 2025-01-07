"""
	풀이 : 비지 않을경우 합 nSum을 구하고 list를 돌면서 빼고 남은 것이 답
 

	TC : O(N)
		sum구할 떄 O(N) + for문 O(N) = O(2N)\

	SC : O(1)
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nSum = sum(range(0,len(nums) + 1))
        for num in nums :
            nSum -=num
        return nSum
