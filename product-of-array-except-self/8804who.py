class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total_product = 1

        for num in nums:
            if num != 0:
                total_product *= num
        
        if nums.count(0) == 1:
            return [0 if num != 0 else total_product for num in nums]
        elif nums.count(0) > 1:
            return [0 for _ in range(len(nums))]
        else:
            return [total_product//num for num in nums]
    


