class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_dict = {x: 1 for x in nums}

        max_count = 0
        for num in nums:
            res = self.dfs(num_dict, nums, num, 0)
            max_count = max(max_count, res)

        return max_count

    def dfs(self, num_dict: Dict, nums: List[int], num: int, count: int):
        if num not in num_dict:
            return 0

        if num_dict[num] == 0:
            return 0

        num_dict[num] = 0
        left_count = self.dfs(num_dict, nums, num - 1, 0)
        right_count = self.dfs(num_dict, nums, num + 1, 0)

        return 1 + left_count + right_count
