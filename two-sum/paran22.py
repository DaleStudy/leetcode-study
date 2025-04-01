class Solution:
    # 시간복잡도 : O(n)
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {num: i for i, num in enumerate(nums)}

        for i, first_num in enumerate(nums):
            second_num = target - first_num
            if second_num in num_dict and num_dict[second_num] != i:
                return [i, num_dict[second_num]]

