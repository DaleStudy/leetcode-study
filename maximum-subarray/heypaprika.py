"""
복잡도 : 예상 -> 예상한 이유

시간 복잡도 : O(n) -> len(nums) 만큼 반복
공간 복잡도 : O(n) -> len(nums) 크기의 배열 a 생성
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        a = [0] * len(nums)
        a[0] = nums[0]
        for i in range(1, len(nums)):
            a[i] = max(nums[i], nums[i]+a[i-1])
        return max(a)

