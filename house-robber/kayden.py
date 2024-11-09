class Solution:
    # 시간복잡도: O(N)
    # 공간복잡도: O(1)
    def rob(self, nums: List[int]) -> int:
        one, two = 0, 0

        for num in nums:
            temp = max(two+num, one)
            two, one = one, temp

        return one
