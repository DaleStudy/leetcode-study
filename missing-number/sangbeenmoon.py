class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        visited = {}
        for num in nums:
            visited[num] = True
        for i in range(len(nums) + 1):
            if i in visited:
                continue
            else:
                return i
        return 0

