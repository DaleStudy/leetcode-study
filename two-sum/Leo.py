class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for key, val in enumerate(nums):
            diff = target - val

            if diff in seen:
                return [seen[diff], key]
            else:
                seen[val] = key

    # TC: O(n), SC: O(n)
