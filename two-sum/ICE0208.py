class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # key: num / value: index of num (key)
        prev = {}

        for i, num in enumerate(nums):
            # need = target이 되기위한 숫자 
            need = target - num

            # 이전에 봤던 숫자들 중에 need 와 같은 숫자가 있으면 끝
            if need in prev:
                return [prev[need], i]
            else:
                prev[num] = i

        return []
