class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_pos = set()

        for i in range(len(nums)):
            num = nums[i]
            if num != 0:
                product *= num
            else:
                zero_pos.add(i)
        
        if len(zero_pos) >= 2:
            return [0 for num in nums]
        elif len(zero_pos) == 1:
            return [0 if i not in zero_pos else product for i in range(len(nums))]
        else:
            return [int(product / num) for num in nums]
