class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for idx1, num1 in enumerate(nums):
            back = nums[idx1 + 1 :]
            for idx2, num2 in enumerate(back):
                if num1 + num2 == target:
                    return [idx1, idx1 + idx2 + 1]

        raise Exception("Invalid nums and target")
