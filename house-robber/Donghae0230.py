# 시간 복잡도
# nums의 길이에 여러 분기로 나뉨 -> O(2^n) -> Time Limit Exceeded로 실패
# 공간 복잡도
# 재귀 깊이에 따라 늘어남 -> 최대 O(n)

class Solution:
    def temp(self, n, nums, val, lst):
        if n+2 >= len(nums):
            lst.append(val)
            lst = max(lst)
            return lst
        for i in range(n+2, len(nums)):
            self.temp(i, nums, val+nums[i], lst)
        lst = max(lst)
        return lst

    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            start_0 = self.temp(0, nums, nums[0], [])
            start_1 = self.temp(1, nums, nums[1], [])
            return max(start_0, start_1)
        else:
            return nums[0]
