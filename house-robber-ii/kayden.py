class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robLinear(houses: List[int]) -> int:
            one, two = 0, 0
            for money in houses:
                one, two = two, max(two, one + money)
            return two

        return max(robLinear(nums[1:]), robLinear(nums[:-1]))
