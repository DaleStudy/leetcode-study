class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        N = max(nums)
        num_set = set()

        for i in range(N + 1):
            num_set.add(i)

        for num in nums:
            num_set.remove(num)

        if len(num_set) == 0:
            return N + 1
        else:
            return num_set.pop()
