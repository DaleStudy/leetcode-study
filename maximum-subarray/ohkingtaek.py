class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        현재까지 이어서 만든 부분합이 음수면 버리고 다시 시작하여 갱신 하는 것입니다.
        """
        now_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            now_sum = max(num, now_sum + num)
            max_sum = max(max_sum, now_sum)
        return max_sum

