class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_dict = {}

        for idx1, num1 in enumerate(nums):
            num2 = target - num1
            idx2 = nums_dict.get(num2)

            if idx2 is None:
                nums_dict.update({num1: idx1})
            else:
                return [idx1, idx2]

        raise Exception("Invalid nums and target")


if __name__ == "__main__":
    test_cases = [
        ([2, 7, 11, 15], 9, {0, 1}),
        ([3, 2, 4], 6, {1, 2}),
        ([3, 3], 6, {0, 1}),
        ([-2, -3, 0, 3], 1, {0, 3}),
        ([0, -5, 2, 6], -3, {1, 2}),
        ([4, 7, 2, 0, 0], 0, {3, 4}),
    ]

    solution = Solution()
    for idx, case_ in enumerate(test_cases):
        nums, target, answer = case_
        result = solution.twoSum(nums, target)
        assert answer == set(
            result
        ), f"Test Case {idx} Failed: Expected {answer}, Got {result}"
