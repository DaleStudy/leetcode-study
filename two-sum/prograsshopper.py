class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_dict = {elem: idx for idx, elem in enumerate(nums)}
        result = []
        for idx, num in enumerate(nums):
            remain = index_dict.get(target-num, None)
            if remain and idx != remain:
                result = [idx, remain]
                break
        return result
