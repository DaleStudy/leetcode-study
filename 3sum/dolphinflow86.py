# 1) Fix one element first, and then treat others as two-sum problem. Use set to get rid of duplicate combination.
# TC: O(N^2) where N is the length of nums.
# SC: O(N) where N is the length of nums.
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        answer: Set[tuple[int,int,int]] = set()
        n = len(nums)
        nums.sort()
        
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]: continue

            target = -nums[i]            
            nums_map: Dict[int, int] = {}
            for j in range(i + 1, n):
                comp = target - nums[j]
                if comp in nums_map:
                    answer.add((nums[i], comp, nums[j]))
                nums_map[nums[j]] = j

        return [list(triplet) for triplet in answer]
