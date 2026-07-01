class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # [3, 2, 4] -> {3: 0, 2: 1, 4: 2}
        # [3, 3] -> {3: 1}. use last index for the same value.
        num_dict = {num: i for i, num in enumerate(nums)}

        for i in range(len(nums)):
            diff = target - nums[i]

            # example 2) nums = [3, 2, 4], target = 6
            # prevent 3 to be answer because 3 is only one
            if diff in num_dict and i == num_dict[diff]:
                continue

            if diff in num_dict:
                return [i, num_dict[diff]]

        return []
