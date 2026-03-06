class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        for idx1, num1 in enumerate(nums):
            back = nums[idx1 + 1 :]
            for idx2, num2 in enumerate(back):
                if num1 + num2 == target:
                    return [idx1, idx1 + idx2 + 1]

        raise Exception("Invalid nums and target")


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-2, -3, 0, 3], 1, [0, 3]),
        ([0, -5, 2, 6], -3, [1, 2]),
        ([4, 7, 2, 0, 0], 0, [3, 4]),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        nums, target, answer = case_
        result = solution.twoSum(nums, target)
        assert (
            answer == result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
